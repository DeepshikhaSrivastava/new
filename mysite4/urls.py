
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from food import views
from rest_framework import routers
from food.views import FoodViewSet, CommentViewSet






router = routers.DefaultRouter()
router.register(r'food', views.FoodViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'reply', views.ReplyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),

]


