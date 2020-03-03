from django.urls import include
from django.urls import path


urlpatterns = [
    path('auth/', include('test_case.auth_api.urls')),
]
