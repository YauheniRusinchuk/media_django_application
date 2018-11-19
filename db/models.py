from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import comments.models


class Post(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
	title = models.CharField(max_length=100)
	description = models.TextField(blank=False, null=False)
	content = RichTextUploadingField(blank=False, null=False)
	img = models.ImageField(upload_to='posts/', blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	def lenght_comments(self):
		result = comments.models.Comment.objects.filter(post=self)
		return len(result)

	def contentmax(self):
		return self.description[:300] + " ..."


	class Meta:
		ordering = ['-date']
