from django.conf.urls import patterns, include, url
import primero.views

from django.contrib import admin
admin.autodiscover()
views = "primero.views."

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'primero.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', primero.views.hello),
    url(r'^alert/$', primero.views.jsAlert),
    url(r'^time/$', primero.views.currentDateTime),
	url(r'^time/plus/(\d+)/$', primero.views.hours_ahead), #plus any number > 0
	url(r'^time/restrictedPlus/(\d{1,2})/$', primero.views.hours_ahead), #plus two digit numbers > 0
    url(r'^(orderSubmitted)/(.+)/(AuRa)/(T|F)/$', primero.views.displayThankForm),
    url(r'^dateTime/$', primero.views.currentDateTimeTemplate), #Using base html (inheritance)

    url(r'^admin/', include(admin.site.urls)),
)
