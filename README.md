# Домашние работы по фреймворкам Flask и FastAPI (реализация на языке Python) площадка GeekBrains

<summary>Цели на репозиторий:</summary>
<p>

✔️ Выполнить домашнюю работу 1 семинара
  
✔️ Выполнить домашнюю работу 2 семинара

✔️ Выполнить домашнюю работу 3 семинара
  
✔️ Выполнить домашнюю работу 4 семинара

✔️ Выполнить домашнюю работу 5 семинара

✕ Выполнить домашнюю работу 6 семинара

</p>

<br>
<br>
↓ Домашние работы по семинарам с заданиями:

<details><summary><h4>Семинар 1. Знакомство с Flask.</h4></summary>

✔️ Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

</details>

<details><summary><h4>Семинар 2. Погружение во Flask</h4></summary>

✔️ Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

</details>

<details><summary><h4>Семинар 3. Дополнительные возможности Flask</h4></summary>

✔️ Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

</details>

<details><summary><h4>Семинар 4. Введение в многозадачность</h4></summary>

✔️ Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
  
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg

✔️ Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.

✕ Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.

✔️ Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

</details>

<details><summary><h4>Семинар 5. Знакомство с FastAPI</h4></summary>

✔️ Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:

* GET /tasks — возвращает список всех задач.

* GET /tasks/{id} — возвращает задачу с указанным идентификатором.

* POST /tasks — добавляет новую задачу.

* PUT /tasks/{id} — обновляет задачу с указанным идентификатором.

* DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.

</details>
