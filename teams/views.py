from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import AboutPage, Contact, Groups, PersonalInfo
from .serializers import AboutPageSerializer, ContactSerializer, GroupsSerializer, PersonalInfoSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.
class AboutPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer


class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer


class PersonalInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAuthenticated]


# დალოგინების ფუნქციონალი / აბრუნებს ტოკენს ან წერს რომ მომხმარებელი რეგისტრირებული არ არის
class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes =[AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            except User.DoesNotExist:
                return Response({'error': "მომხმარებელი რეგისტრირებული არ არის"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
