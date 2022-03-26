import time
from typing import NoReturn, Tuple

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
    NoSuchElementException,
)

from pages.base import BasePage
from utilites.locators import (
    CancelRequestLocators,
    CloseChangeLocators,
    DateSectionSelector,
    CommonChangeCreateLocators,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

"""
A class for Cancel the unused Change Requests. For cancelling a 
Request all the functions should be declared here

written by: jiaul_islam
"""


class CancelRequests(BasePage):
    """A class for mimicking the user interactions to cancel a Change Request"""

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_change_request_opened(self) -> bool:
        """Checks if the current working change request is opened or not"""
        try:
            self.click(DateSectionSelector.DATE_PAGE)
            status = self.is_visible(DateSectionSelector.START_DATE_INPUT)

            if status:
                value = self.find_element(
                    *CloseChangeLocators.ACTUAL_OPEN_DATE
                ).get_attribute("value")
                if value == "":
                    return False
                else:
                    return True
        except TimeoutException as error:
            print(error)
        except ElementClickInterceptedException:
            time.sleep(2)
            self.click(DateSectionSelector.DATE_PAGE)
            status = self.is_visible(DateSectionSelector.START_DATE_INPUT)
            if status:
                value = self.find_element(
                    *CloseChangeLocators.ACTUAL_OPEN_DATE
                ).get_attribute("value")
                if value == "":
                    return False
                else:
                    return True

    def is_cancelled(self) -> bool:
        """Checks if the Cancellation is successful or not"""
        status_value = self.get_text(CancelRequestLocators.STATUS_AREA)
        if status_value == "Cancelled":
            return True
        else:
            return False

    def select_cancel(self) -> NoReturn:
        """select the Cancel Option from Status Menu"""
        self.click(CancelRequestLocators.MENU_FOR_STATUS)
        self.hover_over(CancelRequestLocators.CANCEL_OPTION_SELECT)
        self.click(CancelRequestLocators.CANCEL_OPTION_SELECT)

    def save_status(self) -> NoReturn:
        """Save the change status to cancelled"""
        self.click(CancelRequestLocators.SAVE)

    def get_cancelled_cr_number(self):
        """Get the Cancelled Changed Number"""
        change_number = ""
        while change_number == "" or None:
            try:
                return self.get_text(CommonChangeCreateLocators.CHANGE_NUMBER_VALUE)
            except NoSuchElementException:
                raise Exception("Timed out.....")

    def _wait_for_loading_icon_disappear(
        self, locator: Tuple[By, str], _time: float = 1, _range: int = 600
    ) -> None:
        """Wait for loading_icon to vanish"""
        _counter = 1
        while _counter <= _range:
            _loading_icons: list = self.find_elements(*locator)
            if not len(_loading_icons):
                break
            time.sleep(_time)
            _counter += 1

    def cancel_sfa_cr(self) -> NoReturn:
        """Cancels the SFA Change Request"""
        # driver.find_element(By.XPATH, "//*[@id='WIN_3_301542100']/a").click()
        base_window = self._driver.current_window_handle
        self.click(CancelRequestLocators.ARROW_FOR_SFA)
        actions = ActionChains(self._driver)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        time.sleep(0.8)
        actions = ActionChains(self._driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        for w1 in self._driver.window_handles:
            if w1 != base_window:
                self._driver.switch_to.window(w1)
                self.click(CancelRequestLocators.YES_BTN)
                time.sleep(1)
                break
        self._driver.switch_to.window(base_window)
        self._wait_for_loading_icon_disappear(CommonChangeCreateLocators.LOADING_ICON)