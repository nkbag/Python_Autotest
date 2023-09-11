import logging

from Homework4.conftest import browser
from Homework4.testpage import OperationsHelper


def test_step1():
    logging.info("Test1 API run")
    testpage = OperationsHelper(browser)
    assert testpage.auth_site()[0] == 200, "Test1 API failed"


def test_step2():
    logging.info("Test2 API run")
    testpage = OperationsHelper(browser)
    assert testpage.create_post() == "description", "Test2 API failed"
