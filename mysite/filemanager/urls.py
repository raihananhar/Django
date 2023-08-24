from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileGetViewSet, FileListViewSet, FileViewSet, TypeFileViewSet
from . import views

router = DefaultRouter()
router.register(r"file", FileViewSet)
router.register(r"filelist", FileListViewSet)
router.register(r"fileget", FileGetViewSet)
router.register(r"typefile", TypeFileViewSet)

app_name = "filemanager"
urlpatterns = [
    path("", views.FileListViewSet.as_view({'get' : 'list', 'post' : 'create'}), name="index"),
    path("<pk>/", views.FileGetViewSet.as_view({'get': 'retrieve','put' : 'update', 'delete': 'delete'})),
    path("api/", include(router.urls)),
]