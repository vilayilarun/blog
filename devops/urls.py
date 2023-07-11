from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.blogs.urls')),
    path('scribblings/', include('applications.gallery.urls')),
    path('contact-us/', include('applications.contact.urls')),
    path('accounts/', include('applications.accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
