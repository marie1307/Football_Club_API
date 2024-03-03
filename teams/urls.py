from django.urls import path, include
from .views import GroupsViewSet, PersonalInfoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'about', AboutPageViewSet, basename="about_page"),
# router.register(r'contact', ContactViewSet, basename="contact"),
router.register(r'groups', GroupsViewSet, basename="groups"),
router.register(r'personal_page', PersonalInfoViewSet, basename="personal_page"),


urlpatterns = [
    path('', include(router.urls)),
    # path("personal_page/", PersonalInfoAPIView.as_view(), name="personal_page"),
]

