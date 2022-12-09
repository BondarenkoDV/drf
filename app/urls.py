from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
app_name = 'app'

urlpatterns = [
    path('api/token/tickets_list/', TicketsAPIView.as_view(), name='tickets_list'),
    path('api/token/tickets_list/<int:pk>', TicketAPIUpdate.as_view(), name='tickets_list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
