from django.conf import settings

DEFAULT_SIGNER_KWARGS = {
    'key': settings.SECRET_KEY,
}
SIGNER_KWARGS = getattr(settings, 'TINYURL_SIGNER_KWARGS', DEFAULT_SIGNER_KWARGS)
