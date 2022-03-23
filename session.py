import requests
usr=input(' Username : ')
password=input('Password : ')
url='https://www.instagram.com/accounts/login/ajax/'
h={
 'accept': '*/*',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
 'content-length': '291',
 'content-type': 'application/x-www-form-urlencoded',
 'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
 'origin': 'https://www.instagram.com',
 'referer': 'https://www.instagram.com/',
 'sec-fetch-dest': 'empty',
 'sec-fetch-mode': 'cors',
 'sec-fetch-site': 'same-origin',
 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
 'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
 'x-ig-app-id': '936619743392459',
 'x-ig-www-claim': '0',
 'x-instagram-ajax': '1cb44f68ffec',
 'x-requested-with': 'XMLHttpRequest'}
data={
 'username': usr,
 'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{password}',
 'queryParams': '{}',
 'optIntoOneTap': 'false'}
req=requests.post(url,data=data, headers=h)
if '"authenticated":true' in req.text :
 print(' Done Logged in')
 sessd=req.cookies['sessionid']
 print('Your session id is:\n',sessd)
 with open('sessionid Wx.txt', 'a') as session:
			session.write(f'{sessd}\n')
else:
 print(f"{req.text} ")
