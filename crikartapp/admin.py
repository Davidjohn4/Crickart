from django.contrib import admin
from django.contrib.auth.models import Group
#from .models import registaration
from .models import player_register
from .models import team_register
#from .models import sport_product
from .models import Product
from .models import order
from .models import feedback

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','amount','name', 'email', 'address1', 'city', 'state', 'zip_code', 'phone'
					]

class PlayerAdmin(admin.ModelAdmin):
	list_display = ['pname','pemail', 'pnumber', 'date'
					]

class TeamAdmin(admin.ModelAdmin):
	list_display = ['id','team_name','college_name', 'captain_name', 'college_address', 'email_id', 'team_logo', 'date'
					]	

class FeedAdmin(admin.ModelAdmin):
	list_display = ['id','fname','email', 'phone', 'message'
					]

# Register your models here.
admin.site.unregister(Group)
#admin.site.register(registaration)
admin.site.register(player_register,PlayerAdmin)
admin.site.register(team_register,TeamAdmin)
#admin.site.register(sport_product)
admin.site.register(Product)
admin.site.register(order,OrderAdmin)
admin.site.register(feedback,FeedAdmin)