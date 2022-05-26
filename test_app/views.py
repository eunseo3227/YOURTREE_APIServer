from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from test_app.models import Test
from test_app.serializers import TestSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()               # Test테이블 안에 있는 모든 object들을 queryset으로 저장.
    serializer_class = TestSerializer