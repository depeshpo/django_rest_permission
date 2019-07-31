import os
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_permission.settings')

import django

django.setup()
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


GROUPS = ['admin', 'anonymous']
MODELS = ['user']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
