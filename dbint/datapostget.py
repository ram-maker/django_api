# import imp
import json
URL="http://127.0.0.1:8000/api/studentapi/"
import requests
# name=[]
# name1={'name':'ram','roll':5,'city':'Kansas'}
# name2={"name":"krishna","roll":10,"city":"Newyork"}
# dic_data={'employee':"{'name':'ram','roll':5,'city':'Kansas'},{'name':'krishna','roll':10,'city':'Newyork'}"}
# print(name1)
# c=json.dumps(name1)
# print(c)
# r=requests.post(url=URL,data=c,headers={'Content-type': 'application/json'})
r=requests.get(url=URL)
json_data=r.json()
# dict_data=json.loads(json_data)
print(json_data)