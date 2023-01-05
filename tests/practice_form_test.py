from selene.support.shared import browser
from demo_qa.model.pages import practice_form


def test_student_registration_form():
    browser.open('/automation-practice-form')

    practice_form.type_first_name('Iuliia')
    practice_form.type_last_name('Ekkart')
    practice_form.type_email('test@mail.com')
    practice_form.pick_gender()
    practice_form.type_phone_number('0123456789')
    practice_form.enter_birthday()
    practice_form.choose_hobbies('Music')
    practice_form.type_subject('Accounting')
    practice_form.select_picture('resources/more.jpg')
    practice_form.type_address('Sitsevaya st')
    practice_form.select_state('Rajasthan')
    practice_form.select_city('Jaipur')

    practice_form.submit_data()
    practice_form.validate_data(
        'Iuliia Ekkart',
        'test@mail.com',
        'Female',
        '0123456789',
        '14 November,1985',
        'Accounting',
        'Music',
        'more.jpg',
        'Sitsevaya st',
        'Rajasthan Jaipur')


