from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 

urlpatterns = [
    # path ('',views.ProductView().as_view, name='home'),
    path('', views.home, name='home'),
    path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('delcart/<int:pk>', views.del_cart, name='delcart'),
    path('emptycart/' , views.emptycart , name='emptycart'),
    path('pluscart/' , views.plus_cart ),
    path('minuscart/' , views.minus_cart ),
    # path('removecart/' , views.remove_cart ),
    path('paymentdone', views.paymentdone , name='paymentdone'), 
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.customerregistration, name='customerregistration'),
    # path('CustomerRegisterations', views.customerregisterationView().as_view, name='CustomerRegisterations'),
    path('checkout/', views.checkout, name='checkout'),


]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
