# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CarImgLikeViewTb(models.Model):
    member_id = models.CharField(db_column='MEMBER_ID', primary_key=True, max_length=255)  # Field name made lowercase.
    vh_img_id = models.CharField(db_column='VH_IMG_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    bool_like = models.IntegerField(db_column='BOOL_LIKE', blank=True, null=True)  # Field name made lowercase.
    hits = models.IntegerField(db_column='HITS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAR_IMG_LIKE_VIEW_TB'
        #unique_together = (('member_id', 'vh_img_id'),)


class CommonCodeTb(models.Model):
    group_cd = models.CharField(db_column='GROUP_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    group_cd_nm = models.CharField(db_column='GROUP_CD_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    common_cd = models.CharField(db_column='COMMON_CD', primary_key=True, max_length=4)  # Field name made lowercase.
    common_cd_nm = models.CharField(db_column='COMMON_CD_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    upper_common_cd = models.CharField(db_column='UPPER_COMMON_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    upper_group_cd = models.CharField(db_column='UPPER_GROUP_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    attribute = models.CharField(db_column='ATTRIBUTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    order = models.IntegerField(db_column='ORDER', blank=True, null=True)  # Field name made lowercase.
    user = models.IntegerField(db_column='USER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMMON_CODE_TB'


class MemberTb(models.Model):
    mem_id = models.CharField(db_column='MEM_ID', primary_key=True, max_length=255)  # Field name made lowercase.
    mem_userid = models.IntegerField(db_column='MEM_USERID', blank=True, null=True)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=4, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateField(db_column='REG_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEMBER_TB'


class VehicleDataTb(models.Model):
    model_cd = models.CharField(db_column='MODEL_CD', primary_key=True, max_length=4)  # Field name made lowercase.
    detail_model_cd = models.CharField(db_column='DETAIL_MODEL_CD', primary_key=True, max_length=4)  # Field name made lowercase.
    vh_info_cd = models.CharField(db_column='VH_INFO_CD', max_length=4)  # Field name made lowercase.
    vh_info_value = models.CharField(db_column='VH_INFO_VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VEHICLE_DATA_TB'
        #unique_together = (('model_cd', 'detail_model_cd', 'vh_info_cd'),)


class VehicleImgTb(models.Model):
    vh_img_id = models.CharField(db_column='VH_IMG_ID', primary_key=True, max_length=20)  # Field name made lowercase.
    model_cd = models.CharField(db_column='MODEL_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    color_cd = models.CharField(db_column='COLOR_CD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    package_cd = models.CharField(db_column='PACKAGE_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    angle_cd = models.CharField(db_column='ANGLE_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    weather_cd = models.CharField(db_column='WEATHER_CD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='UPDATE_TIME', blank=True, null=True)  # Field name made lowercase.
    use = models.IntegerField(db_column='USE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VEHICLE_IMG_TB'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
