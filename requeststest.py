import requests
payload={'username':'corey','password': 'testing'}
#r = requests.get('https://httpbin.org/get',params=payload)
r = requests.post('https://httpbin.org/post',data=payload)

print(r.text)

#with open('comic.png', 'wb') as f:
  #f.write(r.content)
#print(r.ok) checks to see if message was less than 400
#print(r.headers) displays header information



