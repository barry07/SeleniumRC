from selenium import selenium

import unittest
import time
import re

class Page(object)

	def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://www.freelancer.com.au/")
        self.selenium.start()


