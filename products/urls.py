from django.urls import path, include
from products.views import ProductsListView,ProductCreateView,ProductDetailView,ProductUpdateView,ProductDeleteView

urlpatterns = [
    path('', ProductsListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', include([
        path('', ProductDetailView.as_view(), name='product-details'),
        path('edit/', ProductUpdateView.as_view(), name='product-edit'),
        path('delete/', ProductDeleteView.as_view(), name='product-delete'),

    ])),
]