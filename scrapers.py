import os, time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By


class ScrapedDataHolder():
    """
    Class used as data container for scraped data directly from web page
    """
    def __init__(self):
        self.fulltext = []
        self.flat_size_rooms = []
        self.flat_size_m = []
        self.address = []
        self.city = []
        self.czech_part = []
        self.price = []
        self.extra_price = []
        self.link = []
        self.web_page = []
        self.date = []

    def get_dictionary(self):
        dictionary = {'address: ': self.address,
                      'price: ': self.price,
                      'energy': self.extra_price,
                      'rooms': self.flat_size_rooms,
                      'size': self.flat_size_m,
                      'link': self.link,
                      'date': self.date,
                      'web_page': self.web_page}
        return dictionary
    
    def get_extended_dictionary(self):
        extra_dictionary = {'fulltext', self.fulltext,
                            'city', self.city,
                            'czech_part', self.czech_part}
        return {**extra_dictionary, **self.get_dictionary()}
    
    def get_dataframe(self):
        return pd.DataFrame(self.getDictionary())
    def get_extended_dataframe(self):
        return pd.DataFrame(self.getDictionary())
    
class MyScraper:
    """
    General scrapper class containing all common properties
    """
    def __init__(self, *args, **kwargs):
        """
        ## Initialize General webscraper, main properties are:
         - web_page_name   - Name of scraped page - just for info, not requiierd
         - web_page_link   - Contains link to scraped page
         - browser         - Used browser Firefox
         - IS_SILENT       - ONLY FOR FIREFOX, mode with invisible window
        """
        #Default values
        self.web_page_name = ''
        self.web_page_link = ''
        self.browser = 'Firefox'
        self.IS_SILENT = 1
        
        #Update passed properties
        self.__dict__.update(kwargs)
        
        #Initialize driver 
        self.initDriver()
    def initDriver(self):
        """Method for webdriver inicialization \n
        Set ups browser
        """
        
        #Firefox browser is choosen
        if self.browser == 'Firefox':
            #Silent mode is choosen
            if self.IS_SILENT:
                print('Silent mode activated')
                os.environ['MOZ_HEADLESS'] = '1'
            else:
                os.unsetenv('MOZ_HEADLESS')
            print('Openning browser')
            #Initialize driver
            self.driver = webdriver.Firefox()
            print('Maximalizing')
            #Maximalize window
            self.driver.maximize_window()
        else:
            #If selected driwer is not supported, error is thrown
            raise Exception('Uknown web driver')
        
        #If driver is initialized, go to web page:
        self.driver.get(self.web_page_link)
        
class BezrealitkyScraper(MyScraper):
    """
    Class for webscraping Bezrealitky.cz
    """
    def __init__(self, *args, IS_SILENT=1, browser = 'Firefox', **kwargs):
        """
        ## Create a instance of Bezrealitky scraper, input variables are: \n
         - web_page_link = url
         - IS_SILENT = 0 / 1
         - browser = 'Firefox' / 'Chrome' 
        """
        if not 'web_page_link' in kwargs:
            raise ValueError("No URL was specified in 'web_page_link' variable")
        #Constructor for Bezrealitky.cz scraping
        super().__init__(
            web_page_name = 'Bez realitky',
            web_page_link = kwargs['web_page_link'],
            browser = browser,
            IS_SILENT = IS_SILENT)
        
        self.scraped_data = ScrapedDataHolder()
        #Constant private properties      
        self.init_constant_properties()
        
        #Click on cookie button
        self.click_cookie_button()
        
        self.full_scrape_cycle() 
    def full_scrape_cycle(self):
        """
        Run this to scrape all pages
        """
        page = 1
        print('Scraping started')
        while True:
            try:
                print("Scraping page ", page)
                self.extract_data_from_page()
                self.next_page_button_click()
                time.sleep(3)
                page += 1
            except ElementNotInteractableException:
                break
            except NoSuchElementException:
                break    
    def click_cookie_button(self):
        #Tries to click on cookie button, if no such button exists, waits 1 sec and tries again
        counter = 0
        while True:
            try:
                print('Clicking Cookie button')
                self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
                print('Cookie Button successfully clicked')
                break
            except ElementNotInteractableException:
                #No clickable button found
                time.sleep(1)
                counter+=1
            except NoSuchElementException:
                #No button found
                time.sleep(1)
                counter+=1
            if counter >10:
                raise Exception('Cookie button not found')
                break
    def init_constant_properties(self):
        #Xpaths for data of interest
        self._articles_xpath = '/html/body/div[3]/main/section/div/div[2]/div/div[5]/section'
        self._author_name_xpath = 'div[2]/h2/a/span[2]'
        self._flat_size_rooms_xpath = 'div[2]/ul/li[1]'
        self._flat_size_m_xpath = 'div[2]/ul/li[2]'
        self._extra_info_xpath = 'div[2]/p'
        self._price_xpath = 'div[2]/div/span[1]'
        self._extra_price_xpath = 'div[2]/div/span[2]'
        self._link_xpath = 'div[2]/h2/a'
        self._next_page_xpath = 'html/body/div[3]/main/section/div/div[2]/div/div[5]/section/ul/li[3]/a'
    def extract_data_from_page(self):
        #Extract all data from articles found on page
        articles_box = self.driver.find_elements(By.XPATH, self._articles_xpath)
        articles = articles_box[0].find_elements(By.XPATH, 'article')
        for article in articles:
            author_city_czech_part = article.find_element(By.XPATH, self._author_name_xpath).text.rsplit(',')
            self.scraped_data.fulltext.append(article.text)
            self.scraped_data.flat_size_rooms.append(article.find_element(By.XPATH, self._flat_size_rooms_xpath).text)
            self.scraped_data.flat_size_m.append(article.find_element(By.XPATH, self._flat_size_m_xpath).text)
            self.scraped_data.address.append(author_city_czech_part[0]) 
            self.scraped_data.city.append(author_city_czech_part[1])
            self.scraped_data.czech_part.append(author_city_czech_part[2])
            self.scraped_data.price.append(article.find_element(By.XPATH, self._price_xpath).text)
            self.scraped_data.link.append(article.find_element(By.XPATH, self._link_xpath).get_attribute('href'))
            self.scraped_data.web_page.append(self.web_page_name)
            self.scraped_data.date.append()
            try:
                self.scraped_data.extra_price.append(article.find_element(By.XPATH, self._extra_price_xpath).text)
            except NoSuchElementException:
                self.scraped_data.extra_price.append('Not specified')
    def next_page_button_click(self):
        #Clicks on next page button
        self.scroll_down()
        time.sleep(0.5) #pause 0.5 s is required
        print('New page button clicked')
        self.driver.find_element(By.XPATH, self._next_page_xpath).click()
    def scroll_down(self):
        #Scroll the page down
        print('Scrolling down')
        self.driver.execute_script("window.scrollTo(0, 10000)")
        
        
if __name__ =='__main__':        
    url = 'https://www.bezrealitky.cz/vyhledat?offerType=PRONAJEM&estateType=BYT&disposition=DISP_2_KK&disposition=DISP_2_1&disposition=DISP_3_KK&disposition=DISP_3_1&priceTo=15000&surfaceFrom=40&regionOsmIds=R438344&osm_value=Plze%C5%88%2C+okres+Plze%C5%88-m%C4%9Bsto%2C+Plze%C5%88sk%C3%BD+kraj%2C+Jihoz%C3%A1pad%2C+%C4%8Cesko#lat=49.74172501797827&lng=13.371914800000013&zoom=11.95907496555022'    
    br = BezrealitkyScraper(web_page_link = url, IS_SILENT=1)