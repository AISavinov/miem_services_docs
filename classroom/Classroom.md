#Google Classroom

##Описание взаимодействия
- Работа с google classroom происходит через API. 
- Отправка запросов происходит с помощью node.js. 
- HTTP Server слушает GET запрос от гитлаба и читает query параметры, откуда забирает всю необходимую информацию для взаимодействия со студентом. 
- При получении стороннего запроса все данные передаются классу, который делает асинхронные запросы к API для выставления оценки.

##Авторизация
- сredentials, сконфигурованные на https://developers.google.com/classroom/ активирует Classroom API.
- чтение credentials из файла и отправка их с запросом на авторизацию для контрольной консоли разработчика.
- получение OAuth2 токена, который необходимо передавать при каждом запросе в Google API.