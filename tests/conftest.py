from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

import pytest


@pytest.yield_fixture
def django_client(harness):
    harness.fs.project.mk(
    ('aspen_django_urls.py', '''
from aspen.shims import django as shim
from django.conf.urls import patterns

urlpatterns = patterns('', (r'^', shim.view))
'''),
    ('aspen_django_settings.py', '''
SECRET_KEY = 'cheese'
ROOT_URLCONF = 'aspen_django_urls'
DEBUG = TEMPLATE_DEBUG = True

from aspen.shims import django as shim
ASPEN_REQUEST_PROCESSOR = shim.install()
'''))

    sys.path.insert(0, harness.fs.project.root)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'aspen_django_settings'

    try:
        from django.test.client import Client
        yield Client()
    finally:
        del os.environ['DJANGO_SETTINGS_MODULE']
        sys.path = sys.path[1:]
