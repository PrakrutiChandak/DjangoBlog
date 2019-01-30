"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post_list, name = "post_list"),
    path('blog/',include('blog.urls', namespace="blog")),
    path('login', views.user_login, name="user_login"),
    path('logout',views.user_logout,name = "user_logout"),
    path('blog/post_create',views.post_create,name ="post_create"),
    path('blog/edit_profile',views.edit_profile,name ="edit_profile"),
    path('register', views.register, name  = "register"),


    #password reset urls

    # url(r'^password-rest/$',auth_views.password_reset, name="password_reset"),
    # url(r'^password-rest/done/$',auth_views.password_change_done, name="password_reset_done"),
    # url(r'^password-rest/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-])/$',auth_views.password_reset_confirm, name="password_reset_confirm"),
    # url(r'^password-rest/completes/$',auth_views.password_reset_complete, name="password_reset_complete"),



    # path('password-reset/',auth_views.password_reset, name = "password_reset"),
    # path('password-reset/done',auth_views.password_change_done, name = "password_reset_done"),
    # path('password-change/confirm/<uidb64>/<token>', auth_views.password_reset_confirm, name ="password_reset_confirm"),
    # path('password-reset/complete/', auth_views.password_reset_complete, name = "password_reset_complete"),

    url(r'^',include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls', namespace="social")),
    path('like/', views.like_post, name = "like_post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)