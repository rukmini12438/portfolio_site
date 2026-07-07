from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    """
    Singleton-style model holding the hero/about content.
    Only the first row is ever used — see Profile.get_solo().
    """
    name = models.CharField(max_length=100, default='Rukmini')
    role_title = models.CharField(
        max_length=150,
        default='Full-Stack Django Developer',
        help_text="Shown as the eyebrow label in the hero section.",
    )
    headline = models.CharField(
        max_length=200,
        default='Building products layer by layer.',
        help_text="Main hero heading. Wrap the word you want highlighted in **double asterisks**.",
    )
    intro = models.TextField(
        default=(
            "I'm Rukmini — a B.Tech CS student who designs and ships complete web "
            "applications end-to-end: Django backends, REST APIs, and interfaces "
            "people actually enjoy using."
        )
    )
    about_heading = models.CharField(
        max_length=250,
        default="I like building things that go from a blank Django project to something a real user can log into.",
    )
    about_body = models.TextField(
        default=(
            "I'm currently pursuing my B.Tech in Computer Science & IT at Ajay Kumar "
            "Garg Engineering College, Ghaziabad (2023–2027). Outside coursework, I "
            "build full production-style Django applications module by module — "
            "custom user roles, JWT authentication, REST APIs, and dashboards that "
            "update in real time."
        )
    )
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    github_url = models.URLField(blank=True, default='https://github.com/rukmini12438')
    linkedin_url = models.URLField(blank=True, default='https://www.linkedin.com/in/rukmini-96b005287')
    leetcode_url = models.URLField(blank=True, default='https://leetcode.com/u/Rukmini2025')

    grad_year = models.CharField(max_length=20, default='2027')
    leetcode_count = models.CharField(max_length=20, default='200+')

    class Meta:
        verbose_name = 'Profile (hero & about content)'
        verbose_name_plural = 'Profile (hero & about content)'

    def __str__(self):
        return f'Profile: {self.name}'

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Tag(models.Model):
    """A single reusable label — used both for skill chips and project tech tags."""
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    """A grouping column in the Skills section, e.g. 'Backend', 'Frontend'."""
    name = models.CharField(max_length=60)
    description = models.TextField(
        blank=True,
        help_text="Optional explanatory text shown under the category title — use this for System Design to explain what it covers.",
    )
    order = models.PositiveIntegerField(default=0)
    skills = models.ManyToManyField(Tag, related_name='skill_categories', blank=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Skill categories'

    def __str__(self):
        return self.name


class TimelineEntry(models.Model):
    """A single row in the 'Journey' timeline section."""
    date_label = models.CharField(max_length=60, help_text="e.g. '2023 — 2027' or 'Ongoing'")
    title = models.CharField(max_length=150)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Timeline entries'

    def __str__(self):
        return self.title


class Project(models.Model):
    """One portfolio project card."""

    STATUS_CHOICES = [
        ('live', 'Live build'),
        ('progress', 'In progress'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='live')
    short_description = models.TextField()
    screenshot = models.ImageField(upload_to='projects/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
