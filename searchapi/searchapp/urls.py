from django.conf.urls import url
from searchapp import views

urlpatterns = [
    url(r'^searches/$', views.search_list),
]
