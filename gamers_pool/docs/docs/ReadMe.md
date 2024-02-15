## Задание:
Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной
MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность
- зарегистрироваться в нём по e-mail,
- получив письмо с кодом подтверждения регистрации.
После регистрации им становится доступно
- создание и редактирование объявлений.
Объявления состоят из:
    - заголовка и
    - текста, внутри которого могут быть картинки, встроенные видео и другой контент.

Кроме того, пользователь обязательно должен определить объявление в одну из
следующих категорий:
Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Пользователи могут отправлять
- отклики на объявления других пользователей, состоящие из простого текста.

При отправке отклика пользователь должен
- получить e-mail с оповещением о нём.

Также пользователю должна быть доступна
- приватная страница с откликами на его объявления,
    внутри которой он может
        - фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик,
        - также должно прийти уведомление).

Также мы бы хотели иметь возможность отправлять пользователям
- новостные рассылки.
--------------------------------------------------------------------------
[Создадим документацию проекта:](https://www.mkdocs.org/user-guide/configuration/)

Create a new project 'mkdocs.docs':
[Read docs >>>](https://www.mkdocs.org/user-guide/writing-your-docs/)

Создадим новое приложение в папке проекта

`mkdocs new docs`

и перейдем в нее

`cd docs`

Build the documentation site:

`mkdocs build`

Start the live-reloading docs server:

`mkdocs serve`

---
ICONS [from](https://fontawesome.com/search?q=logout&o=r)

    python manage.py makemigrations
    python manage.py migrate

## Переводы

Для того чтобы создать файл перевода на какой-либо язык (в папке locale), надо ввести следующую команду в 
терминале в папке с manage.py файлом:

    python manage.py makemessages -l en
Скомпилируем перевод. Для чего нам надо выполнить следующую команду:

    python manage.py compilemessages

Поскольку у нас уже были записи в базе данных, надо будет ввести команду

    python manage.py update_translation_fields
Везде вставить

    from django.utils.translation import gettext as _

Для обновления переводов в 

    django.popython manage.py makemessages -l en
и скомпилировать

    python manage.py compilemessages

-------------------------------------------------------------
    {% load i18n %}
    <form action="{% url 'set_language' %}" method="POST"> {% csrf_token %} <!-- Не забываем по csrf_token для POST запросов -->
        <input type="hidden" name="next" value="{{ redirect_to }}"></form>

        <select name="language" id="">
        {% get_available_languages as LANGUAGES %} <!-- получаем языки -->
        {% get_language_info_list for LANGUAGES as languages %} <!-- Помещаем их в список languages -->

        {% for language in languages %} <!-- Итерируясь по списку, выводим их название на языке пользователя и код -->
            <option value="{{ language.code }}" {% if language.code == LANGUAGE_CODE %} selected {% endif %}>
                {{ language.name_local }} - {{ language.code }}
            </option>
        {% endfor %}
    </select>
    <input type="submit" value="set">
-------------------------------------------------------------
## For Celery & Redis

* Worker — это часть системы, которая отправляет задачи из очереди на исполнение.
Все задачи принято хранить в файлах с названием tasks.py. В таком случае Celery сможет самостоятельно 
находить задачи. Любая задача представляет собой обычную функцию с одной особенностью: 
она должна быть обернута в декоратор.

----

* Celery - разблокирует рабочий процесс для Django. Это означает, что вы можете разгрузить задачи из основного цикла
запросов/ответов внутри Django.

--- 

* Redis — это хранилище данных и брокер сообщений между Celery и Django. Другими словами, Django и Celery используют
Redis для взаимодействия друг с другом (вместо базы данных SQL)

Все трое работают вместе, создавая асинхронное волшебство. Вот несколько отличных вариантов использования Django + Celery:

Разгрузка любых долгосрочных задач
Отправка электронных писем и/или уведомлений по электронной почте
Создание отчетов, создание которых занимает более 3 секунд.
Запуск обучения и/или вывода машинного обучения
Запуск определенных функций по расписанию
Резервное копирование базы данных
Включение/выключение дополнительных виртуальных машин для обработки нагрузки.
Запуск рабочих процессов и/или отправка уведомлений веб-перехватчика
----------------------------------------------------------

1. Запустить сервер:
`(venv) PS C:\MMORPG_v2\gamers_pool\> python manage.py runserver`

2. Запустить Redis
`C:\Program Files\Redis\redis-server.exe`

3. Запустить Celery:
`C:\MMORPG_v2\gamers_pool\
(venv) PS C:\MMORPG_v2\gamers_pool\> celery -A gamers_pool worker -l INFO --pool=solo`

4. Запустить Beat:
`(venv) PS C:\MMORPG_v2\gamers_pool\> Celery -A gamers_pool beat -l INFO`
---
#Работа в [картинками](https://mob25.com/django-dobavlenie-kartinok-k-postam/) 

[документация к sorl-thumbnail](https://github.com/jazzband/sorl-thumbnail)

    `pip install pillow`
    `pip install sorl-thumbnail`

Добавьте приложение в список INSTALLED_APPS, в конец списка:

    PYTHONINSTALLED_APPS = [
        # ...
        'sorl.thumbnail',
    ]

Выполните миграцию
Теперь вам станут доступны специальные теги в шаблонах:

    <!-- Загрузка тегов библиотеки в шаблон -->
    {% load thumbnail %}

    <!-- Пример использования тега для пропорционального уменьшения и обрезки -->
    <!-- картинки до размера 100x100px с центрированием -->
    {% thumbnail item.image "100x100" crop="center" as im %}
      <img src="{{ im.url }}" width="{{ im.width }}" height="{{ im.height }}">
    {% endthumbnail %}

## Настройки проекта
Добавим в модель Post новое поле, чтобы к посту можно было добавить заглавную картинку:

    class Post(models.Model):
        ...
            # Поле для картинки (необязательное) 
        image = models.ImageField(
            'Картинка',
            upload_to='posts/',
            blank=True
        )  
        # Аргумент upload_to указывает директорию, 
        # в которую будут загружаться пользовательские файлы. 
    
        class Meta:
            ordering = ('-pub_date',)
            verbose_name = 'Пост'
            verbose_name_plural = 'Посты'
    
        def __str__(self):
            return self.text[:15]

