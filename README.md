# payments_system

Сервис для приема вебхуков от банка
Работает на Django, DRF, MySQL

1. Установить зависимости из requirements.txt
2. .env в корне рядом с manage.py:
DEBUG=True
SECRET_KEY=some_key
DB_NAME=my_db
DB_USER=my_user
DB_PASSWORD=my_pass
DB_HOST=localhost
DB_PORT=3306
3. В папке с manage.py

python manage.py makemigrations
python manage.py migrate

Запуск: python manage.py runserver

Тестить:
1. POST http://127.0.0.1:8000/api/webhook/bank/ 
Формат:
{
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": 145000,
  "payer_inn": "1234567890",
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"
}

2. GET
Получаем по ИНН организацию и чекаем баланс
http://127.0.0.1:8000/api/organizations/1234567890/balance/ 


Разработчик:
Алимов Р.Ф.
