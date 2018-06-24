from django.conf.urls import url
from teach04 import apis_v1 as api


urlpatterns = [
    url(r'^add-language$',api.add_language_api)
]
