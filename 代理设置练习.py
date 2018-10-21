from selenium import webdriver
import requests
import pyspider
import aiohttp
from flask import Flask
proxy_pool = 'http://localhost:5555/random'
def get_proxy():
    try:
        req = requests.get(proxy_pool)
        if req.status_code == 200:
            return req.text
    except requests.RequestException:
        print(None)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+ get_proxy())
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')
