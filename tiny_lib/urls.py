from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fta.heroku.app.com/', include('tiny_app.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
