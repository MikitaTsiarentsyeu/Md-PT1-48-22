from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.items, name='search_results'),
    path('items/', views.items, name='all_items'),
    path('type/<str:type>/', views.items, name='by_type'),
    path('category/<int:category_id>/', views.items, name='by_category'),
    path('city/<int:city_id>/', views.items, name='by_city'),
    path('item/<int:item_id>/', views.item, name='item'),
    path('item/<int:item_id>/respond', views.respond, name='respond'),
    path('add_item/', views.add_item, name='add_item'),
    path('help/', views.help, name='help')
]
