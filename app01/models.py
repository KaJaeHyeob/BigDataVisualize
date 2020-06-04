from django.db import models
from django.conf import settings
from django.utils import timezone


# 모델 : 데이터베이스를 사용하여 비즈니스 로직 수행


class FileRequest(models.Model):
    title = models.CharField(max_length=100)
    fileName = models.FileField(null=False, blank=False, upload_to="file/")
    time = models.DateTimeField(default=timezone.now)


class ImageResponse(models.Model):
    title = models.CharField(max_length=100)
    imagePath = models.ImageField(null=False, blank=False, upload_to="image/")
    time = models.DateTimeField(default=timezone.now)

    def getImagePath(self):
        return '%s%s' % (settings.MEDIA_URL, self.imagePath)

