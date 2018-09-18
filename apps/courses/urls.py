from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('destroy/<int:id>', views.destroy),
    path('comments/<int:id>', views.comments),
    path('remove', views.remove),
    path('addComment', views.add_comment)
]