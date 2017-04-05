from django.contrib import admin

from web.models import CarImgLikeViewTb
from web.models import CommonCodeTb
from web.models import MemberTb
from web.models import VehicleDataTb
from web.models import VehicleImgTb

# Register your models here.


class CarImgLikeViewTbAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'vh_img_id', 'bool_like', 'hits')


class CommonCodeTbAdmin(admin.ModelAdmin):
    list_display = ('group_cd', 'group_cd_nm', 'common_cd', 'common_cd_nm', 'upper_common_cd',
                    'upper_group_cd', 'attribute', 'order', 'use')


class MemberTbAdmin(admin.ModelAdmin):
    list_display = ('mem_id', 'mem_userid', 'pw', 'name', 'age', 'sex', 'job', 'reg_date')


class VehicleDataTbAdmin(admin.ModelAdmin):
    list_display = ('model_cd', 'detail_model_cd', 'vh_info_cd', 'vh_info_value')


class VehicleImgTbAdmin(admin.ModelAdmin):
    list_display = ('vh_img_id', 'model_cd', 'color_cd', 'package_cd',
                    'angle_cd', 'weather_cd', 'date', 'update_time', 'use')


admin.site.register(CarImgLikeViewTb, CarImgLikeViewTbAdmin)
admin.site.register(CommonCodeTb, CommonCodeTbAdmin)
admin.site.register(MemberTb, MemberTbAdmin)
admin.site.register(VehicleDataTb, VehicleDataTbAdmin)
admin.site.register(VehicleImgTb, VehicleImgTbAdmin)
