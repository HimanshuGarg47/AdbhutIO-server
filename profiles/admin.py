from django.contrib import admin

from .modelAdmin import *
from .models import *

# Register your models here.
# admin.site.register(Company)
admin.site.register(TemplateProjectSkill)
admin.site.register(SocialProfile)
admin.site.register(Role, RoleAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtistFeedback, ArtistFeedbackAdmin)
admin.site.register(ProjectDemo, ProjectDemoAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectFee, ProjectFeeAdmin)
admin.site.register(ArtistRequest, ArtistRequestAdmin)

admin.site.register(TemplateProjects, TemplateProjectsAdmin)

admin.site.register(Manager)
admin.site.register(ChatGPTMessage)
