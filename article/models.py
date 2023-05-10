from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Article(models.Model):
    author          = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title           = models.CharField(max_length = 50)
    content         = RichTextField()
    created_date    = models.DateTimeField(auto_now_add=True)
    article_image   = models.FileField(blank = True, null = True, verbose_name="Add image")
    
    def __str__(self):
        return self.title
    
    class Meta:
        """ this meta class allow us to list our articles from the newest to the lattest """
        ordering = ["-created_date"]


class Comment(models.Model):
    article         = models.ForeignKey(Article, verbose_name="Article", on_delete=models.CASCADE , related_name="comments")
    comment_author  = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=200)
    comment_date    = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment_content
    
    class Meta:
        """ this meta class allow us to list our comments from the newest to the lattest """
        ordering = ["-comment_date"]