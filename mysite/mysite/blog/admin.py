from django.contrib import admin
from .models import Post, Profile

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','status')
    list_filter = ('status','title')
    search_fields = ('status','title','author')
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo',)


admin.site.register(Post,PostAdmin)
admin.site.register(Profile, ProfileAdmin)
