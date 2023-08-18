from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('builder.urls',namespace="builder")),
    path('auth/', include('authentication.urls',namespace="authentication")),
]
