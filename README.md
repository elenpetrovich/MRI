## Структура проекта

```
└───nginx-django-mysql
    ├───dev
    │   ├───django
    │   └───nginx
    ├───django
    │   └───src
    │       ├───clinics
    │       │   ├───migrations
    │       │   ├───templates
    │       │   │   ├───clinics
    │       │   │   └───doctors
    │       │   └───__pycache__
    │       ├───domain
    │       │   ├───migrations
    │       │   └───__pycache__
    │       ├───IS
    │       │   ├───migrations
    │       │   ├───static
    │       │   │   └───IS
    │       │   ├───templates
    │       │   │   └───IS
    │       │   └───__pycache__
    │       ├───MRI_IS
    │       │   └───__pycache__
    │       ├───my_app
    │       │   └───migrations
    │       └───users
    │           ├───migrations
    │           ├───templates
    │           │   └───users
    │           └───__pycache__
    ├───env
    └───nginx
        └───conf.d
```

### Запуск
> cd nginx-django-mysql
> docker-compose up --build --force-recreate

### Просмотр в браузере
> localhost

### Полезные ссылки
<http://pawamoy.github.io/2018/02/01/docker-compose-django-postgres-nginx.html>