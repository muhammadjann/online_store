
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('market.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),

]
