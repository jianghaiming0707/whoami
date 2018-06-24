from django.conf.urls import url
from teach04 import views

urlpatterns = [
    url(r'^add-language$',views.language_view),
    url(r'^language-v2',views.language_v2_view),
    url(r'all-lang$',views.get_langes_view,name="zhangsan"),
    url(r'^index$',views.index)
]