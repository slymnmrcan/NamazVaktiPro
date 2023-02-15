
import http.client

api_token ="apikey 64TfWWbR2Ax6d8xy1ug97Q:50F0I7e7RK2c9AUg94BvUE"
conn = http.client.HTTPSConnection("api.collectapi.com")
vakit=["%C4%B0msak","%C3%96%C4%9Fle","Ak%C5%9Fam","%C4%B0kindi","Yats%C4%B1"]

headers = {
    'content-type': "application/json",
    'authorization': api_token
    }

try:
    conn.request("GET", f'/pray/single?ezan={vakit[1]}&data.city=istanbul', headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    print(type(data))
    print(data)
    
except:
    print("bir sorun oluştu")
