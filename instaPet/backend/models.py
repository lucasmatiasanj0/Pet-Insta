from django.db import models


class UserPet(models.Model):
    name = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    email = models.EmailField()
    description = models.TextField()
    image_url = models.TextField(default='')
    
    def __str__(self):
        return self.name
    
    
class Post (models.Model):
    description = models.CharField(max_length=100)
    image_url = models.TextField(default='')
    user = models.ForeignKey(UserPet, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ' ' + self.description

class Reaction (models.Model):
    isLike = models.BooleanField()
    comment = models.CharField(blank=True, max_length=100)
    user = models.ForeignKey(UserPet, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
class Follow(models.Model):
    user = models.ForeignKey(UserPet, on_delete=models.CASCADE)
    follower = models.ForeignKey(UserPet, on_delete=models.CASCADE, related_name='follower')
    
    def __str__(self):
        return self.description