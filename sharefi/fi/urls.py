from django.conf.urls import url 
from fi import views 
 
urlpatterns = [ 
    url(r'^api/fi$', views.fi_list),
    url(r'^api/fi/(?P<pk>[0-9]+)$', views.fi_detail),
    url(r'^api/fi/stock_today$', views.fi_list_stock_date),
    url(r'^api/fi/ai$', views.fi_get_ai_stock_price)
]