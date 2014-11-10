from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from ecomstore import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^', include('catalog.urls')),
    url(r'^cart/', include('cart.urls')),
)
