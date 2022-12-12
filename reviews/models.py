from django.db import models
from django.utils import timezone

class Review(models.Model):
    STARS = (
        (1, '☆'),
        (2, '☆☆'),
        (3, '☆☆☆'),
        (4, '☆☆☆☆'),
        (5, '☆☆☆☆☆')

    )

    store_name = models.CharField('タイトル', max_length=225)
    title = models.CharField('コメント', max_length=255)
    text = models.TextField('コメント詳細',blank=True)
    stars = models.IntegerField('星の数', choices=STARS, null=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title