from rest_framework.response import Response
from rest_framework.views import APIView as ApiView
from django.shortcuts import get_object_or_404

from app.models import User, Role
from app.serializers import UserSerializer, RoleSerializer


class UserView(ApiView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # ✏️ ACTUALIZAR USUARIO
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # ❌ ELIMINAR USUARIO
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=204)


class RoleView(ApiView):

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # ACTUALIZAR ROL
    def put(self, request, pk):
        role = get_object_or_404(Role, pk=pk)
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # ELIMINAR ROL
    def delete(self, request, pk):
        role = get_object_or_404(Role, pk=pk)
        role.delete()
        return Response(status=204)