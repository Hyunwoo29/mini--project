from common.views import connection
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    path('connection', connection.as_view()),
    url(r'^api/member/', include('member.urls')),
    url(r'^api/post/', include('board.urls')),
    url(r'^adm/member/', include('member.urls')),

]

'''
CBV 방식 (Class Based View)
from django.conf.urls import url
from .views import Members as members
from .views import Member as member
from django.urls import path, include
urlpatterns = [
    url('/register', members.as_view()),
    path('/<int:pk>/', member.as_view()),
]
'''
