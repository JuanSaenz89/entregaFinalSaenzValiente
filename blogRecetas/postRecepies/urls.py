from django.urls import path
from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
             
    path('', HomeView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detalle_receta'),
    path('agregar_receta/', PostCreateView.as_view(), name='agregar_receta'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='editar_receta'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='borrar_receta'),
       
   ]
