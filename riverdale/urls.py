from django.conf import settings
from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static



urlpatterns=[
    path('',views.home, name='home'),
    path('logout/', views.logout, name="logout"),
    path('phase/<id>',views.phase, name='phase'),
    path('editprofile',views.editprofile, name='editprofile'),
    path('profile/<id>',views.profile, name='profile'),
    path('search/',views.search, name='search'),
    path('register/',views.register, name='register'),
    path('login/',views.loginpage, name='login'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)