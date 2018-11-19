from django.db import models
from db.models import Post
# Create your models here.



class Comment(models.Model):
	text = models.TextField(blank=False, null=False)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text