"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path, include
from . import views
from .views import Homepage, Register, LoginRequest, LogoutRequest, FilterSeries, FilterTutorials,FilterBlogs

app_name = "main"

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('about/', views.about, name = 'about'),
    path('register/', Register.as_view(), name = 'register'),
    path('logout/', LogoutRequest.as_view(), name = 'logout'),
    path('login/', LoginRequest.as_view(), name = 'login'),
    path("<first_slug>/", FilterSeries.as_view(), name = "first_slug"),
    path("<first_slug>/<slug:second_slug>/", FilterTutorials.as_view(), name = "second_slug"),
    path("<first_slug>/<slug:second_slug>/<slug:third_slug>/", FilterBlogs.as_view(), name = "third_slug")
]

# category/<slug>
# tutorialsSeries/
# tutorialsSeries/<slug>
# Wassaf Shahzad3:48 PM
# tutorials/car.slug
# RestApisCHEMA
# Wassaf Shahzad3:50 PM
# tutorial-series/python