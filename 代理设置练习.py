from selenium import webdriver
import aiohttp
from flask import Flask
proxy = '94.242.59.135:10010'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+ proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')
