from django.contrib import admin
from models import *
# Register your models here.

admin.site.register(DisasterDescription)
admin.site.register(DisasterProposal)
admin.site.register(SosReports)
admin.site.register(DecisionsOrgs)
admin.site.register(Orgs)
admin.site.register(ContactNumbersOrgs)
admin.site.register(ContactMailsOrgs)
admin.site.register(AddressOrgs)
admin.site.register(MessagesOrgs)
admin.site.register(MessagesFromAdmin)
admin.site.register(DisasterApprovalAdmin)

