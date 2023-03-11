from django.urls import path
from .views import member_detail_view, members

urlpatterns = [
    path("", members.as_view(), name="members"),
    path('<int:pk>/', member_detail_view.as_view(), name='member_detail'),
]