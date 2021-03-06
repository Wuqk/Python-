from PIL import Image
from selenium import webdriver
import os
from aip import AipOcr
import time
import xlrd
"""浏览器自动化,从excel读取数据添加到网站"""
""" 你的 APPID AK SK """
"""百度OCR"""
APP_ID = "your_id"
API_KEY = "your_key"
SECRET_KEY = "your_secret_key"

#创建百度OCR实例
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

"""调用百度OCR识别验证码"""
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def checkAndSub():
    #获取验证码element
    check = driver.find_element_by_class_name("pointer")
    #获取验证码位置
    x1 = check.location.get("x")
    y1 = check.location.get("y")
    #获取验证码大小
    x2 = check.size.get("width")
    y2 = check.size.get("height")
    #截取全屏
    driver.save_screenshot(r"D:/pic.png")
    image = Image.open(r"D:/pic.png")
    #根据验证码的位置和大小从全屏中截取验证码（电脑显示比例为125%所以乘以1.25）
    img = image.crop((1.25*x1,1.25*y1,1.25*(x1+x2),1.25*(y1+y2)))
    img.save("D:/check.png")
    #调用文字识别
    result = client.basicGeneral(get_file_content("D:/check.png"))
    checkcode = result.get("words_result")[0].get("words")
    #输入验证码
    elements[2].send_keys(checkcode)
    driver.find_element_by_tag_name("button").click()

#加载浏览器驱动
driver = webdriver.Chrome(executable_path="D:\GoogleDownload\chromedriver_win322\chromedriver.exe")
#打开网址
driver.get("http://demo.open.renren.io/renren-security/index.html")
#最大化窗口
# driver.maximize_window()
elements = driver.find_elements_by_class_name("form-control")
elements[0].send_keys("admin")
elements[1].send_keys("admin")

def login():
    #识别验证码并填入，然后提交
    checkAndSub()

#获取当登录页面url
url1 = driver.current_url
#登录
login()

#若登录失败则重新登录
while True:
    time.sleep(1)
    search_window = driver.current_window_handle
    #获取当前页面url，若和登录页面一样则代表登录失败，这里的原因是因为验证码错误
    url2 = driver.current_url
    if url1==url2:
        #重新输入验证码登录
        login()
    else:
        break

#到达提交数据页面
time.sleep(1)
search_window = driver.current_window_handle
driver.find_element_by_link_text("系统管理").click()

time.sleep(1)
search_window = driver.current_window_handle
driver.find_element_by_link_text("管理员管理").click()

time.sleep(1)
search_window = driver.current_window_handle
driver.switch_to.frame(0)
driver.find_element_by_partial_link_text("新增").click()

time.sleep(1)
search_window = driver.current_window_handle

#提交数据
def sub(info):
    print(info)
    eles = driver.find_elements_by_xpath("//form//input")
    eles[0].send_keys(info[0]);
    eles[1].click();
    driver.find_element_by_xpath("//div[@id='deptLayer']//a[@title='人人开源集团']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[text()='确定']").click()
    eles[2].send_keys(info[2]);
    eles[3].send_keys(info[3]);
    eles[4].send_keys(str(info[4])[:-2]);
    if(info[5]==0):
        driver.find_elements_by_name("status")[0].click()
    else:
        driver.find_elements_by_name("status")[1].click()
    driver.find_element_by_xpath("//input[@type='button' and @ value='确定']").click()
    time.sleep(3)

#打开excel
web = xlrd.open_workbook(r"D:\Users\Administrator\Desktop\IMAGE\inputexcel\test.xlsx")
#取出对应的Sheet
sheet = web.sheet_by_name("Sheet1")
#按行遍历excel
for a in range(sheet.nrows):
    info = sheet.row_values(a)
    #将excel对应的数据提交到网页
    sub(info)
    time.sleep(3)

