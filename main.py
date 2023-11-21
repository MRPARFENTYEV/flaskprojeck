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
from flask import jsonify
from flask.views import MethodView
from models import Advertisement, Session

app = flask.Flask('app')


# def hello_world():
#     return jsonify({'print':'Hello,World!'})
# app.add_url_rule('/hello_world',view_func=hello_world, methods=['GET'])
# app.run()
# advertisement
class AdvertisementView(MethodView):
    def get(self, advertisement_id: int):
        pass

    def post(self):  # создание статьи, которой еще нет
        receiving_data = request.json
        with Session() as session:
            new_advertisement =Advertisement(**receiving_data)
            session.add(new_advertisement)
            session.commit()
            return jsonify({'id':new_advertisement.id})

    def patch(self, advertisement_id: int):
        pass

    def delete(self, advertisement_id: int):
        pass


advertisement_view = AdvertisementView.as_view('advertisement_view')
app.add_url_rule('/advertisement/<int:advertisement_id>', view_func=advertisement_view, methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/advertisement', view_func=advertisement_view, methods=['GET', 'PATCH', 'DELETE'])

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
