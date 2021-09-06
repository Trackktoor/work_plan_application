# Work Plan V1.0 TEST WORK
## **ОПИСАНИЕ МЕТОДОВ**
## Стандартная запросов проекта в Schema.py


## экземпляр ObjectType - WorkForQuery
```json5
    title_work - String
    work_plan_id - Int
    date_start - DateTime
    date_end - DateTime
    work_id - ID
```

## экземпляр ObjectType - WorkPlanQuery
```json5
    id - ID
    title - String
    version - Int
```

---
## **РУТЫ ДЛЯ ЗАПРОСОВ** *EntryPoint: http://query*
## **Получение всех работ для плана работ**


### Обязательные аргументы 

- `work_plan_id` - ID проекты для которого нужно получить работы


### Пример запроса 

```GraphQL
{
    all_works(work_plan_id: 3) {
        title_work
    }
}
```

### Пример ответа

```GraphQL
{
  "data": {
    "all_works": [
      {
        "title_work": "Материалы"
      },
      {
        "title_work": "Материалы_4"
      },
      {
        "title_work": "Материалы_5"
      },
      {
        "title_work": "Материалы_3"
      }
    ]
  }
}
```


## **Создание работы для определённого плана**

### Обязательные аргументы 

- `title_work`- String
- `date_start` - String(datetime)
- `date_end` - String(datetime)
- `work_plan_id` - ID

### Пример запроса
```GraphQL
    {
        create_work(title_work: 5, date_start: "2021-01-10T21:33:15.233Z", date_end:"2021-01-10T21:33:15.233Z", work_plan_id:4){
        title_work
        }
    }
```

### Пример ответа

```GraphQL
{
    "data": {
        "create_work": {
            "title_work": "Work"
        }
    }
}   
```


## **Удаление работы из определённого плана работ**

### Пример запроса

```GraphQL
    {
        delete_work(work_plan_id: ID, id(работы): ID){
            title
        }
    }
```


### Пример ответа

```GraphQL
{
  "data": {
    "all_works": [
      {
        "title_work": "Материалы"
      }
    ]
  }
}
```

## **Изменение работы в плане работ**

### Обазятельные аргументы
 - id (работы для изменения)
 - work_plan_id
### Пример запроса
```GraphQL
{
    change_work(work_plan_id: 12, id: 16, change:"date_start=2021-08-30 13:12:00'"){
        title
    }
}
```
### Пример ответа
```GraphQL
{
  "data": {
    "change_work": {
      "title": "<built-in method title of str object at 0x000001EE06829C70>"
    }
  }
}
```


## **Удаление работы из определённого плана работ**

### Обязательные параметры 

- `id` - ID работы
- `work_plan_id` - ID плана работ

### Пример запроса 

```GraphQL
{
    delete_work(work_plan_id: 13, id:12){
   		title
    }
}
```

### Пример ответа

```GraphQL
{
  "data": {
    "delete_work": {
      "title": null
    }
  }
}
```

## **Получение всех версий плана работ**

### Обязательные параметры 

- `work_plan_title` - названия проекта для получения всех версий

## Пример запроса 

```GraphQL
{
    all_versions_for_work_plan(work_plan_title: "Завод"){
   		title
    }
}
```

## Пример ответа

```GraphQL
{
  "data": {
    "all_versions_for_work_plan": [
      {
        "title": "Завод"
      },
      {
        "title": "Завод"
      },
      {
        "title": "Завод"
      }
    ]
  }
```