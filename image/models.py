from django.db import models
class CategoryImage(models.Model):
  image = models.ImageField(upload_to = 'categories_image/%Y/%m', null = True)
  def __str__(self):
    return self.id

class ProductImage(models.Model):
  image = models.ImageField(upload_to = 'products_image/%Y/%m', null = True)
  def __str__(self):
    return self.id

class AvatarImage(models.Model):
  image = models.ImageField(upload_to = 'avatar_image/%Y/%m', null = True)
  def __str__(self):
    return self.id
