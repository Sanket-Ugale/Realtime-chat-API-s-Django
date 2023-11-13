from django.contrib import admin
from django.urls import path
from api.views import GrpMsgCreateView, GrpMsgDeleteView, GrpMsgUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/groups/create/', GrpMsgCreateView.as_view(), name='group-create'),
    path('api/groups/update/<int:pk>/', GrpMsgUpdateView.as_view(), name='group-update'),
    path('api/groups/delete/<int:pk>/', GrpMsgDeleteView.as_view(), name='group-delete'),
]

