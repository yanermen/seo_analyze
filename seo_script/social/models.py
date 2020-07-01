from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    business = models.CharField(max_length=100)

    def __str__(self):
        return self.business


class SocialNetworkLinksFacebook(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    facebook_link = models.CharField(max_length=100)

    def __str__(self):
        return self.facebook_link


class SocialNetworkLinksTwitter(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    twitter_link = models.CharField(max_length=100)

    def __str__(self):
        return self.twitter_link