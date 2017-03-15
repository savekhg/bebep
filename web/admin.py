from django.contrib import admin

from web.models import CarImgLikeViewTb
from web.models import CommonCodeTb
from web.models import MemberTb
from web.models import VehicleDataTb
from web.models import VehicleImgTb
from web.models import AuthGroup
from web.models import AuthGroupPermissions
from web.models import AuthPermission
from web.models import AuthUser
from web.models import AuthUserGroups
from web.models import AuthUserUserPermissions
from web.models import DjangoAdminLog
from web.models import DjangoContentType
from web.models import DjangoMigrations
from web.models import DjangoSession

admin.site.register(CarImgLikeViewTb)
admin.site.register(CommonCodeTb)
admin.site.register(MemberTb)
admin.site.register(VehicleDataTb)
admin.site.register(VehicleImgTb)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)

# Register your models here.
