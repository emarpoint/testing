from django.contrib import admin

from .models import Category, Profile, Question,  Result




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, 
            {'fields': [ 'profile_name', 'question', 'option1', 'option2', 'option3', 'option4', 'answer','is_active', 'weight']}
        ),
        ('Информация о дате',
            {'fields': ['date_published'], 
            'classes': ['collapse']}
        ),
    ]
    list_display = ['id','profile_name', 'question', 'date_published', 'is_active', 'weight']
    list_filter = ['date_published']
    search_fields = ['title']
    date_hierarchy = ('date_published')

class ResultAdmin(admin.ModelAdmin):
    list_display=("profile_id", "date_time", "username", "rating")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug', 'name',
    'work_time', 'questions_count',]
    list_filter = ['category']
    # list_editable = ['category']
    prepopulated_fields = {'slug': ('name',)}
    

 



   
admin.site.register(Category, CategoryAdmin),
admin.site.register(Profile, ProfileAdmin),
admin.site.register(Question, QuestionAdmin),
admin.site.register(Result, ResultAdmin),
