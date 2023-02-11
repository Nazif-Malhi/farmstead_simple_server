from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from authentication.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, ChangePasswordSerializer, SentPasswordResetSerializer, PasswordResetSerializer, MyUsersSerializer, SentVerifiedSerializer, UserVerifiedSerializer
from django.contrib.auth import authenticate
from authentication.renderers import Renderers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from authentication.models import MyUser


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'message': "Created Successfully"}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    renderer_classes = [Renderers]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'message': "Login Successfully", 'Token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': "User Name & Password doesn't matched"}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    renderer_classes = [Renderers]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [Renderers]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Password Change Success"}, status=status.HTTP_200_OK)


class SentPasswordResetView(APIView):
    # renderer_classes = [Renderers]

    def post(self, request, format=None):
        serializer = SentPasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Email sent for password reset. Please check your mail"}, status=status.HTTP_200_OK)


class ResetPasswordView(APIView):
    renderer_classes = [Renderers]

    def post(self, request, uid, token, format=None):
        serializer = PasswordResetSerializer(data=request.data, context={
                                             'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Password Reset Successfully"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        print(request.data)
        if id is not None:
            user = MyUser.objects.get(id=id)
            serializer = MyUsersSerializer(user)
            return Response(serializer.data)
        users = MyUser.objects.all()
        users_serializer = MyUsersSerializer(users, many=True)
        return Response(users_serializer.data)


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, id, format=None):
        user = MyUser.objects.get(id=id)
        if user is not None:
            serializer = MyUsersSerializer(
                user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors)


class UserVerifiedView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = SentVerifiedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Email sent for password verified."}, status=status.HTTP_200_OK)


class UserVerfiedUpdateView(APIView):
    renderer_classes = [Renderers]

    def post(self, request, uid, token, format=None):
        serializer = UserVerifiedSerializer(data=request.data, context={
            'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({"message": "verified"}, status=status.HTTP_200_OK)