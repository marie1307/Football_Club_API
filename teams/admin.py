from django.contrib import admin
from .models import Contact, AboutPage, AgeCroups, Schedules, Videos, Images, Groups, Skill_statistics, PersonalInfo

# Register your models here.

admin.site.register(AboutPage)
admin.site.register(Contact)
admin.site.register(AgeCroups)
admin.site.register(Schedules)
admin.site.register(Videos)
admin.site.register(Images)
admin.site.register(Groups)
admin.site.register(Skill_statistics)
admin.site.register(PersonalInfo)
