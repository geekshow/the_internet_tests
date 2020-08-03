import re

import pytest
from selenium import webdriver

TARGET_WEB_PAGE = "http://the-internet.herokuapp.com/challenging_dom"
CHROME_PATH = "/home/kp/Downloads/chromedriver"


@pytest.fixture(scope="module")
def web():
    """
    Fixture to setup and return selenium session
    Tears down session after tests
    :returns webdriver
    """
    print(f"\nSetting up webdriver using Chrome: {CHROME_PATH}")
    driver = webdriver.Chrome(CHROME_PATH)
    yield driver

    # test teardown
    driver.close()


def test_load_page(web):
    """
    Check that the target web page can be opened.
    Check the title matches the expected page title "The Internet"
    """
    print(f"\nGetting URL {TARGET_WEB_PAGE}")
    web.get(TARGET_WEB_PAGE)
    assert "The Internet" in web.title


def test_check_page_header(web):
    """
    Check the page header matches the expected name "Challenging DOM"
    """
    print(f"\nChecking Page Header 'Challenging DOM'")
    assert web.find_element_by_xpath('//div[@class="example"]/h3').text == "Challenging DOM"


def test_check_button(web):
    """
    Test that checks the operation of the element "button" in blue
    This also checks that the element attribute "id" is changed after the button is clicked
    """
    el = web.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    button_id = el.get_attribute("id")
    el.click()
    el = web.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button"]')
    assert el.get_attribute("id") != button_id


def test_check_button_alert(web):
    """
    Test that checks the operation of the element "button alert" in red
    This also checks that the element attribute "id" is changed after the button is clicked
    """
    el = web.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button alert"]')
    button_id = el.get_attribute("id")
    el.click()
    el = web.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button alert"]')
    assert el.get_attribute("id") != button_id


def test_check_button_success(web):
    """
    Test that checks the operation of the element "button success" in green
    This also checks that the element attribute "id" is changed after the button is clicked
    """
    el = web.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button success"]')
    button_id = el.get_attribute("id")
    el.click()
    el = web.find_element_by_xpath('//div[@class="large-2 columns"]/a[@class="button success"]')
    assert el.get_attribute("id") != button_id


def test_check_table_header(web):
    """
    Check the static header of the table
    """
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[1]').text == "Lorem"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[2]').text == "Ipsum"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[3]').text == "Dolor"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[4]').text == "Sit"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[5]').text == "Amet"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[6]').text == "Diceret"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/thead/tr/th[7]').text == "Action"


def test_check_first_table_column(web):
    """
    Check first column elements in the table  # TODO replace with iteration
    """
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[1]/td[1]').text == "Iuvaret0"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[2]/td[1]').text == "Iuvaret1"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[3]/td[1]').text == "Iuvaret2"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[4]/td[1]').text == "Iuvaret3"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[5]/td[1]').text == "Iuvaret4"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[6]/td[1]').text == "Iuvaret5"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[7]/td[1]').text == "Iuvaret6"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[8]/td[1]').text == "Iuvaret7"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[9]/td[1]').text == "Iuvaret8"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[10]/td[1]').text == "Iuvaret9"


def test_check_second_table_column(web):
    """
    Check second column elements in the table  # TODO replace with iteration
    """
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[1]/td[2]').text == "Apeirian0"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[2]/td[2]').text == "Apeirian1"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[3]/td[2]').text == "Apeirian2"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[4]/td[2]').text == "Apeirian3"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[5]/td[2]').text == "Apeirian4"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[6]/td[2]').text == "Apeirian5"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[7]/td[2]').text == "Apeirian6"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[8]/td[2]').text == "Apeirian7"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[9]/td[2]').text == "Apeirian8"
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[10]/td[2]').text == "Apeirian9"


@pytest.mark.xfail
def test_edit_second_line(web):
    """
    Check the operation of the edit link on the second line of the table
    I'm not clear what's meant to happen when the edit button is clicked
    """
    web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[2]/td[7]/a[1]').click()  # TODO use the href
    # Just guessing here, but check the edit link is no longer there?
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[2]/td[7]/a[1]').text != "edit"


@pytest.mark.xfail
def test_delete_sixth_line(web):
    """
    Check the delete button on the sixth line (spot check)
    """
    web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[6]/td[7]/a[2]').click()  # TODO use the href
    # expecting this line to be deleted and the line below to move up - check for line 7's content on line 6
    assert web.find_element_by_xpath('//div[@class="large-10 columns"]/table/tbody/tr[6]/td[1]').text == "Iuvaret6"


def test_answer_changes_on_refresh(web):
    """
    Check the answer field rolls on page refresh
    """
    # grab the canvas generation script block, which contains the Answer buried in javascript
    script_block = web.find_element_by_xpath('//div[@id="content"]/script').get_attribute('innerHTML')
    # pick out the number after 'Answer' using regex
    old_answer = re.search(r"Answer:\s(\d+)", script_block).group(1)
    print(f"\nFound current Answer value: {old_answer}")
    # refresh page
    web.refresh()
    # grab the canvas generation script block, which contains the Answer buried in javascript
    script_block = web.find_element_by_xpath('//div[@id="content"]/script').get_attribute('innerHTML')
    # pick out the number after 'Answer' using regex
    new_answer = re.search(r"Answer:\s(\d+)", script_block).group(1)
    print(f"\nFound new Answer value: {new_answer}")

    assert old_answer != new_answer
