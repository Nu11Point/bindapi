# -*- coding: utf-8 -*-
# author: kiven

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zkapi.settings")

application = get_wsgi_application()
