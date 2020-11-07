"""New_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.article import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('article/', include('apps.article.urls', namespace='article')),

    path('', views.article_list, name='homepage'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path(r'mdeditor/', include('mdeditor.urls')),

    # 用户管理
    path('userprofile/', include('apps.userprofile.urls', namespace='userprofile')),

    # path('', views.homepage, name='homepage'),

    path('password-reset/', include('password_reset.urls')),

    path('comment/', include('apps.comment.urls', namespace='comment')),
]

if settings.DEBUG:
    # add_static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
