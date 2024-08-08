from django.contrib import admin
from .models import Profile
from .models import Player

# admin.site.register(Profile)


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'age', 'img_preview']    #, 
    list_display_links = ['id', 'name', 'surname']
    list_editable = ['age']
    search_fields = ['name', 'age']
    list_filter = ['age']
    # list_per_page = 1
    

@admin.register(Player)
class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'img_link','mail', 'img_preview', 'flag_img_link', 'flag_preview', 'Best_position']  
    list_editable = ['Best_position']
    # fields = ['id', 'name', 'img_link','mail', 'img_preview'] #
    # readonly_fields = ['img_preview']

