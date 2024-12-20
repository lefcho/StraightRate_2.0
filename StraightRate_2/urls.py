from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('StraightRate_2.common.urls')),
    path('media/', include('StraightRate_2.media.urls')),
    path('accounts/', include('StraightRate_2.accounts.urls')),
    path('reviews/', include('StraightRate_2.reviews.urls')),
    path('', include('StraightRate_2.creators.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
