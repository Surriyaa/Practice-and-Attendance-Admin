from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def open_page(self, url):
        """Open the given URL."""
        self.driver.get(url)

    def handle_wait(self, driver=None):
        """Wait for Google sign-in button and click."""
        if driver is None:
            driver = self.driver

        wait = WebDriverWait(driver, 15)  # Changed to 15 seconds
        sign_in_button = wait.until(
            EC.presence_of_element_located((By.XPATH, self.sign_login_xpath))
        )
        sign_in_button.click()

    def enter_email(self, email):
        """Enter email in Google sign-in popup."""
        email_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.email_xpath))
        )
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        """Enter password in Google sign-in popup."""
        wait = WebDriverWait(self.driver, 15)  # Changed to 15 seconds
        password_input = wait.until(EC.element_to_be_clickable((By.XPATH, self.password_name)))
        password_input.clear()
        password_input.send_keys(password + Keys.TAB)

    def click_Next(self):
        """Click the Next button in Google login flow."""
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.next_button_xpath))
        ).click()

    def click_logout(self):
        wait = WebDriverWait(self.driver, 15)  # Changed to 15 seconds

        # Try closing overlay if any
        try:
            overlay = self.driver.find_element(By.XPATH, "//div[contains(@class,'fixed') and contains(@class,'z-50')]")
            self.driver.execute_script("arguments[0].style.display='none';", overlay)  # Hide overlay forcibly
        except:
            pass  # Overlay not present, continue

        # Click profile icon safely using parent button
        profile_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@data-testid='AccountCircleIcon']/parent::button"))
        )
        self.driver.execute_script("arguments[0].click();", profile_button)

        # Click sign out button
        signout_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.signout_button_xpath))
        )
        self.driver.execute_script("arguments[0].click();", signout_button)
