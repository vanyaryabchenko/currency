

from currency.models import ContactUs


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_rate_list(client):
    response = client.get('/currency/rate/list')
    assert response.status_code == 200


def test_post_empty_form(client):
    response = client.post('/currency/contactus/create')
    assert response.status_code == 200


def test_post_empty_form_errors(client):
    response = client.post('/currency/contactus/create')
    assert response.context_data['form']._errors == {
        'email_from': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.']
    }


def test_post_invalid_data(client):
    payload = {
        'email_from': 'invalid',
        'subject': 'subject',
        'message': 'message'
    }
    response = client.post('/currency/contactus/create', data=payload)
    assert response.context_data['form']._errors == {
        'email_from': ['Enter a valid email address.']
    }


def test_post_valid_data(client, mailoutbox, settings):
    payload = {
        'email_from': 'valid@gmail.com',
        'subject': 'subject',
        'message': 'message'
    }
    response = client.post('/currency/contactus/create', data=payload)
    assert response.status_code == 302
    assert response['Location'] == '/currency/contactus/list'
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
    assert ContactUs.objects.count() == 1
