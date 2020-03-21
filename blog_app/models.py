from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField()
    category = models.ForeignKey('blog_app.Category',
                                 blank=True, null=True,
                                 on_delete=models.CASCADE,
                                 related_name='post'
                                 )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
