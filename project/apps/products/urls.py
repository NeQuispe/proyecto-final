from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="products/index.html"), name="index"),
    path("detail/<int:pk>", views.ProductDetailView.as_view(), name="product_detail"),
    path("list/", views.ProductListView.as_view(), name="product_list"),
    path("create/", views.ProductCreateView.as_view(), name="product_create"),
    path("delete/<int:pk>", views.ProductDeleteView.as_view(), name="product_delete"),
    path("update/<int:pk>", views.ProductUpdateView.as_view(), name="product_update"),
    
    
    
]
