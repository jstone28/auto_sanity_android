
import os
import unittest
from appium import webdriver
from hamcrest import *
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestGenreGameStartUpFlow(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '/Users/1111096/workspace/android-flagship/iHeartRadio/gradle-build/outputs/apk/iHeartRadio-Google-Mobile-AMPProd-debug.apk'
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_genre_game_start_up_flow(self):
        # select skip button
        self.driver.find_element_by_id('android:id/button2').click()
        # select ok button to the Settings pop up
        self.driver.find_element_by_id('android:id/button1').click()
        self.driver.find_element_by_name('Sign Up').click()
        reg_time = str(time.time())
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email').send_keys(reg_time + 'jameson@iheartmedia.com')
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/password').send_keys('things')
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/zipcode').send_keys('11215')
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Spinner[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.TextView[19]").click()
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/male').click()
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/tos').click()
        # submit form
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/sign_up').click()
        time.sleep(3)
        # select 2 genres
        self.driver.find_element_by_xpath(" //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
        self.driver.find_element_by_xpath(" //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[5]/android.widget.ImageView[1]").click()
        #tap Done
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/done_btn').click()






if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGenreGameStartUpFlow)
    unittest.TextTestRunner(verbosity=2).run(suite)
