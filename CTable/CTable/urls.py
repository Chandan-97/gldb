from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('main.urls')),
    path('', include('home.urls')),
    # path('login/', auth_views.LoginView.as_view()),
    # path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
]
