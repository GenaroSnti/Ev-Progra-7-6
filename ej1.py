import requests, json
print('Ingrese cauntos posts necesita entre 1 y 100')
number = int(input())  
index = 1
posts = []
if number > 100:
    print('Número invalido')
while index <= number:
    url = f'https://jsonplaceholder.typicode.com/posts/{index}'
    response = requests.get(url)
    data = response.json()
    posts.append(data)
    index += 1
print(posts)
with open('dl.json', 'w') as f:
    json.dump(posts, f, indent=2)
