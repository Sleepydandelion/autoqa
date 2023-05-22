from pages.text_box import TextBox


def test_clear(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('Happy')
    text_box.address.send_keys('Happy happy happy')
    text_box.btn_submit.click_force()
    assert text_box.name2.get_text() == 'Name:Happy'
    assert text_box.address2.get_text() == 'Current Address :Happy happy happy'





