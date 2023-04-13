from conftest import *

# Endpoints

inventory_url = base_url + '/store/inventory'
create_order_url = base_url + '/store/order'
order_id_url = base_url + '/store/order/3'


@pytest.mark.method_GET
def test_get_store_inventory():
    """Returns pet inventories by status."""
    response = requests.get(inventory_url)
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'


@pytest.mark.method_POST_GET
def test_create_order():
    """Place an order for a pet / Verifies order has been placed."""

    # Creating new order / Asserting status code and json schema
    response = requests.post(create_order_url, json=JsonData.new_order)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert S(
        JsonData.schema_new_order) == data, f'Expected {S(JsonData.schema_new_order)}, got {data} instead'

    # Getting info about created order / Asserting placed status in order's data
    verify_order_exists_response = requests.get(order_id_url)
    get_order_data = verify_order_exists_response.json()
    assert "placed" in get_order_data['status'], f'Expected placed status in {get_order_data["status"]}, order was ' \
                                                 f'not placed '


@pytest.mark.method_DELETE
def test_delete_order():
    """Delete purchase order by ID / Verifies order has been deleted."""

    # Creating new order / Asserting status code and json schema
    response = requests.post(create_order_url, json=JsonData.new_order_2)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status code, got {response.status_code} instead'
    assert S(
        JsonData.schema_new_order) == data, f'Expected {S(JsonData.schema_new_order)}, got {data} instead'

    # Delete created order / Asserting status code
    response_for_delete = requests.delete(order_id_url)
    assert response_for_delete.status_code == 200, f'Expected 200 status code, got {response_for_delete.status_code} instead '

    # Getting info about deleted order / Asserting 404 status code
    # Asserting Order Not Found in response's data
    get_order_response = requests.get(order_id_url)
    get_order_data = get_order_response.json()
    assert get_order_response.status_code == 404, f'Expected 404 status code, got {response_for_delete.status_code} instead '
    assert 'Order not found' in get_order_data["message"], 'Order was not deleted'
