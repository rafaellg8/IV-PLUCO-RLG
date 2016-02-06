from django.contrib import admin
from foros.models import Comment,Forum
from plucoApp.models import UserProfile
#importamos de plucoApp los modelos
# Register your models here.

# Add in this class to customized the Admin Interface
class ForumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('theme',)}

admin.site.register(Comment)
admin.site.register(Forum, ForumAdmin)
admin.site.register(UserProfile)
