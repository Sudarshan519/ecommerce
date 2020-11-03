from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default='')
    chead0 = models.CharField(max_length=5000, default='')
    head1 = models.CharField(max_length=500, default='')
    chead1 = models.CharField(max_length=5000, default='')
    head2 = models.CharField(max_length=500, default='')
    chead2 = models.CharField(max_length=5000, default='')
    author=models.CharField(max_length=5000, default='asmir@asmz')
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="website/images,", default="")

    def __str__(self):
        return self.title + 'by ' +self.author

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500, default='')
    author = models.CharField(max_length=5000, default='')
    slug = models.CharField(max_length=500, default='')
    timeStamp = models.DateTimeField(blank=True)
    thumbnail = models.ImageField(upload_to="website/images,", default="")

    def __str__(self):
        return self.title + 'by ' +self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

   

    def __str__(self):
        return self.comment[0:13] + '..' +"by "+self.user.username