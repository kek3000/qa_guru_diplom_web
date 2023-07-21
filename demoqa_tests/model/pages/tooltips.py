from selene import have
from selene.support.shared import browser


class TooltipPage:

    def open(self):
        browser.open('/tool-tips')
        browser.driver.execute_script('$("#fixedban").remove()')
        return self

    def set_focus_in_field(self):
        browser.element('#toolTipTextField').hover()
        return self

    def assert_text_field(self):
        browser.element('#textFieldToolTip').should(have.text('You hovered over the text field'))
        return self

    def set_focus_in_button(self):
        browser.element('#toolTipButton').hover()
        return self

    def assert_text_button(self):
        browser.element('#buttonToolTip').should(have.text('You hovered over the Button'))
        return self


