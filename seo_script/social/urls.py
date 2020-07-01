from django.urls import path

from .views import BusinessAPI,  ListingPresenceFacebook, ListingPresenceTwitter, FacebookLikes

urlpatterns = [
    path('business/', BusinessAPI.as_view(),  name='business'),
    path('listing/presence/facebook/', ListingPresenceFacebook.as_view(), name='listing_presence_facebook'),
    path('listing/presence/twitter/', ListingPresenceTwitter.as_view(), name='listing_presence_twitter'),
    path('facebook-likes/', FacebookLikes.as_view(), name='facebook_likes'),
]
