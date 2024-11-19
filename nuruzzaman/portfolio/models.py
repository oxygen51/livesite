from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    image = models.ImageField(upload_to='portfolio_images/')
    external_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    


class ContactInfo(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    email = models.EmailField()
    telegram = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    icq = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255)
    personal_phone = models.CharField(max_length=255)

    def __str__(self):
        return f"Contact Info for {self.city}, {self.country}"
    


class Education(models.Model):
    title = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    session = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=500, blank=True, null=True)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class WorkHistory(models.Model):
    title = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    session = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(max_length=500, blank=True, null=True)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
    


# models.py
from django.db import models

class LanguageSkill(models.Model):
    language_name = models.CharField(max_length=50, unique=True)  # e.g., Bangla, English, Spanish
    progress = models.FloatField(default=0.0)  # Progress as a float value (0.0 to 1.0)

    def __str__(self):
        return f"{self.language_name} - {int(self.progress * 100)}%"

    class Meta:
        verbose_name = "Language Skill"
        verbose_name_plural = "Language Skills"


class HardSkill(models.Model):
    skill_name = models.CharField(max_length=50, unique=True)  # e.g., HTML, CSS, JS, PHP, etc.
    progress = models.FloatField(default=0.0)  # Progress as a float value (0.0 to 1.0)

    def __str__(self):
        return f"{self.skill_name} - {int(self.progress * 100)}%"

    class Meta:
        verbose_name = "Hard Skill"
        verbose_name_plural = "Hard Skills"



# models.py
from django.db import models
from datetime import date

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    thum_designation_1 = models.CharField(max_length=100)
    thum_designation_2 = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date_of_birth = models.DateField(default="2000-01-01")
    profile_image = models.ImageField(upload_to='personal_info/', blank=True, null=True)
    cv_file = models.FileField(upload_to='personal_info/cv/', blank=True, null=True)  # Field for CV file

    # Social Media Links
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    kaggle = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    stack_overflow = models.URLField(blank=True, null=True)
    quora = models.URLField(blank=True, null=True)
    hackerrank = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.residence}"

    @property
    def dynamic_age(self):
        """
        Calculate the current age in years, months, and days.
        """
        today = date.today()
        years = today.year - self.date_of_birth.year
        months = today.month - self.date_of_birth.month
        days = today.day - self.date_of_birth.day

        # Adjust for negative values in days or months
        if days < 0:
            months -= 1
            days += (today.replace(month=today.month - 1, day=1) - today.replace(month=today.month, day=1)).days

        if months < 0:
            years -= 1
            months += 12

        return f"{years} y {months} m {days} d"

    


# models.py
class KnowledgeItem(models.Model):
    name = models.CharField(max_length=255)  # Name of the knowledge item
    order = models.PositiveIntegerField(default=0)  # Field to specify order

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']  # Default ordering by the 'order' field




from django.db import models
from django.core.validators import FileExtensionValidator

class Banner(models.Model):
    title_part1 = models.CharField(max_length=100, default="Discover my Amazing")  # First part of the title
    title_part2 = models.CharField(max_length=100, default="Art Space!")          # Second part of the title
    rotating_text = models.TextField(                                             # Text for rotating content
        help_text='Enter a JSON array, e.g., ["web interfaces.", "ios and android applications.", "design mockups.", "automation tools."]'
    )
    image = models.ImageField(upload_to='banner/', blank=True, null=True)         # Background image
    banner_photo = models.ImageField(                                             # Banner photo
        upload_to='banner/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )

    def __str__(self):
        return f"{self.title_part1} {self.title_part2}"



# models.py
from django.db import models

class CounterData(models.Model):
    years_experience = models.PositiveIntegerField(default=0)  # e.g., 10
    years_suffix = models.CharField(max_length=10, blank=True, null=True, default="+")  # e.g., "+"
    completed_projects = models.PositiveIntegerField(default=0)  # e.g., 143
    projects_suffix = models.CharField(max_length=10, blank=True, null=True)  # e.g., ""
    happy_customers = models.PositiveIntegerField(default=0)  # e.g., 114
    customers_suffix = models.CharField(max_length=10, blank=True, null=True)  # e.g., ""
    honors_awards = models.PositiveIntegerField(default=0)  # e.g., 20
    honors_suffix = models.CharField(max_length=10, blank=True, null=True, default="+")  # e.g., "+"

    def __str__(self):
        return "Counter Data"



# models.py
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)  # e.g., Web Development
    description = models.TextField()          # e.g., "Lorem ipsum dolor sit amet..."
    order = models.PositiveIntegerField(default=0)  # Optional: To control the display order

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']  # Ensures services appear in the specified order



# models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Testimonial(models.Model):
    name = models.CharField(max_length=100)  # e.g., Paul Trueman
    designation = models.CharField(max_length=100)  # e.g., Template Author
    description = models.TextField()  # e.g., "Working with Artur has been a pleasure..."
    star_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=5,
    )
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)  # Optional photo

    def __str__(self):
        return f"{self.name} ({self.designation})"



# models.py
from django.db import models

class PricingPlan(models.Model):
    title = models.CharField(max_length=100)  # e.g., Starter Price
    price = models.CharField(max_length=50)  # e.g., FREE, $29, $2999
    duration = models.CharField(max_length=10, blank=True, null=True)  # e.g., h, m (hours/months), or None
    features = models.JSONField()  # Store features as a list of dictionaries
    popular = models.BooleanField(default=False)  # Highlight the plan as "popular"
    note = models.TextField(blank=True, null=True)  # Optional note (e.g., "Free only when ordering paid services")

    def __str__(self):
        return self.title
