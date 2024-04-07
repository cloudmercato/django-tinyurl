from django.core import signing
from django_tinyurl import settings


class InvalidShortPath(Exception):
    pass


signer = signing.Signer(**settings.SIGNER_KWARGS)


def sign(value):
    return signer.sign_object(value)


def unsign(value):
    try:
        return signer.unsign_object(value)
    except signing.BadSignature:
        msg = f"Unknown short path '{value}'"
        raise InvalidShortPath(msg)
