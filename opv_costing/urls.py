from django.conf.urls import patterns, url

from opv_costing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )
