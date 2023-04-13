import requests

from conftest import *

# Endpoints

create_user_url = base_url + '/user'
username_url = base_url + '/user/Tommy'
upd_user_url = base_url + '/user/CJ'
delete_user_url = base_url + '/user/Paul'
login_url = base_url + '/user/login'
auth = ("username", "password")
logout_url = base_url + '/user/logout'
users_array_url = base_url + '/user/createWithArray'


@pytest.mark.method_POST
def test_create_new_user():
    """Creates a new user."""
    response = requests.post(create_user_url, json=JsonData.new_user)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert S(JsonData.schema_post_upd_dlt) == data, f'Expected {S(JsonData.schema_post_upd_dlt)}, got {data} instead'


@pytest.mark.method_GET
def test_get_user_by_username():
    """Gets user by username."""
    response = requests.get(username_url)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert data['username'] == 'Tommy', 'No such user in response data'


@pytest.mark.method_PUT
def test_update_user():
    """Updates user info / Verifies user info has been updated."""

    # Creating new user
    create_new_user_response = requests.post(create_user_url, json=JsonData.new_user_2)
    assert create_new_user_response.status_code == 200, f'Expected 200 status code, got {create_new_user_response.status_code} instead '

    # Getting user info before updating / asserting response's status code
    user_info_before_update = requests.get(upd_user_url)
    old_data = user_info_before_update.json()
    assert user_info_before_update.status_code == 200

    # Updating user info / asserting response's status code
    update_user_response = requests.put(upd_user_url, json=JsonData.update_user)
    assert update_user_response.status_code == 200, f'Expected 200 status code, got {update_user_response.status_code} instead '

    # Getting user info after updating / Comparing both info samples to verify the updates have taken place
    user_info_after_update = requests.get(upd_user_url)
    new_data = user_info_after_update.json()
    assert old_data != new_data


@pytest.mark.method_DELETE
def test_delete_user():
    """Deletes user / Verifies user has been deleted."""

    # Create new user
    create_new_user_response = requests.post(create_user_url, json=JsonData.new_user_3)
    assert create_new_user_response.status_code == 200, f'Expected 200 status code, got {create_new_user_response.status_code} instead '

    # Delete created user
    delete_user_response = requests.delete(delete_user_url)
    assert delete_user_response.status_code == 200, f'Expected 200 status code, got {create_new_user_response.status_code} instead '

    # Check that user is not in the database
    response = requests.get(delete_user_url)
    assert response.status_code == 404, f'Expected 404 status code, got {response.status_code} instead'


@pytest.mark.method_POST
def test_create_user_array():
    """Creates list of users with given input array"""

    # Creating multiple users
    response = requests.post(users_array_url, json=JsonData.users_array)
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'

    # Extracting info about recently added user
    recently_added_user = requests.get(
        f"https://petstore.swagger.io/v2/user/{JsonData.users_array[0]['username']}"
    )
    data = recently_added_user.json()

    # Asserting that recently added user matches with user from payloads data
    assert data["username"] == JsonData.users_array[0]["username"]


@pytest.mark.method_GET
def test_login():
    """Logs user into the system."""
    response = requests.get(login_url, auth=auth)
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'


@pytest.mark.method_GET
def test_logout():
    """Logs out current logged-in user session."""
    response = requests.get(logout_url)
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
