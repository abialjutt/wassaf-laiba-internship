from django.contrib import admin
from .models import *

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    # fields = ["tutorial_title",
    #           "tutorial_published",
    #           "tutorial_content"]
    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["tutorial_content"]})
  
     ]
    prepopulated_fields = {'tutorial_slug' : ('tutorial_title', ), }
    # fieldsets = [
    #     ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
    #     ("Content", {"fields": ["tutorial_content"]})
    # ]
admin.site.register(User)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)

