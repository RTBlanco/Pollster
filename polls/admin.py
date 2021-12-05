from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# Documentation: -> https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Welcome to the Pollster Admin Area'

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3
  
class QuestionAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {
      "fields": (
        'question_text', 'pub_date'
      ),
    }),
  )
  
  inlines = [ChoiceInline]
  
  


admin.site.register(Question, QuestionAdmin)


# admin.site.register(Question)
# admin.site.register(Choice)