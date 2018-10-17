from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_of_board, name='list_of_board'),
    url(r'^(?P<slug>[-\w]+)/(?P<board_id>[0-9]+)/$', views.board_detail, name='board_detail'),
    url(r'^table/create/$', views.create_board, name='create_board'),
    url(r'^table/card/create/$', views.create_card, name='create_card'),
    url(r'^(?P<slug>[-\w]+)/(?P<board_id>[0-9]+)/delete_board/$', views.delete_board, name='delete_board'),
    url(r'^(?P<slug>[-\w]+)/(?P<board_id>[0-9]+)/delete_card/(?P<card_id>[0-9]+)/$', views.delete_card, name='delete_card'),
    url(r'^(?P<slug>[-\w]+)/(?P<board_id>[0-9]+)/update_card_success/(?P<card_id>[0-9]+)/$', views.success_button, name='success_button'),
    url(r'^(?P<slug>[-\w]+)/(?P<board_id>[0-9]+)/update_card_warning/(?P<card_id>[0-9]+)/$', views.warning_button, name='warning_button'),
    url(r'^(?P<slug>[-\w]+)/(?P<board_id>[0-9]+)/update_card_danger/(?P<card_id>[0-9]+)/$', views.danger_button, name='danger_button'),
]
