from django.contrib import admin
from .models import Question, Product

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['text']

class ProductAdmin(admin.ModelAdmin):
    fields = ['image_url', 'name', 'stock', 'price']

admin.site.register(Question)
admin.site.register(Product)

