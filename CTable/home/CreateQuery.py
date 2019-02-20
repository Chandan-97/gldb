cn_customer = "cn_customer_mst."
FROM = "FROM  rw_service_mst LEFT JOIN cn_customer_mst_1 ON " \
       "rw_service_mst.customer_no=cn_customer_mst_1.customer_no LEFT JOIN gsfs_model ON " \
       "rw_service_mst.model_code=gsfs_model.model_code "
gsfs_model_code = "gsfs_model.model_code="
rw_service = "rw_service_mst."
WHERE = "WHERE length(trim(rw_service_mst.serial_no))=13 " \
        "AND SUBSTR(rw_service_mst.serial_no, 1, 3) regexp '^\\d{3}' " \
        "AND rw_service_mst.service_type_code in ('IS','MS')"

# table name for recency, frequecy and monetary value
# "AND rw_service_mst.serial_no first 3 " \
RFM = "RFM."

def CreateQuery(req):
    print(req)
    global cn_customer, FROM, gsfs_model_code, rw_service

    # Filter the data
    # Product Data
    Product = []
    Product.append(True) if req.get("ProductInfo[select_product]") == 'true' else Product.append(False)
    products = req.getlist("ProductInfo[product_list][]")
    for p in products: Product.append(p)

    # print("Product")
    # print(Product)
    # print("===============")


    # Purchase Data
    Purchase = []
    Purchase.append(True) if req.get("PurchaseDateInfo[purchaseDate]") == 'true' else Purchase.append(False)

    Purchase.append(True) if req.get("PurchaseDateInfo[purchaseBefore]") == 'true' else Purchase.append(False)
    Purchase.append(req.get("PurchaseDateInfo[purchaseBeforeDate]").replace("-", ""))

    Purchase.append(True) if req.get("PurchaseDateInfo[purchaseAfter]") == 'true' else Purchase.append(False)
    Purchase.append(req.get("PurchaseDateInfo[purchaseAfterDate]").replace("-", ""))

    # print("Purchase")
    # print(Purchase)
    # print("===============")


    # Warranty Data
    Warranty = []
    Warranty.append(True) if req.get("WarrantyInfo[warranty]") == 'true' else Warranty.append(False)
    if req.get("WarrantyInfo[warranty_status]")=="BOTH":
        Warranty.append("IW"); Warranty.append("OW")
    else:
        Warranty.append(req.get("WarrantyInfo[warranty_status]"))
    #
    # print("Warranty")
    # print(Warranty)
    # print("===============")


    # Recency Data
    Recency = []
    Recency.append(True) if req.get("RecencyInfo[name]") == "true" else Recency.append(False)

    Recency.append(True) if req.get("RecencyInfo[from]") == "true" else Recency.append(False)
    Recency.append(req.get("RecencyInfo[from_val]"))

    Recency.append(True) if req.get("RecencyInfo[to]") == "true" else Recency.append(False)
    Recency.append(req.get("RecencyInfo[to_val]"))
    #
    # print("Recency")
    # print(Recency)
    # print("===============")


    # Frequency Data
    Frequency = []
    Frequency.append(True) if req.get("FrequencyInfo[name]") == "true" else Frequency.append(False)

    Frequency.append(True) if req.get("FrequencyInfo[from]") == "true" else Frequency.append(False)
    Frequency.append(req.get("FrequencyInfo[from_val]"))

    Frequency.append(True) if req.get("FrequencyInfo[to]") == "true" else Frequency.append(False)
    Frequency.append(req.get("FrequencyInfo[to_val]"))
    #
    # print("Frequency")
    # print(Frequency)
    # print("===============")


    # Monetary Data
    Monetary = []
    Monetary.append(True) if req.get("MonetaryInfo[name]") == "true" else Monetary.append(False)

    Monetary.append(True) if req.get("MonetaryInfo[from]") == "true" else Monetary.append(False)
    Monetary.append(req.get("MonetaryInfo[from_val]"))

    Monetary.append(True) if req.get("MonetaryInfo[to]") == "true" else Monetary.append(False)
    Monetary.append(req.get("MonetaryInfo[to_val]"))
    #
    # print("Monetary")
    # print(Monetary)
    # print("===============")


    # Output Fields
    output = []
    op = req.getlist("OutputFields[output_list][]")
    for o in op: output.append(o)

    # print("Output")
    # print(output)
    # print("===============")


    # RFAndOr
    FMAndOr = []
    FMAndOr.append(req.get("FAndOr[F_AND_OR]"))
    FMAndOr.append(req.get("MAndOr[M_AND_OR]"))

    # end of Filtering the data


    # Let's fuck some bitches
    query = "SELECT DISTINCT cn_customer_mst_1.customer_no "
    for f in output:
        query += (", "+cn_customer+f+" ")
    debi = 0
    # print("[DEB %d] : %s"%(debi, query))
    debi += 1


    query += FROM
    # print("[DEB %d] : %s"%(debi, query))
    debi += 1

    where_list1 = []

    if Product[0]:
        where = "("
        for i in range(1, len(Product)):
            p = Product[i]
            if i==len(Product)-1: where += (gsfs_model_code+"'"+p+"'")
            else: where += (gsfs_model_code+"'"+p+"' OR ")
        where += ")"
        # print("[DEB %d] : %s" % (debi, query))
        debi += 1
        where_list1.append(where)

    if Purchase[0]:
        where = "("
        if Purchase[1] and Purchase[3]:
            where += "CAST(DATE_FORMAT("+rw_service+"purchase_date, %X%m) AS INT) BETWEEN str_to_date('"+Purchase[2]+"', '%Y-%m') AND "
            where += "'"+Purchase[4]+"'"
        elif Purchase[1]:
            where += rw_service+"purchase_date <= str_to_date('"+Purchase[2]+"', '%Y-%m'"
        elif Purchase[3]:
            where += rw_service+"purchase_date >= str_to_date'"+Purchase[4]+"', '%Y-%m'"

        if(Purchase[1] or Purchase[3]):
            where += ")"
            # print("[DEB %d] : %s" % (debi, where))
            debi += 1
            where_list1.append(where)


    if Warranty[0] and len(Warranty) != 3:
        where = "("
        where += rw_service+"warranty_flag='"+Warranty[1]+"'"
        where += ")"

        # print("[DEB %d] : %s" % (debi, where))
        debi += 1
        where_list1.append(where)

    cnt = 0
    where_list2 = []
    if Recency[0]:
        cnt+=1
        where = "("
        if Recency[1] and Recency[3]:
            where += RFM+"recency BETWEEN "+Recency[2]+" AND "+Recency[4]
        elif Recency[1]:
            where += RFM+"recency >= "+Recency[2]
        elif Recency[2]:
            where += RFM+"recency <= "+Recency[4]
        # print("RECENCY : ", Recency)
        if(Recency[1] or Recency[3]):
            where += ")"
            # print("[DEB %d] : %s" % (debi, where))
            debi += 1
            where_list2.append(where)

    if Frequency[0]:
        cnt += 1
        where = "("
        if Frequency[1] and Frequency[3]:
            where += RFM + "frequency BETWEEN " + Frequency[2] + " AND " + Frequency[4]
        elif Frequency[1]:
            where += RFM + "frequency >= " + Frequency[2]
        elif Frequency[3]:
            where += RFM + "frequency <= " + Frequency[4]

        if Frequency[0] or Frequency[3]:
            where += ")"
            # print("[DEB %d] : %s" % (debi, where))
            debi += 1
            where_list2.append(where)

    if Monetary[0]:
        cnt += 1
        where = "("
        if Monetary[1] and Monetary[3]:
            where += RFM + "monetary BETWEEN " + Monetary[2] + " AND " + Monetary[4]
        elif Monetary[1]:
            where += RFM + "monetary >= " + Monetary[2]
        elif Monetary[3]:
            where += RFM + "monetary <= " + Monetary[4]

        if Monetary[0] or Monetary[3]:
            where += ")"
            # print("[DEB %d] : %s" % (debi, where))
            debi += 1
            where_list2.append(where)
    #
    # print("==================")
    # print("Where List: ")
    # for w in where_list1:
    #     print(w)
    # print("==================")
    # for w in where_list2:
    #     print(w)
    # print("==================")

    query += WHERE
    if len(where_list1) == 0 and len(where_list2) == 0:
        return query


    where1 = ""
    if len(where_list1) == 0:
        pass
    elif len(where_list1) == 1:
        where1 = where_list1[0]
    elif len(where_list1) == 2:
        where1 = where_list1[0] + " AND " + where_list1[1]
    elif len(where_list1) == 3:
        where1 = where_list1[0] + " AND " + where_list1[1] + " AND " + where_list1[2]


    where2 = ""
    if len(where_list2) == 1:
        where2 = where_list2[0]
    elif len(where_list2) == 2:
        where2 = where_list2[0]
        if Recency[0] and Frequency[0]:
            where2 += " " + FMAndOr[0] + " "
        elif Frequency[0] and Monetary[0]:
            where2 += " " + FMAndOr[1] + " "
        elif Recency[0] and Monetary[0]:
            where2 += " " + FMAndOr[0] + " "
    elif len(where_list2) == 3:
        where2 += where_list2[0]
        where2 += " " + FMAndOr[0] + " "
        where2 += where_list2[1]
        where2 += " " + FMAndOr[1] + " "
        where2 += where_list2[2]


    # print("=======================")
    # print("where1 : ", where1)
    # print("where2 : ", where2)

    if(len(where1) == 0 or len(where2) == 0):
        if(len(where1) == 0):
            query += " AND " + where2
        else:
            query += " AND " + where1
    else:
        query += where1 + " AND " + where2

    return query

