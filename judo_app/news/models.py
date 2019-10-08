from django.db import models
from django.utils import timezone
from register.models import User

# Create your models here.


class News(models.Model):
    """
        Esta classe define uma noticia dentro do sistema
    """
    id = models.AutoField(primary_key=True)
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, db_column="author_name")
    title = models.CharField(max_length=200, db_column="news_name")
    text = models.TextField(db_column="news_content")
    published = models.DateTimeField(
        default=timezone.now, db_column="published_date")
    edited = models.DateTimeField(
        blank=True, null=True, db_column="Last_edited")

    def edit(self):
        self.edited = timezone.now()
        self.save()

    def __str__(self):
        return self.title
