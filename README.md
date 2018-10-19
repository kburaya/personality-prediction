# Personality Prediction REST Server

Простенький сервер для предсказания психотипа пользователя по шкале MBTI, работающий по протоколу REST.

# Работа с сервером
Перед началом работы установить библиотеки для Python:
```
pip install flask
pip install flask_restful
```
Для старта сервера запустить скрипт:

```sh
python server.py
```

После этого локальный адрес http://127.0.0.1:5000/ станет доступен для запросов.

## Пример запроса/ответа
Сервер работает только с GET запросами. Чтобы запросить психотип пользователя Instagram, необходимо выполнить следующий REST запрос:
```
GET http://127.0.0.1:5000/user/happyksuh
```

Успешный ответ вернется в следующем виде:
```
{
	"status": "OK",
	"Extraversion/Intraversion": "E",
	"Sensing/Intuition": "S",
	"Thinking/Feeling": "T",
	"Judjing/Perception": "J"
}
```
В случае ошибки ответ будет:
```
{
    "status": "ERROR"
}
```