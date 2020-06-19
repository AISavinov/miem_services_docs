# Gitlab
### Контракт:
- созданный проект прикрепляется к каждому студенту
- содержит course_id, task_id, user_id, grader_location, max_retries в в переменных окружения
- содержит заготовленные файлы для отправки
### Описание необходимых для работы пайплайна полей:
- course_id - id курса в classroom
- task_id - id задания
- cretor_token - токен создавшего курс
- grader_location - url для отправки готовых задний (url грейдера)
- max_retries - количество возможных попыток
- expiration_date - дедлайн задания
- student_email - email студента
