import yaml
from module import Site
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
username = testdata["username"]
password = testdata["password"]


def test_step1(sel_1, x_selector2, x_selector3, btn_selector, result):
    input1 = site.find_element("xpath", sel_1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector3)
    res = err_label.text
    assert res == result


def test_step2(sel_1, x_selector2, auth, btn_selector, result2):
    input1 = site.find_element("xpath", sel_1)
    input1.clear()
    input1.send_keys(username)
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(password)
    btn = site.find_element("css", btn_selector)
    btn.click()
    auth = site.find_element("xpath", auth)
    res = auth.text
    assert res == result2


def test_step3(btn_create_post, sel_title, sel_desc, sel_content, btn_post_safe, check_title, result3):
    btn = site.find_element("xpath", btn_create_post)
    btn.click()
    time.sleep(testdata["sleep_time"])
    input_title = site.find_element("xpath", sel_title)
    input_title.send_keys('Ту́рция')
    input_desc = site.find_element("xpath", sel_desc)
    input_desc.send_keys('Турция граничит с 14 государствами')
    input_content = site.find_element("xpath", sel_content)
    input_content.send_keys('Современная Турция образовалась в 1923 году в результате распада '
                            'Османской империи после её поражения в Первой мировой войне и '
                            'последовавшей национально-освободительной войны турецкого народа, '
                            'упразднения монархии и создания на территории восточной Фракии, '
                            'Малой Азии и Армянского нагорья турецкого национального государства.')
    btn_s = site.find_element("xpath", btn_post_safe)
    btn_s.click()
    time.sleep(testdata["sleep_time"])
    title_check = site.find_element("xpath", check_title)
    res = title_check.text
    site.close()
    assert res == result3
