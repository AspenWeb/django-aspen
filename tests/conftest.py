import pytest

@pytest.yield_fixture
def DjangoClient():
    def _DjangoClient(*a, **kw):
        try:
            from django.test.client import Client
        except ImportError:
            raise pytest.skip.Exception
        else:
            return Client(*a, **kw)
    yield _DjangoClient
