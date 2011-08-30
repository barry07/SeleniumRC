form page import Page

class FreelancerBasePage(Page):
    
    _login_locator = ""
    _register_locator = ""

    def click_login(self):
	self.selenium.click(_login_locator)
	self.selenium.wait_for_page_to_load("3000")


	
