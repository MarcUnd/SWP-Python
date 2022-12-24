# importing the requests library
import requests
  
# api-endpoint
URL = "http://127.0.0.1:5000/"
  
  
'''  
# sending get request and saving the response as response object
r = requests.post(url = URL + 'hans')

# extracting data in json format
data = r.json()


print(data)

r = requests.get(url = URL + 'a')

# extracting data in json format
data = r.json()


print(data)

r = requests.delete(url = URL + 'hans')

# extracting data in json format
data = r.json()


print(data)


r = requests.get(url = URL+'update', params={'name':'marc', 'win':1, 'choice': 4})

# extracting data in json format
data = r.json()


print(data)
'''

r = requests.get(url = URL+'ai-choice/marc')
# extracting data in json format
data = int(r.json())


print("<Response [200]>" == str(r))
