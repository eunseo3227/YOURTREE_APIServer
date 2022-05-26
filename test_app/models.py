from django.db import models

# Create your models here.

class Test(models.Model):   # test 테이블 생성, 자동적으로 id라는 Primary Key가 생성됨
    test = models.CharField(max_length=10)

    def __str__(self):      # django admin사이트에서 어떻게 보여줄 지 결정
        return self.test

