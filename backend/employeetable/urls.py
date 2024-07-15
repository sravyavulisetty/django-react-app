# employeetable/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeView

router = DefaultRouter()
router.register(r'employees', EmployeeView, basename='employee')

urlpatterns = [
    path('api/', include(router.urls)),
]

