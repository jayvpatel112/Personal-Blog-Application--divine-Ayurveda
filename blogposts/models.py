from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="image")
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title} {self.author}"

class Comment(models.Model):
    user_name = models.CharField(max_length=20)
    content = models.TextField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name}"
