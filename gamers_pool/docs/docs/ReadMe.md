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
### Создадим виртуальное окружение
    py -m venv venv

и заполним его из `requirements.txt`

    pip install requirements.txt    

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
#Работа с [картинками](https://mob25.com/django-dobavlenie-kartinok-k-postam/) 

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

### Подключение [комментариев](https://www.letscodemore.com/blog/how-to-create-a-comment-section-for-django-blog/) к постам ###
[GitHub](https://github.com/LetsCodeMore/Django-comment-section/blob/master/blogcomments)

установите пакет Django  [django_comments_xtd](https://django-comments-xtd.readthedocs.io/en/2.8.5/)

В этом [руководстве](https://django-comments-xtd.readthedocs.io/en/2.8.5/tutorial.html#ref-tutorial) вы узнаете, как использовать все функции django-comments-xtd

    pip install django-comments-xtd

---
        #settings.py
    
    INSTALLED_APPS = [
        '.....'
        'django.contrib.sites',
        '....'
    
        # django_comments_xtd and django_comments order should be same
        'django_comments_xtd',
        'django_comments',  
    ]

Set COMMENTS_APP = 'django_comments_xtd'

    #settings.py
    
    COMMENTS_APP = 'django_comments_xtd'

Установите   для COMMENTS_XTD_MAX_THREAD_LEVEL значение

    # settings.py
    
    # Set the COMMENTS_XTD_MAX_THREAD_LEVEL to N, being N the maximum 
    # level of threading up to which comments will be nested in your project.
    # 0: No nested comments:
    #  Comment (level 0)
    
    # 1: Nested up to level one:
    #  Comment (level 0)
    #   |-- Comment (level 1)
    
    # 2: Nested up to level two:
    #  Comment (level 0)
    #   |-- Comment (level 1)
    #        |-- Comment (level 2)
    
    COMMENTS_XTD_MAX_THREAD_LEVEL = 2

Затем добавьте следующее

    # settings.py
    
    COMMENTS_XTD_CONFIRM_EMAIL = False
    
    # Either enable sending mail messages to the console:
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
    # or smpt EmailBackend
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    
    # Or set up the EMAIL_* settings so that Django can send emails:
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = "587"
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'Your email'
    EMAIL_HOST_PASSWORD = 'Your email password'
    DEFAULT_FROM_EMAIL = "Helpdesk <helpdesk@yourdomain>"

Теперь отредактируйте модуль URL-адресов проекта, main_project/urls.py.

    from django.urls import path, include
    
    urlpatterns = [
        ...
        path('comments/', include('django_comments_xtd.urls')),
        ...
    ]

Теперь запустите миграцию python Manage.py.  И измените файл `post.html`.

1. Отобразите общее количество комментариев, оставленных к сообщению в блоге. (Выполнено этим тегом  get_comment_count  )

2. Перечислите уже опубликованные комментарии. (Выполняется этим тегом  {% render_xtdcomment_tree для объекта %}  )

3. Откройте форму комментариев, чтобы можно было отправлять комментарии. (Выполняется этим тегом  {% render_comment_form for object %}  )




1. Когда кто-то оставит комментарий к вашему сообщению в блоге, вы получите электронное письмо с комментарием.

2. Когда какой-либо пользователь оставляет комментарий и подписывается на следующий комментарий, установив флажок «Последний». Затем, когда другой пользователь отвечает на этот комментарий, он получает электронное письмо об ответном комментарии.

Как настроить шаблон электронного письма с последующими комментариями?

В папке ваших шаблонов

1. Создайте папку «django_comments_xtd».

2. Внутри этой папки создайте файл «email_followup_comment.html».

По умолчанию email_followup_comment.html содержит этот код. Вы можете добавить классы стилей (CSS) или начальной загрузки, чтобы сделать его привлекательным.

    <!-- email_followup_comment.html -->
    <!-- in case of https, replace every http with https -->
    
    {% load i18n %}<p>Hello {{ user_name }},</p>
    
    <p>{% trans 'There is a new comment following up yours.' %}</p>
    
    <p>{% trans 'Sent by' %}: {{ comment.name }}, {{ comment.submit_date|date:"SHORT_DATE_FORMAT" }}<br/>
    <a href="http://{{ site.domain }}{{ comment.content_object.get_absolute_url }}">http://{{ site.domain }}{{ comment.content_object.get_absolute_url }}</a></p>
    
    <p>{% trans 'The comment' %}:<br/>
    <i>{{ comment.comment }}</i>
    </p>
    
    <p>{% blocktrans with site_domain=site.domain mute_url_short=mute_url|slice:":40" %}Click <a href="http://{{ site_domain }}{{ mute_url }}">http://{{ site_domain }}{{ mute_url_short }}...</a> to mute the comments thread. You will no longer receive follow-up notifications.{% endblocktrans %}</p>
    <p>--<br/>
    {% trans 'Kind regards' %},<br/>
    {{ site }}
    </p>

## Настройка электронной почты для [разработки](https://docs.djangoproject.com/en/5.0/topics/email/#topic-email-backends)

Бывают случаи, когда вы вообще не хотите, чтобы Django отправлял электронные письма. Например, при разработке веб-сайта вы, вероятно, не захотите рассылать тысячи электронных писем, но вы можете захотеть убедиться, что электронные письма будут отправлены нужным людям в правильных условиях и что эти электронные письма будут содержать правильный контент.
Самый простой способ настроить электронную почту для локальной разработки — использовать серверную часть консоли электронной почты. Этот серверный механизм перенаправляет всю электронную почту на адрес stdout, позволяя вам проверять ее содержимое.
Серверная часть файловой электронной почты также может быть полезна во время разработки — эта серверная часть сохраняет содержимое каждого SMTP-соединения в файл, который можно проверить на досуге .
Другой подход — использовать «тупой» SMTP-сервер, который получает электронные письма локально и отображает их на терминале, но фактически ничего не отправляет. Пакет aiosmtpd предоставляет способ сделать это:

    python -m pip install aiosmtpd
    python -m aiosmtpd -n -l localhost:8025

Эта команда запустит минимальный SMTP-сервер, прослушивающий порт 8025 локального хоста. Этот сервер выводит в стандартный вывод все заголовки и тело электронного письма. Затем вам нужно только установить EMAIL_HOSTи EMAIL_PORTсоответственно. Более подробное описание параметров SMTP-сервера см. в документации модуля aiosmtpd .