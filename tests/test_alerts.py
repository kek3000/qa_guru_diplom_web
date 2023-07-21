import allure
from demoqa_tests.model.pages.alerts import AlertsPage

alerts = AlertsPage()


@allure.label('owner', 'Nikita Alekseev')
@allure.title('Alert confirmation ok')
def test_confirm_alert():
    with allure.step('Opening the alert page'):
        alerts.open()
    with allure.step('Button click to trigger alert'):
        alerts.click_btn_with_confirm_ok()
    with allure.step('Check alert confirmation'):
        alerts.assert_confirm_alert_ok()


@allure.label('owner', 'Nikita Alekseev')
@allure.title('Alert confirmation ok')
def test_confirm_alert():
    with allure.step('Opening the alert page'):
        alerts.open()
    with allure.step('Button click to trigger alert'):
        alerts.click_btn_with_confirm_cancel()
    with allure.step('Check alert confirmation'):
        alerts.assert_confirm_alert_cancel()


@allure.label('owner', 'Nikita Alekseev')
@allure.title('Acknowledge alert with text field filled')
def test_prompt_alert():
    with allure.step('Opening the alert page'):
        alerts.open()
    with allure.step('Button click to trigger alert'):
        alerts.click_btn_with_prompt()
    with allure.step('Entering value in text field in alert'):
        alerts.type_to_alert('nikitaalekseev')
    with allure.step('Check alert confirmation'):
        alerts.assert_prompt_alert('nikitaalekseev')
