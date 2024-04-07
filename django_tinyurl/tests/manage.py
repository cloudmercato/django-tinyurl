#!/usr/bin/env python
import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='ABigBigBigSecrectToKeepSecret',
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[],
    MIDDLEWARE=[],
    DATABASES={'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }},
    TEMPLATES=[],
)

django.setup()


from django.urls import path
from django.shortcuts import HttpResponse
from django_tinyurl import views


def dummy_view(request):
    return HttpResponse()


urlpatterns = [
    path('', dummy_view, name="dummy"),
    path('<str:token>', views.TinyUrlRedirecView.as_view(), name="tinyurl"),
]


if __name__ == "__main__":
    import sys
    from django.core.management import execute_from_command_line

    argv = list(sys.argv)
    execute_from_command_line(sys.argv)
