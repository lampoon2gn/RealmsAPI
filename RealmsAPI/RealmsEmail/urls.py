from . import views
from django.urls import include,path
from .models import ClientMsg
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'msg',views.ClientMsgViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework'))
]
