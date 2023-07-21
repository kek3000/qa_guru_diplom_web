from datetime import date

import allure

from demoqa_tests.model.data.student import Student, Hobby
from demoqa_tests.model.pages import practice_form_module
from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.utils.parser_files import read_txt_file

practice_form = PracticePage()


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests DemoQA')
@allure.title('Successful registration')
def test_registration():
    student = Student(
        first_name='Nikita',
        last_name='Alekseev',
        email='test@gmail.com',
        phone='8999944455',
        address='Reutov',
        birthday=date(2001, 1, 1),
        gender='Male',
        subject='Economics',
        hobby=[Hobby.Music, Hobby.Sports],
        image='Toolsqa.jpg',
        state='Haryana',
        city='Karnal')
    with allure.step('Opening the registration page'):
        practice_form.open()
    with allure.step('Filling out the form'):
        practice_form.fill(student).submit()
    with allure.step('Checking the values of the resulting form'):
        practice_form.assert_results_registration(student)


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests DemoQA')
@allure.title('Successful registration with required fields')
def test_registration_required_field():
    with allure.step('Opening the registration page'):
        practice_form_module.opening()
    with allure.step('Filling out the form'):
        practice_form_module.fill_registration_form(*read_txt_file('student.txt'))
    with allure.step('Checking the values of the resulting form'):
        practice_form_module.assert_results_registration(
            [('Student Name', 'Nikita Alekseev'),
             ('Gender', 'Male'),
             ('Mobile', '8999944455')])


