
import os
import unittest
from appium import webdriver
from hamcrest import *
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestLiveStationPlayStation(unittest.TestCase):
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

    def test_live_station_play_station(self):
        # select skip button
        self.driver.find_element_by_id('android:id/button2').click()
        # select ok button to the Settings pop up
        self.driver.find_element_by_id('android:id/button1').click()
        # select Maybe Later
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/login_gate_maybe_later').click()
        # select 2 genres
        self.driver.find_element_by_xpath(" //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
        self.driver.find_element_by_xpath(" //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[5]/android.widget.ImageView[1]").click()
        #tap Done
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/done_btn').click()

        self.driver.find_element_by_name("Navigate up").click()

        time.sleep(3)

        #live radio
        self.driver.find_element_by_xpath(" //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[3]/android.widget.TextView[1]").click()

        #select top left radio station
        self.driver.find_element_by_xpath(" //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()

        # verify elements exist
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_thumbup')
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_thumbdown')
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/player_play_pause_buffer')





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLiveStationPlayStation)
    unittest.TextTestRunner(verbosity=2).run(suite)
