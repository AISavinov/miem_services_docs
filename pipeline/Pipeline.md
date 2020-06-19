# Pipeline (aka. task_receiver)
### Принцип работы
- отправляет все файлы из репозитория по контракту описанному в grader/grader_client
- получает оценку и вопросы с ответами для дальнейшей отправки в zulip и classroom
- после получения оценким отправляет ее в classroom_receiver
- после получения вопросы с ответами отправляет их в zulip_receiver
- линка на текущую имплементацию https://github.com/AISavinov/task_receiver/blob/master/main.py
### Контракт на отправку даннух в zulip_receiver
```json
{
    "student_email": "asavino@miem.hse.ru",
    "course_id" : "course_id", 
    "task_id" : "task_id",
    "creator_token" : "creator_token",
    "suggestive_flow": [
            {"quastion1" : "answer1"}, 
            {"quastion1" : "answer2"}
    	]
}
```
### Контракт на отправку даннух в classroom_reciever
```json
{
    "student_email": "asavino@miem.hse.ru",
    "course_id" : "course_id", 
    "task_id" : "task_id",
    "creator_token" : "creator_token",
    "mark": 2
}
