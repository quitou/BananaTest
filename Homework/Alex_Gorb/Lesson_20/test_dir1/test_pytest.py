import requests
import pytest
import allure


@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('Bye')

#@pytest.mark.skip('No preconditions')
@allure.feature('Posts')
@allure.story('Get posts')
def test_get_one_post(new_post_id):
    with allure.step(f'Run get request for post with id {new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}]').json()
    with allure.step(f'Check that post id is {new_post_id}'):
        assert response == {11}

@pytest.mark.regression
@allure.feature('Posts')
@allure.story('Get posts')
@allure.title('Получение всех постов')
def test_get_all_posts(hello):
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

@allure.feature('Posts')
@allure.story('Manipulate posts')
def test_add_post():
    with allure.step(f'Prepare test data'):
        body = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        headers = {'Content-type': 'application/json'}
    with allure.step('Run request to create a post'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
    with allure.step('Check response is 201'):
        assert response.status_code == 201
    with allure.step('Check id of create is 101'):
        assert response.json()['id'] == 101

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.smoke
def test_one():
    assert 1 == 1

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.regression
def test_two():
    assert 1 == 1

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.parametrize('logins',['', '    ','9#^$^'])
def test_three(logins):
    print(logins)
    assert 1 == 1