"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from my_app.views import (BookCreate,
                          AuthorCreatePopup,
                          AuthorEditPopup,
                          get_author_id)

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book/$', TemplateView.as_view(template_name="book.html")),


    url(r'^book/create', BookCreate, name = "BookCreate"),
    url(r'^author/create', AuthorCreatePopup, name = "AuthorCreate"),
    url(r'^author/(?P<pk>\d+)/edit', AuthorEditPopup, name = "AuthorEdit"),
    url(r'^author/ajax/get_author_id', get_author_id, name = "get_author_id"),
    url(r'', TemplateView.as_view(template_name="home.html")),

]
