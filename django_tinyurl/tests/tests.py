from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
from django_tinyurl import utils


class TinyUrlRedirecViewTest(TestCase):
    def test_valid_token(self):
        dest_url = reverse('dummy')
        token = utils.sign(dest_url)
        url = reverse('tinyurl', kwargs={'token': token})

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, dest_url)

    def test_valid_token_with_query(self):
        dest_url = reverse('dummy') + '?foo=bar'
        token = utils.sign(dest_url)
        url = reverse('tinyurl', kwargs={'token': token})

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, dest_url)

    def test_invalid_token(self):
        url = reverse('tinyurl', kwargs={'token': 'foo'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 410)

    @patch('django_tinyurl.signals.failed_redirect.send')
    @patch('django_tinyurl.signals.post_redirect.send')
    @patch('django_tinyurl.signals.pre_redirect.send')
    def test_valid_signals(self, mock_pre, mock_post, mock_failed):
        dest_url = reverse('dummy')
        token = utils.sign(dest_url)
        url = reverse('tinyurl', kwargs={'token': token})

        self.client.get(url)
        self.assertTrue(mock_pre.called)
        self.assertTrue(mock_post.called)
        self.assertFalse(mock_failed.called)

    @patch('django_tinyurl.signals.failed_redirect.send')
    @patch('django_tinyurl.signals.post_redirect.send')
    @patch('django_tinyurl.signals.pre_redirect.send')
    def test_invalid_signals(self, mock_pre, mock_post, mock_failed):
        url = reverse('tinyurl', kwargs={'token': 'foo'})
        self.client.get(url)
        self.assertTrue(mock_pre.called)
        self.assertFalse(mock_post.called)
        self.assertTrue(mock_failed.called)
