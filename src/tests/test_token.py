from django.contrib.auth.models import User
from django.urls import reverse

import pytest


@pytest.mark.django_db
def test_token(client):
    test_token_url = reverse('token_test')
    response = client.post(test_token_url)
    assert response.status_code == 200
    assert response.data['message'] == 'Not authenticated user.'

    User.objects.create_user(
        username='user1',
        email='user1@mail.com',
        password='user1pass'
    )

    response = client.post(
        reverse('token_obtain_pair'),
        {'username': 'user1', 'password': 'user1pass'},
        format='json',
    )
    assert 'access' in response.data
    token = response.data['access']

    response = client.post(
        test_token_url,
        {},
        HTTP_AUTHORIZATION=f'JWT {token}',
    )
    assert response.status_code == 200
    assert response.data['message'] == 'Authenticated user.'
