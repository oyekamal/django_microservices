from django.urls import path


from .views import GetProductData
urlpatterns = [
    path('Getproducts/', GetProductData.as_view())

]