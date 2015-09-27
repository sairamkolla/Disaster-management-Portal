from django.contrib import admin
from organisation.models import *
# Register your models here.

admin.site.register(Orgs)
admin.site.register(Contact_Numbers_Orgs)
admin.site.register(Contact_Mails_Orgs)
admin.site.register(Name_Orgs)
admin.site.register(Address_Org)
admin.site.register(Messages_Orgs)
admin.site.register(Messages_From_Admin)
admin.site.register(Notifications_Org)
