from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from candidates import router as candidates_api_router
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# auth_api_urls = [
#     path(r'', include('rest_framework_social_oauth2.urls'))
# ]

# if settings.DEBUG:
#     auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))


api_url_patterns = [
    # path(r'auth/', include(auth_api_urls)),
    path(r'accounts/', include(candidates_api_router.router.urls))
]


urlpatterns = [
    # path('', home, name='home')
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/', include('cvs.urls')),
    # path('candidates/', include('candidates.urls')),
]
admin.site.site_header ="Top Jobs"
admin.site.site_title ="Top Jobs"
admin.site.index_title ="Top Jobs"
admin.site.site_urls="Top Jobs"