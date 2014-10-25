from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pacman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^APIaaS/', include(APIaaS.site.urls)),
    #url(r'^DaaS/', include(DaaS.site.urls)),
    #url(r'^GaaaS/', include(GaaaS.site.urls)),
    #url(r'^DAaaS/', include(DAaaS.site.urls)),
)
