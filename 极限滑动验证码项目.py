from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# 初始化
EMAIL = '15981981193@163.com'
PASSWORD = 'G1308310285'

class CrackGeetest():
    def __init__(self):
        """基本初始化"""
        self.url = 'https://auth.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)
        self.email = EMAIL
        self.passwrod = PASSWORD


    # 模拟点击初始的验证按钮
    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return: 按钮对象
        """
        button = self.wait.until( # 获取按钮
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'geetest_radar_tip')))
        button.click()

       # 识别缺口
    def get_postion(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'geetest_canvas_img')))
        time.sleep(2)
        location = img.location   # 获取验证码图片位置
        size = img.size   # 获取验证码图片尺寸
        top, bottom, left, right = location['y'], location['y']+ size['height'], \
                                   location['x'], location['x']+ size['width']
        return (top, bottom, left, right) # 返回验证码图片坐标
    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片(获取坐标位置网页截图)
        :return: 图片对象
        """
        top, botton, left, right =self.get_postion()
        print('验证码位置',top, botton, left, right )
        screenshot = self.get_screenshot()  # 创建屏幕对象
        captcha = screenshot.crop((left, top,  right, botton)) # 截取图片
        return captcha # 返回图片对象

    # 获取第二张图片,也就是带缺口的图片
    def get_slider(self):
        """
        获取滑块
        :return:滑块对象
        """
        slider = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'geetest_slider_button')))
        return slider # 返回滑块对象

    slider = self.get_slider()
    slider.click()  # 点击滑块



    # 像素对比算法模块
    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置 x
        :param y: 位置 y
        :return: 像素是否相同
        """
        # 获取两个图片的像素点
        pix1 = image1.load()[x, y]
        pix2 = image2.load()[x, y]
        threshold = 60
        if abs(pix1[0] - pix2[0]) < threshold and\
                abs(pix1[1] - pix2[1]) < threshold and\
                abs(pix1[2] - pix2) < threshold:
            return True
        else:
            return False


   # 缺口位置确定模块
    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param imag1:不带缺口的图片
        :param image2: 带缺口的图片
        :return:
        """
        left = 60 # 从滑块的右边开始比对,偏移60
        for i in range(left, image1.size[0]): # X轴偏移60,从第60列开始对比
            for j in range(image1.size[1]):   # 两个for循环构成<列扫描>
                if not self.is_pixel_equal(image1, image2, i, j): # 调用像素对比算法
                    left = i  # 确定x=i所对应的列为缺口边沿
                    return left
        return left


    # 模拟拖动
    def get_tarck(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []

        # 当前位置
        current = 0

        # 减速阈值
        mid = distance*(4/5)
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为2
                a = 2
            else:
                # 加速度为-3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度 v =v0 + at
            v = v0 + a*t
            # 移动距离 x = v0t + 1/2*a*t*t
            move = v0*t +1/2*a*t*t
            # 当前位移
            current += move

            # 加入轨迹
            track.append(round(move)) # track记录了每个时间间隔移动了多少位移
        return track # 返回完整轨迹

    # 拖动
    def move_gap(self, slider, tracks):
        """
        拖动滑块到缺口处
        :param slider:滑块
        :param tracks: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

