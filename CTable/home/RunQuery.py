import pymysql
import csv
import datetime

from django.conf import settings
import os

def runQuery(request, query, camp_name):
    print("query : ", query)
    print("==============")
    query = "select * from rw_service_mst"
    conn = pymysql.connect(host='localhost', user='root', passwd="helloworld", db='gl')
    cur = conn.cursor()
    try:
        cur.execute(query)
        # for response in cur:
            # print(response)

        cur.close()
        conn.close()
        res = []
        now = datetime.datetime.now()
        file_loc = str(request.user)+"/"+camp_name+str(now)+".csv"

        # download link
        dlink = "/media/" + file_loc

        folder_loc = str(request.user)
        file_loc = os.path.join(settings.MEDIA_ROOT, file_loc)
        folder_loc = os.path.join(settings.MEDIA_ROOT, folder_loc)
        print("file_loc : ", file_loc)
        print("folder_loc : ", folder_loc)
        if not os.path.exists(folder_loc):
            os.makedirs(folder_loc)
        with open(file_loc, "w") as op:
            writer = csv.writer(op, lineterminator="\n")
            q = []
            q.append(query)
            writer.writerow(q)
            num_fields = len(cur.description)
            field_names = [i[0] for i in cur.description]
            writer.writerow(field_names)
            writer.writerows(cur)


        res.append(True)
        res.append(file_loc)

        res.append(dlink)

        return res;

    except Exception as e:
        print("Exception : ", e)
        res = []
        res.append(False)
        return res

