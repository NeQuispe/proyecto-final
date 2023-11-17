from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    
    path("", TemplateView.as_view(template_name="products/index.html"), name="index"),
    path("product/detail/<int:pk>", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/list/", views.ProductListView.as_view(), name="product_list"),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path("product/delete/<int:pk>", views.ProductDeleteView.as_view(), name="product_delete"),
    path("product/update/<int:pk>", views.ProductUpdateView.as_view(), name="product_update"),
 
        # Order
    
    path("order/list/", views.OrderListView.as_view(), name="order_list"),
    path("order/detail/<int:pk>", views.OrderDetailView.as_view(), name="order_detail"),
    path("order/create/", views.OrderCreateView.as_view(), name="order_create"),
    path("order/delete/<int:pk>", views.OrderDeleteView.as_view(), name="order_delete"),
    path("order/update/<int:pk>", views.OrderUpdateView.as_view(), name="order_update"),
    
       
    
    
]
