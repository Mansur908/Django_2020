from django.urls import path, re_path

from users import views
from users.views import signin, signup, profile, message, exit

urlpatterns = [
    re_path(r'^signin',signin),
    path('signup/',signup),
    path('profile/',profile),
    path('message/',message),
    path('news/',views.NewsView.as_view()),
    path('airtickets/',views.AirTicketsView.as_view()),
    path('hotels/',views.HotelsView.as_view()),
    path('restaurants/',views.RestaurantsView.as_view()),
    path('cars/',views.CarsView.as_view()),
    path('attractions/',views.AttractionsView.as_view()),
    path('main/',views.MainPageView.as_view()),
    path('exit/',exit),
]