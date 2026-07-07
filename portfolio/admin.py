from django.contrib import admin
from .models import Profile, Tag, SkillCategory, TimelineEntry, Project


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role_title', 'email', 'phone')

    def has_add_permission(self, request):
        # Only one Profile row should ever exist.
        return not Profile.objects.exists()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    filter_horizontal = ('skills',)


@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_label', 'order')
    list_editable = ('order',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
