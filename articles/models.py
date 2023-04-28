from django.db import models
from users.models import User



class  Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(null=True, blank=True)

    
    # 어드민 페이지에서 쉽게 보기 위해서 제목 보이게 str 메소드 설정
    def __str__(self):
        return str(self.title)
    
    