from rest_framework import serializers  # 직렬화 장치
from test_app.models import Test        # 방금 전 생성한 model Import
                                        # model과 1대 1 매칭
class TestSerializer(serializers.ModelSerializer):  # 웹 상의 Data를 Json 형식으로 가져옴
    class Meta:
        model = Test
        fields = ('test', 'id')                     # 여기 내부에 있는 'test', 'id'는 우리가 위에서 생성한 테이블 들의 속성이다.
                                                    # id는 위에서 말했듯이 우리가 선언하지 않아도 자동적으로 생긴다.
                                                    # Api Root에서 보이는 것이 여기서 결정되는 것.