from django.db import models

# Create your models here.

class UserPet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    password = models.CharField(max_length=20)
    numberOfPosts = models.IntegerField(default=0)
    numberOfFollowers = models.IntegerField(default=0)
    numberOfFollowing = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Post (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(UserPet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Reaction (models.Model):
    isLike = models.BooleanField()
    comment = models.CharField(blank=True, max_length=100)
    user = models.ForeignKey(UserPet, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.description