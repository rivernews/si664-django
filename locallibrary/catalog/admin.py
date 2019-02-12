from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User


# Define the admin class
# def group(self, user):
#     groups = []
#     for group in user.groups.all():
#         groups.append(group.name)
#     return ' '.join(groups)
# group.short_description = 'Groups'

# # The last argument will display a column with the result of the "group" method defined above
# UserAdmin.list_display = list(UserAdmin.list_display) + [
#     'group'
# ]
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
    list_filter = ('language',)

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    # what to show when click into detail of a book instance in /admin
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass