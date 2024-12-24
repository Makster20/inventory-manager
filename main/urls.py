from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('new-category/', views.new_category, name='new-category'),
    path('category/<int:category_id>', views.category_items, name='category-items'),
    path('category/<int:category_id>/new', views.new_item, name='new-item'),
    path('category/<int:category_id>/<int:item_id>/edit', views.edit_item, name='edit-item'),
    path('category/<int:category_id>/<int:item_id>/delete', views.delete_item, name='delete-item'),
    path('category/<int:category_id>/edit', views.edit_category, name='edit-category'),
    path('category/<int:category_id>/delete', views.delete_category, name='delete-category'),
]
