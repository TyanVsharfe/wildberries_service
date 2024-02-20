# Сервис на FastAPI для работы с товарами https://www.wildberries.ru

## Установка
Склонируйте репозиторий
```shell
git clone https://github.com/TyanVsharfe/wildberries_service.git
```
Создайте в корне проекта файл .env в котором укажите следующие поля:
```
BOT_TOKEN=<токен вашего телеграмм бота>
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=wb_db
DB_NAME=wb_db
API_SERVER=http://127.0.0.1:8000
API_DOCKER_NAME=wb_web_service
```
Чтобы создать и запустить контейнеры в docker введите следующую команду:
```shell
docker compose up -d
```

## Использование
### API
В данном проекте разработан Restful API веб-сервис. Доступ к swagger docs можно получить по адресу http://127.0.0.1:8000/docs. 
### Визуализация
Визуализация данных в виде графиков реализована через библиотеку plotly
### Telegram bot
Взаимодействие с API реализовано через команды в боте.
#### Список команд:
```
!get_product <id> - Получить продукт из базы данных по его id
!add_product <id> - Добавить продукт в базу данных по его id
!delete_product <id> - Удалить продукт из базы данных по его id
!update_product <id> - Получить актуальные данные и обновить продукт из базы данных по его id
!get_all - Получить список всех продуктов из базы данных (в telegram кол-во символов в сообщении ограничено, поэтому выдается файл с данными и первые 5 записей из бд)
!product_history <id> - Получить график цены за все время существования продукта по его id
!product_category_history <id> - Получить график цен за все время существования продуктов одной категории с категорией продукта с указанным id из базы данных
!product_count - Количество записей в базе данных
!product_categories_count - Количество записей в базе данных у каждой категории
!product_min-max <id> - Минимальная и максимальная цена товара за последние 6 месяцев
```

## Примеры
### Работа команд
![2024-02-19_17-20-00](https://github.com/TyanVsharfe/wildberries_service/assets/105783276/0b8cdae1-a2f1-4664-a6e8-3b2ee91bf1c4)
![image](https://github.com/TyanVsharfe/wildberries_service/assets/105783276/4794cd59-ea65-4c5b-bb47-4ea234e1372b)
![image](https://github.com/TyanVsharfe/wildberries_service/assets/105783276/87c57005-adbb-4af2-a923-9480afba5eeb)
### Графики
![coffee](https://github.com/TyanVsharfe/wildberries_service/assets/105783276/e13ff4b3-8c60-4615-8eab-60286ae0af49)
![vacuum_cleaner](https://github.com/TyanVsharfe/wildberries_service/assets/105783276/26e58c0d-85a6-4f07-8fef-2160a0790c22)
