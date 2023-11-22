# Задание 1
#
# Вам нужно написать REST API (backend) для сайта объявлений.
#
# Должны быть реализованы методы создания/удаления/редактирования объявления.
# У объявления должны быть следующие поля:
#     заголовок
#     описание
#     дата создания
#     владелец
#
# Результатом работы является API, написанное на Flask.
#
# Этапы выполнения задания:
#
#     Сделайте роут на Flask.
#     POST метод должен создавать объявление, GET - получать объявление, DELETE - удалять объявление.
import flask
from flask import jsonify,request
from flask.views import MethodView
from models import Advertisement, Session


app = flask.Flask('app')


class AdvertisementView(MethodView):
    '''ВОЗВРАЩАЮ ДАННЫЕ ПО ID'''
    def get(self, advertisement_id):
        with Session() as session:
            advertisement = session.get(Advertisement,advertisement_id)
            return jsonify({'id': advertisement.id, 'name': advertisement.name,
                            'publication time': advertisement.publicationtion_time.isoformat(),
                            'text': advertisement.main_text})

    '''СОЗДАЮ ЗАПИСИ В ТАБЛИЦЕ'''
    def post(self):  # создание статьи, которой еще нет
        receiving_data = request.json
        with Session() as session:
            '''создание новой таблички внутри сессии'''
            new_advertisement = Advertisement(**receiving_data)
            session.add(new_advertisement)
            session.commit()
            return jsonify({'id': new_advertisement.id})

    def patch(self, advertisement_id: int):
        advertisement_data = request.json
        with Session() as session:
            adv = session.get(Advertisement, advertisement_id)
            for key,value in advertisement_data.items():
                setattr(adv,key,value)
            session.commit()
            return jsonify({'id': advertisement.id, 'name': advertisement.name, 'text': advertisement.main_text})

    def delete(self, advertisement_id: int):
        with Session() as session:
            new_advertisement = session.get(Advertisement,advertisement_id)
            session.delete(new_advertisement)
            session.commit()
            return jsonify({'deleted': 'advertisement'})



advertisement_view = AdvertisementView.as_view('advertisement_view')#преобразование класса в функцию.

app.add_url_rule('/advertisement/<int:advertisement_id>', view_func=advertisement_view, methods=['GET','PATCH','DELETE'])

app.add_url_rule('/advertisement', view_func=advertisement_view, methods=['POST'])

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
