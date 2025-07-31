from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.bridgelabz.utilities.logger import Logger

class SignInPage:
    # Locators
    sign_login_xpath = "//span[contains(text(),'Sign in with Google')]"
    email_xpath = '//input[@type="email"]'
    password_name = "//input[@name='Passwd']"
    next_button_xpath = "//span[normalize-space()='Next']"

    profile_icon_xpath = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit MuiIconButton-edgeEnd MuiIconButton-sizeLarge css-1gj9yt8']"
    signout_button_xpath = "//p[normalize-space()='Sign Out']"

    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__)

    def open_page(self, url):
        """Open the given URL."""
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def handle_wait(self, driver=None):
        """Wait for Google sign-in button and click."""
        if driver is None:
            driver = self.driver

        self.logger.info("Waiting for Google sign-in button.")
        wait = WebDriverWait(driver, 15)
        sign_in_button = wait.until(
            EC.presence_of_element_located((By.XPATH, self.sign_login_xpath))
        )
        self.logger.info("Clicking on 'Sign in with Google' button.")
        sign_in_button.click()

    def enter_email(self, email):
        """Enter email in Google sign-in popup."""
        self.logger.info(f"Entering email: {email}")
        email_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.email_xpath))
        )
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        """Enter password in Google sign-in popup."""
        self.logger.info("Entering password.")
        wait = WebDriverWait(self.driver, 15)
        password_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.password_name))
        )
        password_input.clear()
        password_input.send_keys(password + Keys.TAB)

    def click_Next(self):
        """Click the Next button in Google login flow."""
        self.logger.info("Clicking on 'Next' button.")
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.next_button_xpath))
        ).click()

    def click_logout(self):
        """Logs the user out by clicking the profile icon and sign out."""
        self.logger.info("Initiating logout process.")
        wait = WebDriverWait(self.driver, 15)

        try:
            self.logger.info("Checking for overlay.")
            overlay = self.driver.find_element(By.XPATH, "//div[contains(@class,'fixed') and contains(@class,'z-50')]")
            self.logger.info("Hiding overlay using JavaScript.")
            self.driver.execute_script("arguments[0].style.display='none';", overlay)
        except Exception:
            self.logger.info("No overlay present. Continuing with logout.")

        self.logger.info("Clicking on profile icon.")
        profile_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@data-testid='AccountCircleIcon']/parent::button"))
        )
        self.driver.execute_script("arguments[0].click();", profile_button)

        self.logger.info("Clicking on 'Sign Out' button.")
        signout_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.signout_button_xpath))
        )
        self.driver.execute_script("arguments[0].click();", signout_button)
        self.logger.info("User signed out successfully.")
