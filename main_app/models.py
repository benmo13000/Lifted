from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField()

    def __str__(self):
        queryset = Image.objects.all()
        return self.description 



class Post(models.Model):
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})    

    class Meta:
        ordering = ['-created_at']



class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_content_display()}"



class Photo(models.Model):
    url = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for post_id: {self.post_id} @{self.url}"