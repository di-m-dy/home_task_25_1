# Домашнее задание 25_1

# Задание 1
Реализуйте CRUD для пользователей, в том числе регистрацию пользователей, 
настройте в проекте использование JWT-авторизации и закройте каждый эндпоинт авторизацией.

_Эндпоинты для авторизации и регистрации должны остаться доступны для неавторизованных пользователей._

# Задание 2
Заведите группу модераторов и опишите для нее права работы с любыми уроками и курсами, 
но без возможности их удалять и создавать новые. Заложите функционал такой проверки в контроллеры.

# Задание 3

Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, 
могли видеть, редактировать и удалять только свои курсы и уроки.

_Заводить группы лучше через админку и не реализовывать для этого дополнительных эндпоинтов._


# Дополнительное задание
Для профиля пользователя введите ограничения, чтобы авторизованный пользователь мог просматривать любой профиль, 
но редактировать только свой. При этом для просмотра чужого профиля должна быть доступна только общая информация, 
в которую **не входят**: пароль, фамилия, история платежей.