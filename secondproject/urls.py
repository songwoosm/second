from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
import accounts.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', blog.views.home, name="home"),
    path('blog/',include('blog.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('signup/', accounts.views.signup, name='signup'),
    path('', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name="logout"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
