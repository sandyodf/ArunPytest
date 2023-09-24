import pytest
from selenium import webdriver


@pytest.mark.usefixtures("setupbrowser")
class TestWebsites:

    def test_fan_code_chrome(self):
        print("fb")
        self.driver.get("https://www.fancode.com/")
        # assert self.driver.title == "Watch Live Cricket Streaming, Live Scores, Highlights " \
        assert self.driver.title == "hi"
        fancode_screenshot = self.driver.get_screenshot_as_png()

        # Save the screenshot to a file
        with open("fancode_screenshot.png", "wb") as file:
            file.write(fancode_screenshot)

    def test_gmail_chrome(self):
        self.driver.get("https://www.google.com/gmail/about/")
        assert self.driver.title == "Gmail: Private and secure email at no cost | Google Workspacee"
        gmail_screenshot = self.driver.get_screenshot_as_png()
        # Save the screenshot to a file
        with open("gmail_screenshot.png", "wb") as file:
            file.write(gmail_screenshot)

    def test_fb_chrome(self):
        self.driver.get("https://www.facebook.com/")
        assert self.driver.title == "Facebook – log in or sign upe"
        fb_screenshot = self.driver.get_screenshot_as_png()

        # Save the screenshot to a file
        with open("fb_screenshot.png", "wb") as file:
            file.write(fb_screenshot)

    def test_insta_chrome(self):
        self.driver.get("https://www.instagram.com/")
        assert self.driver.title == "Instagrame"
        insta_screenshot = self.driver.get_screenshot_as_png()

        # Save the screenshot to a file
        with open("insta_screenshot.png", "wb") as file:
            file.write(insta_screenshot)

    def test_BMS_chrome(self):
        self.driver.get("https://in.bookmyshow.com/explore/home/hyderabad")
        # assert driver.title == "Movie Tickets, Plays, Sports, Events &amp; Cinemas near Hyderabad - BookMyShow"
        BMS_screenshot = self.driver.get_screenshot_as_png()
        # Save the screenshot to a file
        with open("BMS_screenshot.png", "wb") as file:
            file.write(BMS_screenshot)
