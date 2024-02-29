from django.contrib import admin
from .models import Contact, AboutPage, AgeCroups, Schedules, Videos, Images, Groups, SkillStatistics, PersonalInfo

# Register your models here.

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ("logo", "title", "about", "facebook", "tiktok", "instagram")

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ("age_group", "video", "image", "schedule")


@admin.register(Schedules)
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ("date", "week_day", "hour")


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date",
                    "personal_image", "cover_image", "height", "weight", "foot", "position", "skill_statistic")


admin.site.register(Contact)
admin.site.register(AgeCroups)
admin.site.register(Videos)
admin.site.register(Images)
admin.site.register(SkillStatistics)
