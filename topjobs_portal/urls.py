from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('', home, name='home')
    path('admin/', admin.site.urls),
    path('api/', include('cvs.urls')),
    path('candidates/', include('candidates.urls')),
]
admin.site.site_header ="Top Jobs"
admin.site.site_title ="Top Jobs"
admin.site.index_title ="Top Jobs"
admin.site.site_urls="Top Jobs"