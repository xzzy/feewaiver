import django.dispatch

# name_changed = django.dispatch.Signal(providing_args=['user'])
# post_clean = django.dispatch.Signal(providing_args=['instance'])
name_changed = django.dispatch.Signal()
post_clean = django.dispatch.Signal()
