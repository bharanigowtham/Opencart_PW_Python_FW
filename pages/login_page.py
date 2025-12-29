from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page:Page):
        self.page=page
        self.txt_email_address = self.page.locator('#input-email')
        self.txt_password = self.page.locator('#input-password')
        self.btn_login = self.page.locator('input[value="Login"]')
        self.txt_error_message = self.page.locator('.alert.alert-danger.alert-dismissible')


    def enter_email(self, email):
        try:
            self.txt_email_address.fill(email)
        except Exception as e:
            print(f"Exception on entering email: {e}")
            raise

    def enter_password(self,pswd):
        try:
            self.txt_password.fill(pswd)
        except Exception as e:
            print(f"Exception on entering password: {e}")
            raise

    def click_login_btn(self):
        try:
            self.btn_login.click()
        except Exception as e:
            print(f"Exception on login click {e}")

    def get_login_error(self):
        try:
            return self.txt_error_message
        except Exception as e:
            print(f"Exception while retruning error msg = {e}")
            return None



