from testproduct.models import Product

def show_data():
    print(Product.objects.values())