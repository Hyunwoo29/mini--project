from django.urls import path
from common.views import connection
# from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url, include
from rest_framework import routers
# from member.views import Auth
# from board import views
router = routers.DefaultRouter()
# router.register(r'member', views.MemberViewSet)
# router.register(r'board', views.BoardViewSet)
urlpatterns = [
    path('connection', connection.as_view()),
    path('board', include('board.urls')),
    path('member', include('member.urls')),
    # url(r'^member', Auth.as_view()),
    # # path('admin/', admin.site.urls),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),
    # url(r'^accounts-rest/registration/accunt-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),



]