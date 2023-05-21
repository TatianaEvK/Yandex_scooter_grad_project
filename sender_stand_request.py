import configuration
import requests
import data

#Запрос на создание заказа.
def post_new_order(order_body):
    order_body = data.order_body
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=order_body)

# Сохранение номера трека заказа.
def get_new_track():
    order_body = data.order_body.copy()
    res = post_new_order(order_body)
    t = res.json()["track"]
    return t



# Запрос на получения заказа по треку.

def get_order_body():
    current_order_body = data.order_body.copy()
    current_order_body["t"] = 't'
    return  current_order_body









