def getSql(v):
    service = "rw_service_mst"
    where = " "
    try:
        if(v["product1"] == "true"):
            where = where + service + ".model_code=" + v["product1_option"]
            where = where + " " + v["product1_and_or"] + " "
    except Exception as e:
        pass

    try:
        if(v["product2"] == "true"):
            where = where + service + ".model_code=" + v["product2_option"]
            where = where + " " + v["product2_and_or"] + " "
    except Exception as e:
        pass

    try:
        if(v["product3"] == "true"):
            where = where + service + ".model_code=" + v["product3_option"]
            where = where + " " + v["product3_and_or"] + " "
    except Exception as e:
        pass

    try:
        if(v["tenure"] == "true"):
            pass
    except Exception as e:
        pass

    try:
        if(v["warranty"] == "true"):
            where = where + service + ".warranty_flag=" + v["warranty_status"]
            where = where + " " + v["warranty_status_and_or"]
    except Exception as e:
        pass

    try:
        if(v["recency"] == "true"):
            pass
    except Exception as e:
        pass

    try:
        if(v["frequency"] == "true"):
            pass
    except Exception as e:
        pass

    try:
        if(v["monetary"] == "true"):
            pass
    except Exception as e:
        pass

    print(where)

#    remove extra and / or
    where = where.rstrip()
    where = where.rstrip("and")
    where = where.rstrip("or")
    where = where.rstrip()

    print("[DEB] : where : " + str(where))
    return where

def getSelect(v):
    customer = "cn_customer_mst_1"
    select = "SELECT " + customer + ".customer_no, " + customer + ".customer_name"

    try:
        if(v["phone_no"] == "true"):
            select = select + ", " + customer + ".phone_no"
    except Exception as e:
        pass

    try:
        if(v['email'] == "true"):
            select = select + ", " + customer + ".email_addr"
    except Exception as e:
        pass

    try:
        if(v['city']):
            select = select + ", " + customer + ".city_name"
            select = select + ", " + customer + ".state_name"
    except Exception as e:
        pass

    try:
        if(v['address']):
            select = select + ", " + customer + ".address_line1_info"
            select = select + ", " + customer + ".address_line2_info"
            select = select + ", " + customer + ".address_line3_info"
    except Exception as e:
        pass

    print("[DEB] : SELECT : " + str(select))
    return select



