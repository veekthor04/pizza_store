from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=64, db_index=True)
	slug = models.SlugField(max_length=64, unique=True)
	
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	
	def get_absolute_url(self):
		return reverse('orders:product_list_by_category', args=[self.slug])
	
	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=64, db_index=True)
	slug = models.SlugField(max_length=64, db_index=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	
	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)
	
	def get_absolute_url(self):
		return reverse('orders:product_detail', args=[self.id, self.slug])
	
	def __str__(self):
		return f"{self.id} - {self.name} ${self.price}"

class Topping(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"{self.id} - {self.name} ${self.price}"