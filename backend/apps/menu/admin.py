from django.contrib import admin



from .models import Category, Product, SubCategory



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("name",)}

# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
# 	prepopulated_fields = {"slug":("name",)}


admin.site.register(Product)