
from django.contrib import admin
from django.urls import path,include
from .views import redirect_main_page

urlpatterns = [
    path('', redirect_main_page),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]


