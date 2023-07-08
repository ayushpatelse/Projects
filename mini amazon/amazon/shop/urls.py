from django.urls import path,include
from . import views
urlpatterns = [
    path("home",views.home,name="home"),
    path("signin",views.signin,name="signin"),
    path("",views.signup,name="signup"),
    path("cart/<str:function>",views.cart,name="cart"),
    path("View/<str:id>",views.View,name="view"),
    path("checkout",views.checkout,name="checkout"),
    

]
