import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUrls(unittest.TestCase):
    def test_url1(self):
        url1 = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(url1)
        element=browser.find_element(By.XPATH, "//div[contains(@class,'first_block')]//input[contains(@class, 'form-control first')]")
        element.send_keys("Test")
        element2 = browser.find_element(By.XPATH, "//div[contains(@class,'first_block')]//input[contains(@class, 'form-control second')]")
        element2.send_keys("Test")
        element3 = browser.find_element(By.XPATH, "//div[contains(@class,'first_block')]//input[contains(@class, 'form-control third')]")
        element3.send_keys("Test")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        message="Congratulations! You have successfully registered!"
        print(message)
        self.assertEqual(message, welcome_text)
        browser.quit()

    def test_url2(self):
        url2 = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(url2)
        element=browser.find_element(By.XPATH, "//div[contains(@class,'first_block')]//input[contains(@class, 'form-control first')]")
        element.send_keys("Test")
        element2 = browser.find_element(By.XPATH, "//div[contains(@class,'first_block')]//input[contains(@class, 'form-control second')]")
        element2.send_keys("Test")
        element3 = browser.find_element(By.XPATH, "//div[contains(@class,'first_block')]//input[contains(@class, 'form-control third')]")
        element3.send_keys("Test")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        message = "Congratulations! You have successfully registered!"
        welcome_text = welcome_text_elt.text
        self.assertEqual(message, welcome_text)
        browser.quit()

if __name__ == "__main__":
    unittest.main()