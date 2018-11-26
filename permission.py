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
    driver=webdriver.Chrome()
    driver.maximize_window()
    @classmethod
    def setUpClass(cls):
    
        #设置超时时间
        cls.driver.implicitly_wait(30)
        
    #每执行完一遍，清除一次cookie
    def tearDown(self):
        file.write('------------------------------------'+'\n')
        self.driver.delete_all_cookies()
    @data(*parse('E:/测试数据/CSM/CSM_Account_List_01112018.csv'))
    @unpack
    def test_a(self,email,passwd):
        driver=self.driver
        driver.get('https://csm.bestwaycorp.com/Login/Transit')
        driver.find_element_by_class_name('Non-employee').click()
        driver.find_element_by_id('account').send_keys(email)
        driver.find_element_by_id('pwd').send_keys(passwd)
        driver.find_element_by_xpath('/html/body/div/div/form/button').submit()
        driver.find_element_by_id('liMenu_1036').click()
        global file      
        file=open('E:\\scripts\\csm\\country.txt','a+',encoding='utf-8')
        #获取登录名
        country=driver.find_element_by_xpath('//*[@id="side-menu"]/li[1]/div/a/span/span')
        file.write(country.text+'\n')
        #获取工作台table内容
        time.sleep(3)
        file.write('获取工作台内容：'+'\n')
        dash=driver.find_element_by_id('example')
        file.write(dash.text+'\n')
        file.write('退款的国家选项：'+'\n')
        #获取退款的国家选项
        driver.find_element_by_id('liMenu_1051').click()
        driver.find_element_by_id('searchCountry_chosen').click()
        re_country=driver.find_element_by_xpath('//*[@id="searchCountry_chosen"]/div/ul')
        file.write(re_country.text+'\n')
        # file.write('上海发货信息的大区：'+'\n')
        #获取上海发货信息的国家和售后服务中心
        driver.find_element_by_id('liMenu_1040').click()
        driver.find_element_by_id('liSecondMenuId_1041').click()
        driver.find_element_by_xpath('//*[@id="txtParent_chosen"]').click()
        # region=driver.find_element_by_xpath('//*[@id="txtParent_chosen"]/div/ul')
        # file.write(region.text+'\n')
        file.write('上海发货信息的国家：'+'\n')
        driver.find_element_by_id('txtCountry_chosen').click()
        co_ship=driver.find_element_by_xpath('//*[@id="txtCountry_chosen"]/div/ul')
        file.write(co_ship.text+'\n')
        file.write('上海发货信息的售后服务中心：'+'\n')
        driver.find_element_by_id('txtServiceCenter_chosen').click()
        cs_code=driver.find_element_by_xpath('//*[@id="txtServiceCenter_chosen"]/div/ul')
        file.write(cs_code.text+'\n')
        #获取库存查询的国家筛选
        driver.find_element_by_id('liSecondMenuId_13').click()
        driver.find_element_by_xpath('//*[@id="txtCountry_chosen"]').click()
        ku_country=driver.find_element_by_xpath('//*[@id="txtCountry_chosen"]/div/ul')
        file.write('库存国家：'+'\n')
        file.write(ku_country.text+'\n')
        #获取上传文件的国家
        driver.find_element_by_id('liMenu_1017').click()
        driver.find_element_by_id('txtFormType_chosen').click()
        driver.find_element_by_xpath('//*[@id="txtFormType_chosen"]/div/ul/li[1]').click()
        driver.find_element_by_id('txtServiceCenter_chosen').click()
        cs_code_upload=driver.find_element_by_xpath('//*[@id="txtServiceCenter_chosen"]/div/ul/li')
        file.write('获取上传文件的售后服务中心：'+'\n')
        file.write(cs_code_upload.text+'\n')
        #获取投诉记录的国家
        driver.find_element_by_id('liMenu_1056').click()
        driver.find_element_by_id('txtCountry_chosen').click()
        co_quest=driver.find_element_by_xpath('//*[@id="txtCountry_chosen"]/div/ul/li')
        file.write('获取投诉记录的国家：'+'\n')
        file.write(co_quest.text+'\n')
if __name__ == '__main__':
    unittest.main()
    
