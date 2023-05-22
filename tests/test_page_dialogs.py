from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal = ModalDialogs(browser)

    modal.visit()
    assert modal.btn_submenu.check_count_elements(5)
    modal.btn_all.find_elements()

def test_navigation_modal(browser):
    modal = ModalDialogs(browser)
    demo = DemoQa(browser)

    modal.visit()
    modal.refresh()
    modal.icon.click()

    browser.back()
    browser.set_window_size(900, 400)

    browser.forward()
    assert demo.equal_url()
    assert browser.title == 'DEMOQA'

    browser.set_window_size(1000, 1000)
