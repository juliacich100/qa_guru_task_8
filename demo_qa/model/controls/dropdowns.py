from selene.support.shared import browser


def select_option(selector, value):
    browser.element(selector + ' [id^=react-select][id*=input]').type(value).press_enter()