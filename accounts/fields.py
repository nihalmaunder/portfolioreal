from __future__ import unicode_literals

from django.db import models

from accounts.conf import settings


class TimeZoneField(models.CharField):

    def __init__(self, *args, **kwargs):
        defaults = {
            "max_length": 100,
            "default": "",
            "blank": True,
        }
        defaults.update(kwargs)
        return super(TimeZoneField, self).__init__(*args, **defaults)
