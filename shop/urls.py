from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.product_list, name='product_list'),
	url(r'^feminino/$', views.female_product_list, name='female_product_list'),
	url(r'^masculino/$', views.male_product_list, name='male_product_list'),
	url(r'acessorios-sapatos', views.acessorios_list, name='acessorios-sapatos'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
	url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
]