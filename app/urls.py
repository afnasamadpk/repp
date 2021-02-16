"""project_4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from app.views import home,add_image,like_post,log_in,log_out,register

urlpatterns = [
    path('',home,name='home'),
    path('addimage/',add_image,name='add_image'),
    path('likes/<int:id>/',like_post,name='like_post'),
    path('login/',log_in,name = 'log_in'),
    path('logout/',log_out,name='log_out'),
    path('register/',register,name='register')

]
