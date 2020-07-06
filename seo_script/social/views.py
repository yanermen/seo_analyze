import re

import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from urllib.request import urlopen

from bs4 import BeautifulSoup
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Business, SocialNetworkLinksFacebook, SocialNetworkLinksTwitter
from .serializers import BusinessModelSeriializer


class BusinessAPI(generics.ListCreateAPIView):
    """
    Add business in DB
    """
    serializer_class = BusinessModelSeriializer


class ListingPresenceFacebook(APIView):
    """
    Find the facebook links in website
    """
    def get(self, request):
        business_name = Business.objects.all().order_by('-id')[0]
        business_link = business_name.business
        url = f'{business_link}'
        page = requests.get(url)
        soup = BeautifulSoup(page.text)
        for link in soup.findAll('a', attrs={'href': re.compile("^https://www.facebook.com/\w+")}):
            href = link.get('href')
            if href:
                facebook_link = SocialNetworkLinksFacebook.objects.create(business=business_name, facebook_link=href)
                return Response({'facebook': 1})
            else:
                return Response({'facebook': 0})


class ListingPresenceTwitter(APIView):
    """
       Find the twitter links in website
    """
    def get(self, request):
        business_name = Business.objects.all().order_by('-id')[0]
        business_link = business_name.business
        url = f'{business_link}'
        page = requests.get(url)
        soup = BeautifulSoup(page.text)
        for link in soup.findAll('a', attrs={'href': re.compile("^https://twitter.com/\w+")}):
            href = link.get('href')
            if href:
                twitter_link = SocialNetworkLinksTwitter.objects.create(business=business_name, twitter_link=href)
                return Response({'twitter': 1})
            else:
                return Response({'twitter': 0})


class FacebookLikes(APIView):
    """
    Number of facebook likes
    """

    def get(self, request):
        fb_link = SocialNetworkLinksFacebook.objects.all().order_by('-id')[0]
        link_facebook = fb_link.facebook_link
        page = requests.get(link_facebook)
        soup = BeautifulSoup(page.text, 'html.parser')
        ls = list()
        for div in soup.find_all(class_='_4bl9'):
            for childdiv in div.find_all('div'):
                my_str = childdiv.string
                if my_str is not None:
                    ls.append(my_str)

        ls[0] = ls[0].replace('\xa0', '')
        result = ''
        for char in ls[0]:
            if char.isdigit():
                result += char
        return Response({'facebook people likes': result})



class Twitter_followers(APIView):
    """
    Get number of followers
    """
    def get(self, request):
        twit_link = SocialNetworkLinksTwitter.objects.all().order_by('-id')[0]
        link_twitter = twit_link.twitter_link

        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        DRIVER_PATH = './chromedriver'
        driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        driver.get(f"{link_twitter}")
        sleep(3)

        followers = driver.find_element_by_css_selector("a[href='/MercedesBenz/followers']").get_attribute("title")

        sleep(3)
        driver.quit()

        return Response({'twitter followers': f'{followers}'})


class Twitter_following(APIView):
    """
    Get number of following
    """
    def get(self, request):
        twit_link = SocialNetworkLinksTwitter.objects.all().order_by('-id')[0]
        link_twitter = twit_link.twitter_link

        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        DRIVER_PATH = './chromedriver'
        driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        driver.get(f"{link_twitter}")
        sleep(3)

        following = driver.find_element_by_css_selector("a[href='/MercedesBenz/following']").get_attribute("title")

        sleep(3)
        driver.quit()

        return Response({'twitter followers': f'{following}'})

