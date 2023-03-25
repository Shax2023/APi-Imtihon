
from django.contrib import admin
from django.urls import path, include
from api.views import UserList, ProductList, OrdeList, OrderItemList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserList,basename='user')
router.register(r'product', ProductList,basename='product')
router.register(r'order', OrdeList,basename='oredr')
router.register(r'orderitem', OrderItemList,basename='orderitem')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls))
]
