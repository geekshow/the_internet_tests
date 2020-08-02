import pytest
import logging as log
from selenium import webdriver

# Settings function
from selenium.webdriver.chrome.webdriver import WebDriver


TARGET_WEB_PAGE = "http://the-internet.herokuapp.com/challenging_dom"
CHROME_PATH = "/home/kp/Downloads/chromedriver"

log.basicConfig()

@pytest.fixture(scope="module")
def web_session() -> webdriver:
    """
    Fixture to setup and return selenium session
    Tears down session after tests
    :returns webdriver
    """
    log.info(f"Setting up webdriver using Chrome: {CHROME_PATH}")
    driver = webdriver.Chrome(CHROME_PATH)
    yield driver

    # test teardown
    driver.close()


def test_load_page(web_session):
    """
    Check that the target web page can be opened.
    Check the title matches the expected page title "The Internet"
    """
    log.info(f"Getting URL {TARGET_WEB_PAGE}")
    web_session.get(TARGET_WEB_PAGE)
    assert "The Internet" in web_session.title


def test_check_page_header(web_session):
    """
    This test checks that the page header matches the expected name "Challenging DOM"
    """
    log.info("Checking Page Header"["web_url"])
    assert web_session.find_element_by_xpath('//div[@class="example"]/h3').text == "Challenging DOM"


def test_check_button(web_session):
    """
    Test that checks the operation of the element "button"
    This also checks that the element attribute "id" is changed after the button is clicked
    """
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button_id = el.get_attribute("id")
    el.click()
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    assert el.get_attribute("id") != button_id


def test_check_button_alert(web_session):
    """
    Test that checks the operation of the element "button alert"
    This also checks that the element attribute "id" is changed after the button is clicked
    """
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button alert"]')
    button_id = el.get_attribute("id")
    el.click()
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button alert"]')
    assert el.get_attribute("id") != button_id


def test_check_button_success(web_session):
    """
    Test that checks the operation of the element "button success"
    This also checks that the element attribute "id" is changed after the button is clicked
    """
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button success"]')
    button_id = el.get_attribute("id")
    el.click()
    el = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button success"]')
    assert el.get_attribute("id") != button_id


def test_check_table_header_one(web_session):
    """
    Test that checks the text of the first header of the table
    This also checks that the text of the first header dose not change after a page refresh
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[1]')
    th_text = el.text
    assert th_text == "Lorem"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    log.info(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[1]').text == th_text


def test_check_table_header_two(web_session):
    """
    Test that checks the text of the second header of the table
    This also checks that the text of the second header dose not change after a page refresh
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[2]')
    th_text = el.text
    assert th_text == "Ipsum"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    log.info(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[2]').text == th_text


def test_check_table_header_three(web_session):
    """
    Test that checks the text of the third header of the table
    This also checks that the text of the third header dose not change after a page refresh
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[3]')
    th_text = el.text
    assert th_text == "Dolor"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    log.info(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[3]').text == th_text


def test_check_table_header_four(web_session):
    """
    Test that checks the text of the forth header of the table
    This also checks that the text of the forth header dose not change after a page refresh
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[4]')
    th_text = el.text
    assert th_text == "Sit"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    log.info(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[4]').text == th_text


def test_check_table_header_five(web_session):
    """
    Test that checks the text of the fifth header of the table
    This also checks that the text of the fifth header dose not change after a page refresh
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[5]')
    th_text = el.text
    assert th_text == "Amet"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    log.info(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[5]').text == th_text


def test_check_table_header_six(web_session):
    """
    Test that checks the text of the sixth header of the table
    This also checks that the text of the sixth header dose not change after a page refresh
    """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[6]')
    th_text = el.text
    assert th_text == "Diceret"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    log.info(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[6]').text == th_text


def test_check_table_header_seven(web_session):
    """
    Test that checks the text of the seventh header of the table
    This also checks that the text of the seventh header dose not change after a page refresh
   """
    el = web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[7]')
    th_text = el.text
    assert th_text == "Action"
    button = web_session.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button.click()
    log.info(th_text)
    assert web_session.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[7]').text == th_text


def test_check_first_table_edit_button(web_session):
    """
    Test that checks the first edit button of the table is enabled
    """
    el = web_session.find_element_by_xpath('//div[2]/table/tbody/tr[1]/td[7]/a[1]')
    if el.is_enabled():
        log.info("Edit Enabled")
    else:
        log.info("Edit not enabled")


def test_check_first_table_delete_button(web_session):
    """
    Test that checks the first delete button of the table is enabled
    """
    el = web_session.find_element_by_xpath('//div[2]/table/tbody/tr[1]/td[7]/a[2]')
    if el.is_enabled():
        log.info("Delete Enabled")
    else:
        log.info("Delete not enabled")


# TODO add test to store answer produced by script element, refresh page, and check that new answer is produced.