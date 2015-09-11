from django.conf.urls import url
from mumble_radio.views import UpdateListView, queue_data_ajax

urlpatterns = [
    url(r'^$', UpdateListView.as_view(), name='home-queue'),
    url(r'^queue/$', queue_data_ajax, name='ajax-queue')
]