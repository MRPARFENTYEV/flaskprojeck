import aiohttp
import requests
import asyncio

'''создает запись в бд'''
# response = requests.post('http://127.0.0.1:5000/advertisement',
#                         json ={'name':'advertisementhhh6', 'main_text':'The textus_'})
#чтобы работал запрос надо менять только вторую строчку
# ___________________________________________________________________________________________
'''возвращает информацию по id'''
# response = requests.get('http://127.0.0.1:5000/advertisement/1')
# AttributeError: type object 'Advertisement' has no attribute 'get'
# #____________________________________________________________________________________________
'''обновляю информацию'''
# response = requests.patch('http://127.0.0.1:5000/advertisement/3',
#                         json ={'name':'advertisement122', 'main_text':'The main text of the middle earth'}
#                         )
#не смотря на ошибку, в бд информация обновлена: NameError: name 'advertisement' is not defined
# _____________________________________________________________________________________________
'''удаляю информацию'''
# response = requests.delete('http://127.0.0.1:5000/advertisement/2')
# print(response.status_code)
# print(response.text)
'''____________________________________________________'''
'''aiohttp'''
'''____________________________________________________'''

'''пробные запросы на ассинхранизацию'''
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.post('http://127.0.0.1:8080/hello/world') as response:
#             print(response.status)
#             print(await response.text())
# asyncio.run(main())

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://127.0.0.1:8080') as response:
#             print(response.status)
#             print(await response.text())
# asyncio.run(main())

'''запрос на создание статьи'''
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.post('http://127.0.0.1:8080/advertisement',json={'name':'advertisement1','publisher':'Stephen King','main_text':'I am the main one'}) as response:
#             print(response.status)
#             print(await response.text())
# asyncio.run(main())

'''запрос на проверку статьи'''
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://127.0.0.1:8080/advertisement/2',) as response:
#             print(response.status)
#             print(await response.text())
# asyncio.run(main())
'''Result: 200
{"id": 1, "name": "Name1", "publisher": "Publisher1", "publication time": "2023-12-05T11:04:54.315675", "main text": "The Text"}'''
'''not found запрос:
Result:
404
{"error": "Avertisement with id: 10 is not found"}
'''


'''запрос-изменение информации'''
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.patch('http://127.0.0.1:8080/advertisement/2',
                               json={'name':'IT-2','publisher':'Stephen King','main_text':'I am the main one, you see'}) as response:
            print(response.status)
            print(await response.text())
asyncio.run(main())
'''200
{"id": 2}'''

'''запрос на удаление статьи'''
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.delete('http://127.0.0.1:8080/advertisement/2') as response:
            print(response.status)
            print(await response.text())
asyncio.run(main())
'''не удаляет'''