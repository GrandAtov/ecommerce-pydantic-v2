from .data.dummy_data import customer

def test_customer_created():
    assert customer.name == "Grand Atov"