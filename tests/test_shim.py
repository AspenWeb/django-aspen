def test_django_shim_is_importable():
    from aspen.shims import django as shim
    assert shim

def test_django_shim_basically_works(harness, django_client):
    harness.fs.project.mk(('www/index.spt', '''
program = request.GET['program']
[-----] text/html
Greetings, {{program}}!
'''))
    response = django_client.request(QUERY_STRING='program=django')
    assert response.content == 'Greetings, django!\n'
