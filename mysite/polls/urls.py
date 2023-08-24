from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, ChoiceViewSet, UserLoginView, UserRegisterView
from django.urls import include

from . import views

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)
router.register(r"choices", ChoiceViewSet)

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("api/", include(router.urls)),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]