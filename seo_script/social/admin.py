from django.contrib import admin

from .models import Business, SocialNetworkLinksFacebook, SocialNetworkLinksTwitter

admin.site.register(Business)
admin.site.register(SocialNetworkLinksFacebook)
admin.site.register(SocialNetworkLinksTwitter)
