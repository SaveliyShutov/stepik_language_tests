from selenium.webdriver.common.by import By

LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button_on_product_page(browser):
    browser.get(LINK)
    add_buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(add_buttons) == 1, "Add to basket button is not presented on product page"
