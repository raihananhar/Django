from django.db import models

# Create your models here.

class TypeFile(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, unique=True, blank=True)
    def __str__(self):
        return self.title

class File(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True, blank=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    type_file = models.ForeignKey(TypeFile, on_delete=models.DO_NOTHING, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    deskription = models.TextField(blank=True, null=True, max_length=500)
    def __str__(self):
        return self.title
