"""clinico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from appbase.views import InicioV2, login_session_View, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include('appbase.urls')),
    path('atencion/', include('appconsulta.urls')),
    path('seguridad/login/', login_session_View.as_view(), name='login'),
    path('seguridad/logout/', logout_user.as_view(), name='logout'),
    path('', InicioV2.as_view(), name='inicio'),

]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
