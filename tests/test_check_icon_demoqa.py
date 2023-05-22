# from selenium.webdriver.common.by import By
# import time
from pages.demoqa import DemoQa


def test_check_icon(browser):
    # browser.get('https://demoqa.com/')
    #
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    # if icon is None:
    #     print('Элемент не найден')
    # else:
    #     print('Элемент найден')

    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    # time.sleep(2)
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    # time.sleep(2)
    assert demo_qa_page.icon.exist()
