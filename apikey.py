import requests

headers = {
    'content-type': "application/json",
    'authorization': "apikey 64TfWWbR2Ax6d8xy1ug97Q:50F0I7e7RK2c9AUg94BvUE"
    }

url = "https://api.collectapi.com/pray/single?ezan=%C4%B0kindi&data.city=konya"
try:
    response = requests.get(url, headers=headers)
    data= response.json()
except:
    print("bir sorun oluştu")
print(data)
if data['success']:
    print(data['result'][0]['time'])
    print(data['result'][0]['remainingTime'])