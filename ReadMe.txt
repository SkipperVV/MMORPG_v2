Для транслятора

python manage.py makemessages -l en
python manage.py update_translation_fields
python manage.py compilemessages

В моделях
from django.utils.translation import gettext as _
....
_("Автор")

В html
{% load i18n %}
{{ string }} {%trans 'Вход'%}