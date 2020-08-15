from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ForeignKey= 다른 모델에 대한 링크
    title = models.CharField(max_length=200) # models.CharField = 글자수가 제한된 텍스트의 정의
    text = models.TextField()                # models.TextField = 글자수의 제한이 없는 텍스트의 정의
    created_data = models.DateTimeField(    #   날짜 및 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
