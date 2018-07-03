import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


def scroll_page(no_of_pagedowns, elem):
    '''
    scrolls down the browser page to get more linkg
    :param no_of_pagedowns: the number of pages you want to scroll
    :param elem: the element that contains the scroll idk
    :return:
    '''
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        no_of_pagedowns-=1


def get_urls_list(browser):
    '''
    finds the wanted links in the browser
    :param browser: the browser object
    :return: the list of urls of the questions
    '''
    list = []
    post_elems = browser.find_elements_by_class_name("question_link")
    for post in post_elems:
        list.append(post.get_attribute('href'))
    return list


def main(topic):
    '''
    main function calls all the other functions and prints the output
    :param topic: the topic in quora
    '''
    driverLocation = '/home/downey/Desktop/chromedriver_linux64/chromedriver'
    browser = webdriver.Chrome(driverLocation)

    browser.get("https://www.quora.com/topic/"+topic+ "/all_questions")
    time.sleep(1)

    scroll_page(2, browser.find_element_by_tag_name("body"))

    urls = get_urls_list(browser)
    print(urls)

# can be run from the command line
main(str('Experiences-in-Life'))