from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # author : 추후 작성 예정

    def __str__(self):
        # pk는 해당 포스트의 고유값: Primary Key???
        return f'[{self.pk}] {self.title}' # self.pk: 해당 포스트의 pk값, self.title: 해당 포스트의 title 값
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'