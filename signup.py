 
import json

import getpass


l=open("login.json","r")
dic_list=json.load(l)
# print(type(dic_list))

full_data={}
user_data={}
data=[]
t=True
while True:
	email=input("enter a email id")
	for i in dic_list:
		if email in i.keys():
			t=True
			break
		else:
			t=False
	if t==False:
		password=getpass.getpass(prompt="enter your password:-")
		full_data[email]=password
		a=int(input("press 1 for entering details and 2 for not"))
		if a==1:
			n=input("enter your Name")
			p=input("enter your place")
			age=input("enter your age")
			user_data["Name"]=n
			user_data["place"]=p
			user_data['age']=age
			break
		else:
			data=[]
			break
	elif t==True:
		print("this email already exists")
l.close()
k=open("login.json","w+")
data.append(user_data)
full_data["data"]=data
dic_list.append(full_data)
json.dump(dic_list,k,indent=4)