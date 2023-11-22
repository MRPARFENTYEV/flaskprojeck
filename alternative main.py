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
from flask import jsonify,request,Response
from flask.views import MethodView
from models import Advertisement, Session
from sqlalchemy.exc import IntegrityError

app = flask.Flask('app')


class HttpError(Exception):
    def __init__(self, status_code:int,description:str):
        self.status_code = status_code
        self.description = description

@app.errorhandler(HttpError)
def error_handler(error):
    response = jsonify({'error':error.description})
    response.status_code = error.status_code
    return response
@app.before_request
def before_request():
    session = Session()
    request.session = session
@app.after_request
def after_request(response:Response):# по моменту пробрасывания надо уточнить
    request.session.close()
    return response

def get_advertisement(advertisement_id):
    advertisement = request.session.get(Advertisement, advertisement_id)
    if advertisement is None:
        response = jsonify({'error': 'advertisement is not found'})
        response.status_code = 404
    return advertisement
def add_advertisement(advertisement:Advertisement):
    try:
        request.session.add(advertisement)
        request.session.commit()
    except IntegrityError:
        raise HttpError(409,'Advertisement is already exists')
    return advertisement

class AdvertisementView(MethodView):
    @property
    def session(self):
        return request

    '''ВОЗВРАЩАЮ ДАННЫЕ ПО ID'''
    def get(self, advertisement_id):
        advertisement = get_advertisement(advertisement_id)
        if advertisement is None:
            raise HttpError(404,'advertisement is not found')

            return response

        return jsonify({'id': advertisement.id, 'name': advertisement.name,
                        'publication time': advertisement.publicationtion_time.isoformat(),
                        'text': advertisement.main_text})

    '''СОЗДАЮ ЗАПИСИ В ТАБЛИЦЕ'''
    def post(self):  # создание статьи, которой еще нет
        receiving_data = request.json
        new_advertisement = Advertisement(**receiving_data)
        new_advertisement =add_advertisement(new_advertisement)
        return jsonify({'id': new_advertisement.id})

    def patch(self, advertisement_id: int):
        advertisement_data = request.json
        adv = get_advertisement(advertisement_id)
        for key,value in advertisement_data.items():
            setattr(adv,key,value)
        advertisement = add_advertisement(adv)
        return jsonify({'Advertisement has been changed':"status: ok"})

    def delete(self, advertisement_id: int):
        new_advertisement = get_advertisement(advertisement_id)
        self.session.delete(new_advertisement)
        self.session.commit()
        return jsonify({'deleted': 'advertisement'})



advertisement_view = AdvertisementView.as_view('advertisement_view')#преобразование класса в функцию.

app.add_url_rule('/advertisement/<int:advertisement_id>', view_func=advertisement_view, methods=['GET','PATCH','DELETE'])

app.add_url_rule('/advertisement', view_func=advertisement_view, methods=['POST'])

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
