from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from . import models, forms 
from django.contrib import messages
# Create your views here.

class ProductDetailView(DetailView):
    """ Vista para mostrar el detalle de un producto """
    model = models.Product
    
   
class ProductListView(LoginRequiredMixin, ListView):
    model = models.Product
    def get_queryset(self):
        """Filtra todos los productos que contengan el texto ingresado."""
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Product.objects.filter(name__icontains=query)
        else:
            object_list = models.Product.objects.all()
        return object_list
    
class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy("products:product_list")

    def form_valid(self, form):
        messages.success(self.request, "Producto creado correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    def test_func(self):
        """ Devuelve True si el usuario tiene permiso."""
        return self.request.user.has_perm('products.add_product')
    
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Product
    template_name = "products/confirm_delete.html"
    success_url = reverse_lazy("products:product_list")

    def get_success_url(self):
            messages.success(self.request, "Producto eliminado correctamente.", extra_tags="alert alert-danger")
            return super().get_success_url()
    
    def test_func(self):
        """ Devuelve True si el usuario tiene permiso."""
        return self.request.user.has_perm('products.delete_product')

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Product
    success_url = reverse_lazy("products:product_list")
    form_class = forms.ProductForm

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente.", extra_tags="alert alert-success")
        return super().form_valid(form)
    def test_func(self):
        """ Devuelve True si el usuario tiene permiso."""
        return self.request.user.has_perm('products.change_product')
    

