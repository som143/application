
from django.contrib import admin
from django.urls import path, include
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.regView,name='register'),
    path('otpshow',views.generate_otp,name='generate'),
    path('login/',include('myapp.urls')),
    # path('show',views.new,name='show'),
]
