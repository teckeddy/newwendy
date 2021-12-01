from django.db import models

class Gallery(models.Model):
    image=models.ImageField(upload_to='media')
    name=models.CharField(max_length=250)
    summery=models.TextField("product summary description",default="Wendys closet")
    details=models.TextField(help_text="Full product details",default="wendys closet")

    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

  