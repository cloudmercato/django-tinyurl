Django-TinyURL
~~~~~~~~~~~~~~

Small view fro shorten URL to other views and redirect to it.


Get started
===========

1. Redirect clients
-------------------

In your ``urls.py`` add the following ``path``:::

    from django_tinyurl.views import TinyUrlRedirecView

    urlpatterns = [
        ...
        path('<str:token>', TinyUrlRedirecView.as_view(), name="tinyurl"),
        ...
    ]

This view will redirect clients coming with a valid shorten URL (token).

2. Create short URLs
--------------------

The app contains the utilities to shorten and lengthen URLs::

    from django.urls import reverse
    from django_tinyurl import utils

    dest_url = "/foo?bar=ham"
    url_token = utils.sign(dest_url)
    short_url = reverse('tinyurl', kwargs={'token': url_token})

    url_token = utils.unsign(url_token)

Under the hood, the Django's signing system is used and can be configured
with the setting ``TINYURL_SIGNER_KWARGS`` in ``settings.py``

Contribute
----------

This project is created with ❤️ for free by `Cloud Mercato`_ under BSD License. Feel free to contribute by submitting a pull request or an issue.

.. _`Cloud Mercato`: https://www.cloud-mercato.com/
