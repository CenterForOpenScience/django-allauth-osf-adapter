from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import OSFProvider


urlpatterns = default_urlpatterns(OSFProvider)
