from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from market import views
from .views import index, contact
from .forms import LoginForm
app_name = 'market'
urlpatterns = [
    path('', views.index, name='index'),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('contact/', views.contact, name='contact'),
    path('singup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="market/login.html", authentication_form=LoginForm), name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)