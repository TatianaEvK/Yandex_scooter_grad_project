import sender_stand_request
import requests


#Тест на проверку получения кода 200:
def test_get_order():
    order_body = sender_stand_request.get_order_body()
    order_res = sender_stand_request.post_new_order(order_body)
    assert order_res.status_code == 200
