from conftest import *

# Endpoints

pet_url = base_url + '/pet'
pet_id = base_url + '/pet/5'
pet_id_delete = base_url + '/pet/2'
pet_id_check_deleted = base_url + '/pet/3'
pet_invalid_id = base_url + '/pet/10500'
upload_image_url = base_url + '/pet/4/uploadImage'
find_by_status_url = base_url + '/pet/findByStatus'


@pytest.mark.method_GET
def test_get_pet_by_valid_id():
    """Finds pet by id / Returns a single pet."""
    response = requests.get(pet_id)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert len(data['category']) > 0, f'{data} is empty'
    assert S(
        JsonData.schema_pet_get_put_post) == data, f'Expected {S(JsonData.schema_pet_get_put_post)}, got {data} instead'


@pytest.mark.method_GET
def test_get_by_invalid_id():
    """Checks that response code is 404."""
    response = requests.get(pet_invalid_id)
    data = response.json()
    assert response.status_code == 404, f'Expected 404 status code, got {response.status_code} instead'
    assert 'Pet not found' in data['message'], f'Expected Pet not found error, got  {data["message"]} instead.'


@pytest.mark.method_DELETE
def test_deletes_pet():
    """Deletes a pet."""
    response = requests.delete(pet_id_delete)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert S(JsonData.schema_post_upd_dlt) == data, f'Expected {S(JsonData.schema_post_upd_dlt)}, got {data} instead'


@pytest.mark.method_DELETE
def test_deletes_deleted_pet():
    """Deletes already deleted pet and checks that response code is 404."""
    response_1 = requests.delete(pet_id_check_deleted)
    response_2 = requests.delete(pet_id_check_deleted)
    assert response_1.status_code == 200, f'Expected 200 status code, got {response_1.status_code} instead'
    assert response_2.status_code == 404, f'Expected 404 status code, got {response_2.status_code} instead'


@pytest.mark.method_POST
def test_updates_pet_with_form_data():
    """Updates a pet in the store with form data by passing pet id (*required), pet name & pet status."""
    response = requests.post(pet_id, data=JsonData.update_pet)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert S(JsonData.schema_post_upd_dlt) == data, f'Expected {S(JsonData.schema_post_upd_dlt)}, got {data} instead'


@pytest.mark.method_POST
def test_upload_image():
    """Uploads an image by passing pet id (*required), additionalMetadata and file itself."""
    pet_img = {'file': open('pet.jpeg', 'rb')}
    response = requests.post(upload_image_url, files=pet_img)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert S(JsonData.schema_upload_image) == data, f'Expected {S(JsonData.schema_upload_image)}, got {data} instead'


@pytest.mark.method_POST
def test_add_new_pet():
    """Adds a new pet to the store."""
    response = requests.post(pet_url, json=JsonData.add_new_pet)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert len(data['category']) > 0, f'{data} is empty'
    assert S(
        JsonData.schema_pet_get_put_post) == data, f'Expected {S(JsonData.schema_pet_get_put_post)}, got {data} instead'


@pytest.mark.method_PUT
def test_update_pet():
    """Updates an existing pet."""
    response = requests.put(pet_url, json=JsonData.update_pet)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert len(data['category']) > 0, f'{data} is empty'
    assert S(
        JsonData.schema_pet_get_put_post) == data, f'Expected {S(JsonData.schema_pet_get_put_post)}, got {data} instead '


@pytest.mark.method_GET
@pytest.mark.parametrize('status', ['pending', 'available', 'sold'])
def test_find_by_status(status):
    """Finds pets by status."""
    response = requests.get(find_by_status_url, params=status)
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
