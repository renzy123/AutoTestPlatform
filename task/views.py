from django.shortcuts import render
from product.models import Product, SuitProductMapping


# Create your views here.


def init_task_page(request):
    products = Product.objects.all()
    # 获取产品信息
    product_info = []
    for product in products:
        _p = {"name": product.name, "id": product.id}
        product_info.append(_p)

    return render(request, "pages/task/task.html", {"products": product_info})
