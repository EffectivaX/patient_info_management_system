from django.db import models

# Create your models here.

# class ProgressUpdate(models.Model):
#     request_email = models.EmailField()
#     slug = models.SlugField(unique=True, editable=False)
#
#     def __str__(self):
#         return self.email
#
#     def save(self, *args, **kwargs):
#         value = self.request_email
#         self.slug = slugify(value, allow_unicode=True)
#         super().save(*args, **kwargs)
