def filterCampData(req):
    print("req : ", req)
    print("************************************")
    CampInfo = req.getlist("CampaignInfo[campaign_arr][]")
    err = False
    for x in CampInfo:
        if(len(x) <= 1):
            err = True
            break
    CampInfo.append(err)
    return CampInfo
