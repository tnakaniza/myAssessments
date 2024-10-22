# Utils/driver_factory.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import os

class DriverFactory:
    @staticmethod
    def get_driver():
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # Add more options if needed

        service = ChromeService(executable_path=os.path.abspath("chromedriver"))
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
