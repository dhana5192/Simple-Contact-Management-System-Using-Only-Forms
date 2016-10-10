from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add-contact', views.add_contact, name='add_contact'),
    url(r'^$', views.index, name='index'),
    url(r'^contact-list', views.contact_list, name='contact_list'),
    url(r'^(?P<contact_id>[0-9]+)/delete/$', views.contact_delete, name='contact_delete'),
    url(r'^(?P<contact_id>[0-9]+)/edit/$', views.contact_edit, name='contact_edit'),
]
