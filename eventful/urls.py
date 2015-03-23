from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from eventful import settings

urlpatterns = patterns('eventful_app.views',
    # Examples:
    # url(r'^$', 'eventful.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'show_cats', name='show_cats'),
    url(r'^results/(?P<api_query>.+)$', 'show_query'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
