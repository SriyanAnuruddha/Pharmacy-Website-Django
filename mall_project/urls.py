from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views  # django login

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pharmacy_site.urls')),
    path('pharmacy/', include('pharmacy_site.urls')),
    path('register/', user_views.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='user-login'),  # change default login template path
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='user-logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
