from django.contrib import admin        # django admin 사이트에서 테이블이 보이도록 등록

# Register your models here.
from test_app.models import Test

# admin.site.register(Account)
admin.site.register(Test)
