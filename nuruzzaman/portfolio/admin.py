from django.contrib import admin
from .models import Category, PortfolioItem, Education, WorkHistory
from .models import ContactInfo

admin.site.register(Category)
admin.site.register(PortfolioItem)


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'email', 'telegram', 'skype']
    search_fields = ['country', 'city', 'email']

admin.site.register(ContactInfo, ContactInfoAdmin)



class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'designation', 'session', 'description', 'link')
    search_fields = ('title', 'designation')

class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'designation', 'session', 'description', 'link')
    search_fields = ('title', 'designation')

admin.site.register(Education, EducationAdmin)
admin.site.register(WorkHistory, WorkHistoryAdmin)


# admin.py
from django.contrib import admin
from .models import LanguageSkill, HardSkill

@admin.register(LanguageSkill)
class LanguageSkillAdmin(admin.ModelAdmin):
    list_display = ('language_name', 'progress')
    search_fields = ('language_name',)


@admin.register(HardSkill)
class HardSkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'progress')
    search_fields = ('skill_name',)


# admin.py
from django.contrib import admin
from .models import PersonalInfo

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'residence', 'date_of_birth', 'dynamic_age')
    readonly_fields = ('dynamic_age',)


# admin.py
from django.contrib import admin
from .models import KnowledgeItem

@admin.register(KnowledgeItem)
class KnowledgeItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')  # Display name and order in the admin list
    list_editable = ('order',)  # Allow editing of the order directly in the admin list




from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title_part1', 'title_part2')
    fieldsets = (
        ('Title Settings', {
            'fields': ('title_part1', 'title_part2')
        }),
        ('Content Settings', {
            'fields': ('rotating_text', 'image', 'banner_photo')
        }),
    )



# admin.py
from django.contrib import admin
from .models import CounterData

@admin.register(CounterData)
class CounterDataAdmin(admin.ModelAdmin):
    list_display = ('years_experience', 'completed_projects', 'happy_customers', 'honors_awards')



# admin.py
from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')



# admin.py
from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'star_rating')



# admin.py
from django.contrib import admin
from .models import PricingPlan

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'popular')
