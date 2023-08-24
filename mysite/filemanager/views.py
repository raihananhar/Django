from django.shortcuts import render
from rest_framework import viewsets
from .models import TypeFile, File
from .serializers import TypeFileSerializer, FileSerializer, FileListSerializer, FileGetSerializer, FileCRUDSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class TypeFileViewSet(viewsets.ModelViewSet):
    queryset = TypeFile.objects.all()
    serializer_class = TypeFileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileListViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileListSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_list(self):
        queryset = File.objects.all()
        title = self.request.query_params.get('title', None)
        type = self.request.query_params.get('type', None)
        sortbyCreatedat = self.request.query_params.get('sortbyCreatedat', None)
        if title is not None:
            queryset = queryset.filter(title__contain =title)
        if type is not None:
            queryset = queryset.filter(type_file__id =type)
        if sortbyCreatedat is not None:
            if sortbyCreatedat == 'asc':
                queryset = queryset.order_by('created_at')
            elif sortbyCreatedat == 'desc':
                queryset = queryset.order_by('-created_at')
        
        limit = self.request.query_params.get('limit', None)
        offset = self.request.query_params.get('offset', None)
        countData = queryset.count()
        if limit is not None and offset is not None:
            queryset = queryset[int(offset):int(offset)+int(limit)]
        return (queryset, countData)
    
    def list(self, request):
        queryset = self.get_list()[0]
        count = self.get_list()[1]
        serializer = FileListSerializer(queryset, many=True)
        data_result = serializer.data
        response ={
            'count': count,
            'length': len(data_result),
            'message': 'success',
            'results': data_result
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = FileCRUDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = {
            'status': 'success',
            'code' : status.HTTP_201_CREATED,
            'message': 'File created successfully',
            'files': serializer.data
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class FileGetViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileGetSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_retrieve(self):
        queryset = File.objects.get(pk=self.kwargs['pk'])
        type = self.request.query_params.get('type', None)
        if type is not None:
            queryset = queryset.filter(type=type)
        return queryset
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FileCRUDSerializer(instance,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {
            'status': 'success',
            'code' : status.HTTP_200_OK,
            'message': 'File berhasil diubah',
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response = {
            'status': 'success',
            'code' : status.HTTP_204_NO_CONTENT,
            'message': 'File berhasil dihapus',
        }
        return Response(response,status=status.HTTP_204_NO_CONTENT)

    

    
