import requests
import pytest

@pytest.fixture()
def new_post_id():
    body = {"title": "foo", "body": "bar", "userId": 1}
    headers = {'Content-type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    yield post_id
    print('Deleting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('Bye')

#@pytest.mark.skip('No preconditions')
def test_get_one_post(new_post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}]').json()
    assert response['id'] == new_post_id

@pytest.mark.regression
def test_get_all_posts(hello):
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100


def test_add_post():
    body = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    headers = {'Content-type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.status_code == 201
    assert response.json()['id'] == 101

@pytest.mark.smoke
def test_one():
    assert 1 == 1

@pytest.mark.regression
def test_two():
    assert 1 == 1

@pytest.mark.parametrize('logins',['', '    ','9#^$^'])
def test_three(logins):
    print(logins)
    assert 1 == 1