from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # customer
    path('', views.home_view, name='home_view'),
    path('<str:username>', views.store_view, name='store_view'),
    path('product/<int:myid>', views.productView, name='product_view'),
    url(r'^ajax/rating/$', views.ProductRatingAjaxView.as_view(), name='ajax_rating'),
    # url(r'^like/$', views.like_product, name='like_product'),
    # path('product/<int:myid>/like', views.ProductLikeToggle.as_view(), name='like_product'),
    path('product/<int:myid>/like', views.ProductAPILikeToggle.as_view(), name='like_product'),
    path('search/products', views.SearchItem.as_view(), name='search_product'),


    # seller
    path('product/detail/<int:myid>', views.seller_product_view, name='product_seller_view'),
    path('product/new', views.ProductAddView.as_view(), name='add-product'),
    path('product/<int:pk>/update', views.ProductUpdateView.as_view(), name='update-product'),
    path('product/<int:pk>/delete', views.ProductDeleteView.as_view(), name='delete-product'),
    path('product/list', views.SellerProductListView.as_view(), name='product_list'),
    # path('product/list', views.sellerProductListView, name='product_list'),


    path('seller/dashboard', views.dashboard, name='dashboard'),

    path('category/new', views.CategoryAddView.as_view(), name='add-category'),
    path('category/<int:pk>/update', views.CategoryUpdateView.as_view(), name='update-category'),
    path('category/<int:pk>/delete', views.CategoryDeleteView.as_view(), name='delete-category'),
    path('category/list', views.SellerCategoryListView.as_view(), name='category_list'),

]
