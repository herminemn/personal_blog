from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
    upload = models.FileField(upload_to='uploads/', default="")

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d, %Y')

    def summary(self):
        return self.body[:100]
