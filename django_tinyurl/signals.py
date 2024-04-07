from django import dispatch

pre_redirect = dispatch.Signal()
post_redirect = dispatch.Signal()
failed_redirect = dispatch.Signal()
