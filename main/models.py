from django.db import models
from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(default='default.png', upload_to='media/')
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Save the instance first to ensure the image file is available
        super().save(*args, **kwargs)

        if self.image:  # Ensure the image field is not empty
            try:
                img = Image.open(self.image.path)

                # Resize the image to exact dimensions (300x300), ignoring aspect ratio
                img = img.resize((150, 150))
                img.save(self.image.path, quality=100)  # Save with optimized quality
            except Exception as e:
                print(f"Error resizing image: {e}")


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

