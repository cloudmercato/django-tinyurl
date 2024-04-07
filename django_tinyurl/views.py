from django.views.generic import RedirectView
from django_tinyurl import utils
from django_tinyurl import signals


class TinyUrlRedirecView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        signals.pre_redirect.send(
            sender=self.__class__,
            token=self.kwargs['token'],
        )
        try:
            url = utils.unsign(self.kwargs['token'])
        except utils.InvalidShortPath as err:
            signals.failed_redirect.send(
                sender=self.__class__,
                token=self.kwargs['token'],
                error=err,
            )
            return

        signals.post_redirect.send(
            sender=self.__class__,
            token=self.kwargs['token'],
            url=url,
        )
        return url
