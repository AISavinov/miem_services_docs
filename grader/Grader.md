# Grader
 - контракт получения выполненного задания описан в grader_client
 - при создании должен выставляться timeout выполнения задания
 ### Формат ответа
```json
{"response": {
    "grade" : 5, 
    "suggestive_flow": [
        {"quastion1" : "answer1"}, 
        {"quastion1" : "answer2"}
    ]
}
```
