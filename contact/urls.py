
from django.contrib import admin
from django.urls import path
from .contactApp.views import PrimContListViewPost,PrimContListViewGet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/identity', PrimContListViewPost.as_view()),
    path('api/contacts', PrimContListViewGet)
]
