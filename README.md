# Домашнее задание 25_2

## !!!ВНИМАНИЕ!!! ##
### Инструкция перед запуском проекта (порядок выполнения имеет значение)
1. Перед запуском проекта переименуйте файл [env_template](env_template) в `.env` и поменяйте содержимое на свои переменные окруженния
2. Выполните миграцию `python manage.py migrate`
3. Создайте суперпользователя (имеет все права) `python manage.py create_custom_superuser`

    _Логин: admin@example.com Пароль: 0987_

4. Создайте модератора: `python manage.py create_moderator_user`

    _Логин: moderator@example.com Пароль: qweasd_

5. Создайте простого пользователя: `python manage.py create_simple_user`

    _Логин: test@example.com Пароль: 0987_

6. Заполните базу даных (курсы и уроки): `python manage.py fill_materials_data `
7. Заполните базу даных (платежи): `python manage.py fill_payment_data`

# Задание 1
Для сохранения уроков и курсов реализуйте дополнительную проверку на отсутствие в материалах ссылок 
на сторонние ресурсы, кроме youtube.com.

То есть ссылки на видео можно прикреплять в материалы, 
а ссылки на сторонние образовательные платформы или личные сайты — нельзя.

_Создайте отдельный файл `validators.py`, реализуйте валидатор, проверяющий ссылку,_ 
_которую пользователь хочет записать в поле урока с помощью класса или функции._

_Интегрируйте валидатор в сериализатор._

# Задание 2
Добавьте модель подписки на обновления курса для пользователя.

_Модель подписки должна содержать следующие поля: «пользователь» (FK на модель пользователя),_ 
_«курс» (FK на модель курса). Можете дополнительно расширить модель при необходимости._

Вам необходимо реализовать эндпоинт для установки подписки пользователя и на удаление подписки у пользователя.

При этом при выборке данных по курсу пользователю необходимо присылать признак подписки текущего пользователя на курс. 
То есть давать информацию, подписан пользователь на обновления курса или нет.

# Задание 3

Реализуйте пагинацию для вывода всех уроков и курсов.

Пагинацию реализуйте в отдельном файле `paginators.py`. Можно реализовать один или несколько классов пагинатора. 
Укажите параметры `page_size`, `page_size_query_param`, `max_page_size` для класса `PageNumberPagination`. 
Количество элементов на странице выберите самостоятельно. 
Интегрируйте пагинатор в контроллеры, используя параметр `pagination_class`.

# Задание 4

Напишите тесты, которые будут проверять корректность работы CRUD уроков
и функционал работы подписки на обновления курса.

В тестах используйте метод `setUp` для заполнения базы данных тестовыми данными. 
Обработайте возможные варианты взаимодействия с контроллерами пользователей с разными правами доступа. 
Для аутентификации пользователей используйте `self.client.force_authenticate()`. 
Документацию к этому методу можно найти 
[тут](https://www.django-rest-framework.org/api-guide/testing/#forcing-authentication).

# Дополнительное задание
Напишите тесты на все имеющиеся эндпоинты в проекте.