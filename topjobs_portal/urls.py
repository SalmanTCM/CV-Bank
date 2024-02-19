from django.contrib import admin
from django.urls import path, include
from candidates import router as candidates_api_router

api_url_patterns = [
    path(r'accounts/', include(candidates_api_router.router.urls))
]
urlpatterns = [
    # path('', home, name='home')
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
    # path('api/', include('cvs.urls')),
    # path('candidates/', include('candidates.urls')),
]
admin.site.site_header ="Top Jobs"
admin.site.site_title ="Top Jobs"
admin.site.index_title ="Top Jobs"
admin.site.site_urls="Top Jobs"