# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
import urllib.request


class CelebritiesSpider(scrapy.Spider):
    name = 'celebrities'
    allowed_domains = ['en.wikipedia.org/wiki/']
    start_urls = ['http://en.wikipedia.org/wiki/List_of_Indian_film_actors']

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(executable_path="/home/hemanth/chromedriver_linux64/chromedriver",options=chrome_options)

    celeb_names=[]
    celeb_links = []
    celeb_img = []
    celeb_age=[]
    celeb_des = []
    celeb_status = []
    celeb_dob=[]

    def parse(self, response):
        origin_link="https://en.wikipedia.org"
        alphas = response.xpath("//div[@class='div-col columns column-width']/ul/li")
        for alpha in alphas:
            name = alpha.xpath(".//a/text()").get()
            link = alpha.xpath(".//a/@href").get()
            link = origin_link + link
            self.celeb_names.append(name)
            self.celeb_links.append(link)

        actress_page = self.driver.get("https://en.wikipedia.org/wiki/List_of_Indian_film_actresses")
        pg_src = self.driver.page_source
        res = Selector(text=pg_src)
        alphas_actress = res.xpath(".//div[@class='div-col columns column-width']/ul/li")
        for alpha in alphas_actress:
            name = alpha.xpath(".//a/text()").get()
            link = alpha.xpath(".//a/@href").get()
            self.celeb_names.append(name)
            self.celeb_links.append(link)

        count = 0
        for actor in self.celeb_names:
            self.driver.get("https://www.google.com/")
            search_box = self.driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
            search = str(actor) + " age"
            self.driver.implicitly_wait(5)
            search_box.send_keys(search)
            search_box.send_keys(Keys.ENTER)
            self.driver.implicitly_wait(5)
            html = self.driver.page_source
            resp = Selector(text=html)
            age = resp.xpath(".//div[@class='Z0LcW']/text()").get()
            if age:
                age = age.replace("\xa0",' ').split()[0]
            dob = resp.xpath("(.//span[@class='LrzXr kno-fv'])[1]/text()").get()
            if dob:
                dob = dob.split('(')[0].strip()
            img = resp.xpath(".//g-img/img/@src").get()
            desc_table = resp.xpath(".//div[@jscontroller='DGEKAc']").getall()
            leng = len(desc_table)
            desc = resp.xpath("(.//div[@jscontroller='DGEKAc'])[" + str(leng) + "]/div/span/text()").get()
            person = resp.xpath("(.//span[@class='w8qArf'])[2]/a/text()").get()
            if(person != 'Died'):
                person = 'Alive'
            link = self.celeb_links[count]
            self.celeb_age.append(age)
            self.celeb_dob.append(dob)
            self.celeb_des.append(desc)
            self.celeb_status.append(person)
            filename = str(actor) + ".jpg"
            if(img):
#                urllib.request.urlretrieve(str(img),"/home/hemanth/Desktop/6th sem/Web_Scrapping/Photos/"+ str(actor) + ".jpg")
                self.celeb_img.append(filename)
            else:
                filename = "NA",
                self.celeb_img.append(filename)

        # self.driver.close()
            count += 1
            yield {
                'Name':actor,
                'Link':link,
                'Img' : filename,
                'DOB':dob,
                'age(years)':age,
                'status':person,
                'description':desc
            }
