import sys
sys.path.append('E:\\scripts')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from ddt import ddt,data,unpack,file_data
from parse_csv import parse
import time
@ddt
class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        #设置超时时间
        cls.driver.implicitly_wait(30)
    #每执行完一遍，清除一次cookie
    def tearDown(self):
        print(product_all)
        self.driver.delete_all_cookies()
    @data(*parse('E:/测试数据/CSM/CSM_Account_List_01112018.csv'))
    @unpack
    def test_login(self,email,passwd):
        global product_all
        product_all=[]
        self.driver.get('https://csm.bestwaycorp.com/Login/Transit')
        self.driver.find_element_by_class_name('Non-employee').click()
        self.driver.find_element_by_id('account').send_keys(email)
        self.driver.find_element_by_id('pwd').send_keys(passwd)
        self.driver.find_element_by_xpath('/html/body/div/div/form/button').submit()
        self.driver.find_element_by_id('liMenu_1036').click()
        #获取国家
        country=self.driver.find_element_by_xpath('//*[@id="side-menu"]/li[1]/div/a/span/span/strong').text
        product_all.append(country)
        #查看产品
        self.driver.find_element_by_id('liSecondMenuId_1039').click()
        time.sleep(8)
        #获取产品数据量
        product_num=self.driver.find_element_by_xpath('//*[@id="allCount"]').text
        product_all.append(product_num)
        #查看bom
        self.driver.find_element_by_id('liSecondMenuId_1037').click()
        time.sleep(8)
        bom=self.driver.find_element_by_id('allCount').text
        product_all.append(bom)
if __name__ == '__main__':
    unittest.main()
    