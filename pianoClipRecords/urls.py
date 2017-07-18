from django.conf.urls import patterns, url
from . import views

app_name = 'pianoClipRecords'

urlpatterns = [
	#url(r'^publications/getPublication/', views.Publication.as_view(), name='getPublication'),
	url(r'^signup/$', views.UserFormView.as_view(), name = "signup"),
	url(r'^$', views.AuthenticationView.as_view(), name = "index"),
	url(r'^piano/$', views.records, name='records')
]