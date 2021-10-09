import requests

url = 'http://localhost:4000/'

mybody = {
    'n1': 4,
    'n2': 3,
}

y = requests.get(url+'nombre')
x = requests.post(url+'suma', json=mybody)

print(y.text)
print(x.text)