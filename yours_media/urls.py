from django.contrib import admin
from django.urls import path
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login',views.loginPage),
    path('register',views.register),
    path('profile',views.profile),
    path('logout',views.userLogOut),
    path('profile-upload',views.profileUpload),
    path('profile-delete',views.profileDelete),
    path('fetch_posts/', views.fetch_posts, name='fetch_posts'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)