from django.urls import path
from . import views

app_name = 'Test'
urlpatterns = [
    path('test', views.index, name='index'),
    path('createProduct', views.create_views, name='create_views'),
    path('', views.list_view, name='list_view'),
    path('updateProduct/<int:id>', views.update_product, name='update_product'),
    path('seeProduct/<int:id>', views.detail_view, name='detail_product'),
    path('deleteProduct/<int:id>', views.delete_views, name='delete_product')
]