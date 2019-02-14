function getCampaignInfo(){
    $campaign_name = $("#campaign_name").val().trim();
    $requestor_name = $("#requestor_name").val().trim();
    $request_date = $("#request_date").val().trim();
    $campaign_start_date = $("#campaign_start_date").val().trim();
    $campaign_end_date = $("#campaign_end_date").val().trim();
    $email = $("#email").val().trim();

    var campaign_arr = [];
    campaign_arr.push($campaign_name);
    campaign_arr.push($requestor_name);
    campaign_arr.push($request_date);
    campaign_arr.push($campaign_start_date);
    campaign_arr.push($campaign_end_date);
    campaign_arr.push($email);

    var Campaign = {
        "campaign_arr" : campaign_arr,
        "campaign_name" : $campaign_name,
        "requestor_name" : $requestor_name,
        "request_date" : $request_date,
        "campaign_start_date" : $campaign_start_date,
        "campaign_end_date" : $campaign_end_date,
        "email" : $email
    };

    return Campaign;
}

function getProductInfo(){
    $select_product = $("#select_product").is(":checked");
    $product = $("input[name=product]");
    $all = false;
    var prod_list = []
    for(var i=0; i<$product.length; i++){
        $prod = $product[i];
        if($prod.checked==true){
            if($prod.value == "ALL"){
                $all = true;
            }
            else{
                prod_list.push($prod.value);
            }
        }
        else if($all == true){
            prod_list.push($prod.value);
        }
    }

    // console.log(prod_list);
    // return prod_list;

    $products = {
        "select_product" : $select_product,
        "product_list" : prod_list
    };

    return $products;
}

function getPurchaseDateInfo() {
    $purchaseDate = $("#purchase_date").is(":checked");
    $purchaseBefore = $("#purchase_before").is(":checked");
    $purchaseAfter = $("#purchase_after").is(":checked");
    $purchaseBeforeDate = $("#purchase_before_date").val().trim();
    $purchaseAfterDate = $("#purchase_after_date").val().trim();

    var purchaseDate = {
        "purchaseDate": $purchaseDate,
        "purchaseBefore": $purchaseBefore,
        "purchaseAfter": $purchaseAfter,
        "purchaseBeforeDate": $purchaseBeforeDate,
        "purchaseAfterDate": $purchaseAfterDate
    };

    return purchaseDate;
}

function getWarrantyInfo(){
    $warranty = $("#warranty").is(":checked");
    $warranty_status = $("[name=warranty_status]:checked").val();

    $Warranty = {
        "warranty" : $warranty,
        "warranty_status" : $warranty_status
    };

    return $Warranty;
}

function getRFWInfo(RFWId){
    return {
        "name" : $(RFWId.name).is(":checked"),
        "from" : $(RFWId.from).is(":checked"),
        "to" : $(RFWId.to).is(":checked"),
        "from_val" : $(RFWId.from_val).val(),
        "to_val" : $(RFWId.to_val).val()
    };
}

function getOutputFields(){
    $OutputFields = $("input[name=output]");
    // console.log($OutputFields);
    $all = false;
    var output_list = [];
    for(var i=0; i<$OutputFields.length; i++){
        $output = $OutputFields[i];
        if($output.checked == true){
            if($output.value == "ALL") {
                $all = true;
            }
            else {
                output_list.push($output.value);
            }
        }
        else if($all == true)
            output_list.push($output.value);
    }

    $output_list = {
        "output_list" : output_list
    };

    return $output_list;
}

//Validation Fields Start

function getValidateCampaignInfo(Campaign){
    return true;
    for(var i=0; i<Campaign.campaign_arr.length; i++){
        $campField = Campaign.campaign_arr[i];
        if($campField.length <= 1)
            return false;
    }

    return true;
}

function getValidateProductInfo(ProductInfo){
    return true;
}

function getValidatePurchaseDateInfo(PurchaseDateInfo){
    return true;
}

function getValidateWarrantyInfo(WarrantyInfo){
    return true;
}

function getValidateRecencyInfo(RecencyInfo){
    return true;
}

function getValidateFrequencyInfo(FrequencyInfo){
    return true;
}

function getValidateMonetaryInfo(MonetaryInfo){
    return true;
}

function getValidateOutputFields(OutputFields){
    return true;
}
// Validation Fields Ends


$("#generate").on("click", function (event) {
    event.preventDefault();

    $CampaignInfo = getCampaignInfo();
    // console.log($CampaignInfo);

    $ProductInfo = getProductInfo();
    // console.log($ProductInfo);

    $PurchaseDateInfo = getPurchaseDateInfo();
    // console.log($PurchaseDateInfo);

    $WarrantyInfo = getWarrantyInfo();
    // console.log($WarrantyInfo);

    $recency_id = {
        "name"      : "#recency",
        "from"      : "#recency_from",
        "to"        : "#recency_to",
        "from_val"  : "#recency_from_val",
        "to_val"    : "#recency_to_val"
    };
    $RecencyInfo = getRFWInfo($recency_id);
    // console.log($RecencyInfo);

    $frequency_id = {
        "name"      : "#frequency",
        "from"      : "#frequency_from",
        "to"        : "#frequency_to",
        "from_val"  : "#frequency_from_val",
        "to_val"    : "#frequency_to_val"
    };
    $FrequencyInfo = getRFWInfo($frequency_id);
    // console.log($FrequencyInfo);

    $monetary_id = {
        "name"      : "#monetary",
        "from"      : "#monetary_from",
        "to"        : "#monetary_to",
        "from_val"  : "#monetary_from_val",
        "to_val"    : "#monetary_to_val"
    };
    $MonetaryInfo = getRFWInfo($monetary_id);
    // console.log($MonetaryInfo);

    $OutputFields = getOutputFields();
    // console.log($OutputFields);

    $validateCampaignInfo = getValidateCampaignInfo($CampaignInfo);
    $validateProductInfo = getValidateProductInfo($ProductInfo);
    $validatePurchaseDateInfo = getValidatePurchaseDateInfo($PurchaseDateInfo);
    $validateWarrantyInfo = getValidateWarrantyInfo($WarrantyInfo);
    $validateRecencyInfo = getValidateRecencyInfo($RecencyInfo);
    $validateFrequencyInfo = getValidateFrequencyInfo($FrequencyInfo);
    $validateMonetaryInfo = getValidateMonetaryInfo($MonetaryInfo);
    $validateOutputFields = getValidateOutputFields($OutputFields);

    if($validateCampaignInfo==false || $validateProductInfo==false)
        return;
    if($validatePurchaseDateInfo==false || $validateWarrantyInfo==false)
        return;
    if($validateRecencyInfo==false || $validateFrequencyInfo==false)
        return;
    if($validateMonetaryInfo==false || $validateOutputFields==false)
        return;
    console.log("Preparing request");

    $.ajax({
        type: "POST",
        url:  "/test/",
        data:{
            csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val(),
            CampaignInfo        : {$CampaignInfo},
            ProductInfo         : {$ProductInfo},
            PurchaseDateInfo    : {$PurchaseDateInfo},
            WarrantyInfo        : {$WarrantyInfo},
            RecencyInfo         : {$RecencyInfo},
            FrequencyInfo       : {$FrequencyInfo},
            MonetaryInfo        : {$MonetaryInfo},
            OutputFields        : {$OutputFields}
        },

        success: function(data){
            $(".modal").addClass("open");
            $(".backdrop").addClass("open");
            console.log("Request Sent");
            console.log(data);
        }
    });
})