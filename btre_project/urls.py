from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from pages.api_views import (
    latest_listings_api, about_realtors_api
)  # Importe as API views

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),

    # --- ROTAS DA API ---
    path('api/realtors/', include('realtors.api_urls')),
    path('api/listings/', include('listings.api_urls')),
    path('api/latest-listings/',
         latest_listings_api, name='latest-listings-api'),
    path('api/about-realtors/', about_realtors_api, name='about-realtors-api'),

    # --- ROTAS DA DOCUMENTAÇÃO SWAGGER ---
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
