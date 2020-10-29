from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from profiles.models import UserProfile


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def no_of_ratings(self):
        ratings = Ratings.objects.filter(self)
        return len(ratings)


class Ratings(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    stars = models.IntegerField(validators=[MinValueValidator(1),
                                MaxValueValidator(5)])

    class Meta:
        verbose_name_plural = 'Ratings'
        unique_together = (('product', 'user_profile'),)
        index_together = (('product', 'user_profile'),)

    def __str__(self):
        return self.stars
