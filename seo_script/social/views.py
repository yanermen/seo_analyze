import os
import re
import sys

import requests
import selenium

from bs4 import BeautifulSoup
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from selenium import webdriver

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
    Count fb likes
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
        return Response({'facebook people likes': ls[0].split()[1]})






