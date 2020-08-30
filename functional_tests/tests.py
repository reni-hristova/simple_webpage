from    selenium                        import webdriver
from    selenium.common.exceptions      import WebDriverException
from    selenium.webdriver.common.keys  import Keys
from    django.test                     import LiveServerTestCase, TestCase, Client
import  unittest
import  time

HOMEPAGE = 'http://127.0.0.1:8000/'

class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_website_using_navigation(self):
        # Alex opens the website and sees the homepage.
        self.browser.get(HOMEPAGE)
        time.sleep(1)

        # Then he clicks on the 'Blog' tab in the navigation menu.
        original_window = self.browser.current_window_handle
        self.browser.find_element_by_id("navBlog").click()
        time.sleep(1)

        # He is redirected to Rennie's blog.
        current_url = self.browser.current_url
        expected_url = HOMEPAGE + 'blog/'
        self.assertEquals(current_url, expected_url)

        # He sees a list of blog posts.
        try:
            self.browser.find_element_by_class_name("post")
        except (WebDriverException) as e:
            raise e

        # Then, he decides to navigates to Rennie's CV using the navigation menu.
        self.browser.get(HOMEPAGE)
        self.browser.find_element_by_id("navCV").click()
        time.sleep(1)

        current_url = self.browser.current_url
        expected_url = HOMEPAGE + 'cv/'
        self.assertEquals(current_url, expected_url)

        # Alex sees Rennie's CV.
        # He notices that Rennie has put her contact information.
        try:
            self.browser.find_element_by_class_name("contactDetails")
        except (WebDriverException) as e:
            raise e

        # He takes a quick look over Rennie's CV.
        try:
            self.browser.find_element_by_class_name("entry")
        except (WebDriverException) as e:
            raise e

        # Alex can't add posts or edit Rennie's CV.
        # Alex leaves Rennie's site

if __name__ == '__main__':
    unittest.main(warnings='ignore')
