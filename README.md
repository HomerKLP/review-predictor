# review-predictor

## Инструкция по запуску:

- Клонируем проект

```
git@github.com:HomerKLP/review-predictor.git
```

- Копируем **example.env**, переименовываем в **.env**

```
cp example.env .env
```

- Билдим **docker-compose**

```
docker-compose up --build --detach
```

## API

### Предсказываем рейтинг отзыва

`POST http://127.0.0.1:8000/api/reviews/`

**Payload:**

```json
{
    "text": "Мне все понравилось, спасибо!"
}
```

**Response:**

```json
{
    "id": 1,
    "text": "Мне все понравилось, спасибо!",
    "rating": 5,
    "created_at": "2020-09-20T06:35:30.992561Z"
}
```

### Список всех отзывов

`GET http://127.0.0.1:8000/api/reviews/`

**Response:**

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "text": "Мне все понравилось, спасибо!",
            "rating": 5,
            "created_at": "2020-09-20T06:35:30.992561Z"
        }
    ]
}
```