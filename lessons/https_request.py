import requests
from pprint import pprint

params={'userId':1}
# response = requests.get(
#     'https://jsonplaceholder.typicode.com/posts',
#     params=params,
#     headers={'User-Agent': 'googlebot',
#              'Authorization': f'Bearer{token} '}
# )
#
# print(response.status_code)
# print(response.headers)
# pprint(response.json())

# ----

# new_post = {
#     'title':'new title',
#     'body':'new body',
#     'userId':1
# }
#
# response = requests.post('https://httpbin.org/post', json=new_post,timeout=5)
# print(response.status_code)
# pprint(response.json())
#
# with open('linear.png','rb') as image_file:
#     response = requests.post('https://httpbin.org/post', files={'file':image_file}))
#

update_post = {
    'title':'title',
    'body':'updated body',
    'userId':1,
    'id':101

}

# response= requests.put('https://jsonplaceholder.typicode.com/posts/1',json= update_post)
# response= requests.patch('https://jsonplaceholder.typicode.com/posts/1',json= update_post)
response= requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)
pprint(response.json())

#crud- create,read,update,delete