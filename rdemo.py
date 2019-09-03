import requests


#payload = {'n': 10, 'int': 5}

#basic authorization
#r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))

#Timeout to prevent infinite waiting
#r = requests.get('https://httpbin.org/delay/5', timeout=3)

#GET N random bytes with given seed
r = requests.get('https://httpbin.org/hidden-basic-auth/bob/test', auth=('bob', 'test'))

r_dict = r.json()
print(r.text)

''' write image file using wb - write bytes
with open('comic.png', 'wb') as f:
	f.write(r.content)
'''
#r_dict = r.json()
#print(r_dict['form'])