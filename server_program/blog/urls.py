
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import DynamicImageURL

router = routers.DefaultRouter()
router.register('Post', views.IntruderImage) 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('api_root/', include(router.urls)),
]

urlpatterns += [
    path('api/get_dynamic_image_url/', DynamicImageURL.as_view(), name='dynamic_image_url'),
    # 다른 URL 패턴들을 추가할 수 있습니다.
]
