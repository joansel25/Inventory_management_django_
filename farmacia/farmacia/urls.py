from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT LOGIN
    path('farmacia/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('farmacia/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rutas de la app farmacia
    path('farmacia/', include('apps.task.urls')),
]
