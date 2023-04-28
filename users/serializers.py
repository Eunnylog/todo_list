from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    # create()는 serializers.ModelSerializer의 메서드이며, 부모 클래스 메서드를 호출한 것이다
    def create(self, validated_data):
        user = super().create(validated_data) # 검증된 데이터 사용해 -> 유저 인스턴스 생성 -> user에 담아줌
        password = user.password
        user.set_password(password)  # 비밀번호 암호화
        user.save() # 암호화 설정된 유저 저장
        return user
        