from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views
from .views import create_post, create_hood, create_business, create_emergency, about, search_results

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('add_post', create_post, name='add_post'),
    path('add_hood', create_hood, name='add_hood'),
    path('add_biz', create_business, name='add_biz'),
    path('add_emergency', create_emergency, name='add_emergency'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit_profile'),
    path('search/', search_results, name='search_results'),
    path('about', about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
