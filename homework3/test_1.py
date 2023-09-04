import time
import yaml
from testpage import OperationsHelper
import logging
from post_page import OperationAddPost


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

username = testdata["username"]
password = testdata["password"]


def test_step1(browser):
    logging.info("Test1 run")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("test2 running")
    testpage = OperationsHelper(browser)
    testpage.enter_login(username)
    testpage.enter_pass(password)
    testpage.click_login_button()
    assert testpage.auth() == f"Hello, {username}"


def test_step3(browser):
    logging.info("test3 running")
    testpage = OperationAddPost(browser)
    testpage.add_post()
    time.sleep(1)
    title = "New title"
    testpage.post_context(title=title, description="New description", content="New content")
    time.sleep(1)
    assert title == testpage.check_post()


def test_step4(browser):
    logging.info("test4 running")
    testpage = OperationAddPost(browser)
    testpage.go_to_site()
    testpage.add_post()
    time.sleep(1)
    title = "New title2"
    testpage.post_context(title=title, description="New description")
    time.sleep(1)
    assert title == testpage.check_post()


def test_step5(browser):
    logging.info("test5 running")
    testpage = OperationAddPost(browser)
    testpage.go_to_site()
    testpage.add_post()
    time.sleep(1)
    title = "New title3"
    testpage.post_context(title=title, content="New content")
    time.sleep(1)
    assert title == testpage.check_post()


def test_step6(browser):
    logging.info("test6 running")
    testpage = OperationAddPost(browser)
    testpage.go_to_site()
    testpage.add_post()
    time.sleep(1)
    title = "New title4"
    testpage.post_context(title=title)
    time.sleep(1)
    assert title == testpage.check_post()


def test_step7(browser):
    logging.info("test7 running")
    testpage = OperationAddPost(browser)
    testpage.go_to_site()
    testpage.check_contact_us(name="ivan22", email="kenny@yandex.ru", content="Hello!")
    time.sleep(1)
    alert_text = "Form successfully submitted"
    assert alert_text == testpage.check_alert()