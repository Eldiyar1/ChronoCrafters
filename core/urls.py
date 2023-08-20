from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.watch.urls import router as watch_router
from .settings.yasg import urlpatterns_swagger as doc_urls
from apps.users.urls import router as users_router

routers = [
    watch_router,
    users_router,
]

router = DefaultRouter()
for rtr in routers:
    router.registry.extend(rtr.registry)

urlpatterns = [path('admin/', admin.site.urls),
               path('api/watches/', include('apps.watch.urls')),
               path('api/users/', include('apps.users.urls')),
               ] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_urls
