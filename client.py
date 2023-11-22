import requests
'''создает запись в бд'''
response = requests.post('http://127.0.0.1:5000/advertisement',
                        json ={'name':'advertisement1', 'main_text':'The main text'}
                        )

# ___________________________________________________________________________________________
'''возвращает информацию по id'''
# response = requests.get('http://127.0.0.1:5000/advertisement/1')
# AttributeError: type object 'Advertisement' has no attribute 'get'
# #____________________________________________________________________________________________
'''обновляю информацию'''
# response = requests.patch('http://127.0.0.1:5000/advertisement/2',
#                         json ={'name':'advertisement122', 'main_text':'The main text of the middle earth'}
#                         )
#не смотря на ошибку, в бд информация обновлена: NameError: name 'advertisement' is not defined
# _____________________________________________________________________________________________
'''удаляю информацию'''
# response = requests.delete('http://127.0.0.1:5000/advertisement/2')


print(response.status_code)
print(response.text)