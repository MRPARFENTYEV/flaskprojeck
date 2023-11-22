import requests
"""создает запись в бд"""
# response = requests.post('http://127.0.0.1:5000/advertisement',
#                         json ={'name':'advertisement1', 'main_text':'The main text'}
#                         )

# ___________________________________________________________________________________________
response = requests.get('http://127.0.0.1:5000/advertisement/1')
# AttributeError: type object 'Advertisement' has no attribute 'get'
#____________________________________________________________________________________________

# response = requests.patch('http://127.0.0.1:5000/advertisement/2',
#                         json ={'name':'advertisement1', 'main_text':'The main text'}
#                         )
#AttributeError: 'function' object has no attribute 'json'
# _____________________________________________________________________________________________
print(response.status_code)
print(response.text)