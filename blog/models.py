from django.db import models

# Create your models here.

class Blog(models.Model):
    
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Blog post in admin is the title
    def __str__(self):
        return self.title

# Caps summary to certain numbers of chars
    def summary(self):
        return self.body[:100]

# Strftime to display date however
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')