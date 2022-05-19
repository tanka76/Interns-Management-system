from django.shortcuts import render
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import viewsets
from django.contrib.auth import authenticate,logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserLoginSerializer,AttendanceSerializer,TaskSerializer



# Create your views here.
class LoginView(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password','1026')
        user = authenticate(email=email, password=password)
        if user is not None:
            try:
                token = Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response({'token':token.key, 'message':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"detail": "Successfully Logout"})



class AttedanceAPI(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    def create(self, request, *args, **kwargs):
        serializer = AttendanceSerializer(data = request.data, context = {'user':request.user})
        if serializer.is_valid():
            if serializer.save():
                return Response({"detail": "Attendance Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class TaskCompletedAPI(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    def create(self, request, *args, **kwargs):
        print("views",request.data)
        serializer = TaskSerializer(data = request.data,context = {'task_name':request.data['task_name']})
        if serializer.is_valid():
            if serializer.save():
                return Response({"detail": "Task Completed"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)