from rest_framework import serializers
from .models import TypeFile, File

class TypeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeFile
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class FileListSerializer(serializers.ModelSerializer):
    type_file = TypeFileSerializer()
    class Meta:
        model = File
        fields = ['id', 'title', 'type_file', 'created_at']

class FileGetSerializer(serializers.ModelSerializer):
    type_file = TypeFileSerializer()
    class Meta:
        model = File
        fields = ['id', 'title', 'file', 'type_file', 'thumbnail', 'created_at', 'deskription']

class FileCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'title', 'file', 'type_file', 'thumbnail', 'deskription']