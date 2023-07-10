from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    
    # HOTELS URLS
    path('api/hotel/', include('hotels.api.urls', 'api_hotel')),
    path('api/hotels/', include('hotels.api.urls', 'api_hotels')),
]



# urlpatterns += [re_path(r'^.*', TemplateView.as_view())]