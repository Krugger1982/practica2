import requests


response =requests.post('http://httpbin.org/post', data = {'UserId':'12345', 'Status':'On'})
print('response.status_code = ', response.status_code)
