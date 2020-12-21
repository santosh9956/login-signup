 
import json
import getpass
from pprint import pprint

a=open("login.json","r+")
dic_list=json.load(a)

print("welcome to YOUR DETAILS.COM \n")
# print()
login_signup=int(input("press 1 for signup and 2 for login"))
if login_signup==2:
	email=input("enter your email id :- ")
	password=getpass.getpass()
	hai=False
	for i in dic_list:
		if email in i.keys():
			hai=True
			if password==i[email]:
				print("Thanks for login")
				print()
				if i["data"]!=[]:
					for j in i["data"][0]:
						print(j,":",i["data"][0][j])
				else:
					print("There is no data on this profile")
			else:
				print("you have entered a wrong password")
	if hai==False:
		print("This email doesn't exist")
		
elif login_signup==1:
	import signup