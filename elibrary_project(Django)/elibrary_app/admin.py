from django.contrib import admin
from elibrary_app.models import Author,Category,EBooksModel
# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(EBooksModel)