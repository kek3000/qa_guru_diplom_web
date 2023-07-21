import allure
from demoqa_tests.model.pages.tooltips import TooltipPage

tooltips = TooltipPage()


@allure.label('owner', 'Nikita Alekseev')
@allure.title('Text field tooltip')
def test_confirm_alert_field():
    with allure.step('Opening the hint page'):
        tooltips.open()
    with allure.step('Setting focus on the field'):
        tooltips.set_focus_in_field()
    with allure.step('Check hint text'):
        tooltips.assert_text_field()


@allure.label('owner', 'Nikita Alekseev')
@allure.title('Text button tooltip')
def test_confirm_alert_button():
    with allure.step('Opening the hint page'):
        tooltips.open()
    with allure.step('Setting focus on the button'):
        tooltips.set_focus_in_button()
    with allure.step('Check hint text'):
        tooltips.assert_text_button()
