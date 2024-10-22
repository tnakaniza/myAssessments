# Tests/conftest.py

import pytest
from Utils.driver_factory import DriverFactory
from Utils.config import BASE_URL

@pytest.fixture(scope="class")
def setup(request):
    driver = DriverFactory.get_driver()
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()
