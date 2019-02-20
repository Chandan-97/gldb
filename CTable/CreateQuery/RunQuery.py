import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd="helloworld", db='gl')
cur = conn.cursor()
cur.execute("SELECT * FROM rw_service_mst")
for response in cur:
    print(response)
cur.close()
conn.close()