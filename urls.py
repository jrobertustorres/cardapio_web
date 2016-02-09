from django.conf.urls import include, url
from django.contrib import admin

#admin.site.index_template = 'admin/base_admin.html'
#admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'cardapio_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
