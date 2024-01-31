
from django.contrib import admin
from django.urls import path
from app.views import employeelistview,userlistview,employeeDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees', employeelistview ),
    path('api/employees/<int:pk>', employeeDetailView ),
    path('api/users', userlistview )
]
