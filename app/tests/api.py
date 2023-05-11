from currency.models import Source


def test_api_get_source(api_client):
    response = api_client.get('/api/currency/source/')
    assert response.status_code == 200


def test_api_post_source_status_code(api_client):
    payload = {
        "source_url": "https://api.monobank.ua/bank/currency",
        "name": "test",
        "code_name": "test"
    }
    response = api_client.post('/api/currency/source/', data=payload)
    assert response.status_code == 201


def test_api_post_source_valid_data(api_client):
    initial_count = Source.objects.count()
    payload = {
        "source_url": "https://api.monobank.ua/bank/currency",
        "name": "test",
        "code_name": "test"
    }
    api_client.post('/api/currency/source/', data=payload)
    assert Source.objects.count() == initial_count + 1


def test_api_post_source_invalid_data(api_client):
    initial_count = Source.objects.count()
    error = {'source_url': ['Enter a valid URL.']}
    payload = {
        "source_url": "api.monobank.ua/bank/currency",
        "name": "test",
        "code_name": "test"
    }
    response = api_client.post('/api/currency/source/', data=payload)
    assert response.json() == error
    assert Source.objects.count() == initial_count
    assert response.status_code == 400


def test_api_post_source_empty(api_client):
    error = {
        'source_url': ['This field is required.'],
        'name': ['This field is required.'],
        'code_name': ['This field is required.']
    }
    response = api_client.post('/api/currency/source/')
    assert response.json() == error
    assert response.status_code == 400


def test_api_source_put_status_code(api_client):
    payload = {
      "source_url": "https://api.test.ua/bank/currency",
      "name": "testtest",
      "code_name": "testtest"
    }
    response = api_client.put('/api/currency/source/3/', data=payload)
    assert response.status_code == 200


def test_api_source_put_invalid_data(api_client):
    payload = {
      "source_url": "invalid url",
      "name": "testtest"
    }
    error = {'source_url': ['Enter a valid URL.'], 'code_name': ['This field is required.']}
    response = api_client.put('/api/currency/source/3/', data=payload)
    assert response.status_code == 400
    assert response.json() == error


def test_api_source_patch_status_code(api_client):
    payload = {
      "code_name": "testtest"
    }
    response = api_client.patch('/api/currency/source/4/', data=payload)
    assert response.status_code == 200


def test_api_source_patch_invalid_data(api_client):
    payload = {
      "source_url": "invalid url",
    }
    error = {'source_url': ['Enter a valid URL.']}
    response = api_client.patch('/api/currency/source/4/', data=payload)
    assert response.status_code == 400
    assert response.json() == error


def test_api_delete_source_status_code(api_client):
    response = api_client.delete('/api/currency/source/4/')
    assert response.status_code == 204


def test_api_delete_source_count_data(api_client):
    initial_count = Source.objects.count()
    api_client.delete('/api/currency/source/4/')
    assert Source.objects.count() == initial_count - 1
