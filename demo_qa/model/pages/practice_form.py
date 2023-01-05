from selene.support.shared import browser
from selene import be, have
from demo_qa.model.controls import radiobuttons, checkboxes, datepickers, dropdowns
from demo_qa.utils import paths


def type_first_name(name):
    browser.element('#firstName').should(be.blank).type(name)


def type_last_name(surname):
    browser.element('#lastName').should(be.blank).type(surname)


def type_email(email):
    browser.element('#userEmail').should(be.blank).type(email)


def pick_gender():
    radiobuttons.select_option('[name=gender][value=Female] + label')


def type_phone_number(value):
    browser.element('#userNumber').type(value)


def choose_hobbies(value):
    checkboxes.select_options('[for^=hobbies-checkbox]', value)


def type_subject(value):
    browser.element('#subjectsInput').type(value).press_enter()


def select_picture(rel_path):
    paths.path_to_image('#uploadPicture', rel_path)


def type_address(value):
    browser.element('#currentAddress').should(be.blank).type(value)


def enter_birthday():
    datepickers.select_date_of_birth()


def select_state(value):
    dropdowns.select_option('#state', value)


def select_city(value):
    dropdowns.select_option('#city', value)


def submit_data():
    browser.element('#submit').press_enter()


def validate_data(*values):
    browser.element('.table').all('td').even.should(have.texts(values))