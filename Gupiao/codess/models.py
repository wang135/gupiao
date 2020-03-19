# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TestsgujuDailyBasic(models.Model):
    ts_code = models.CharField(max_length=100, blank=True, null=True)
    exchange = models.CharField(max_length=100, blank=True, null=True)
    td_date = models.CharField(max_length=100)
    close = models.FloatField(blank=True, null=True)
    turnover_rate = models.FloatField(blank=True, null=True)
    turnover_rate_f = models.FloatField(blank=True, null=True)
    volume_ratio = models.FloatField(blank=True, null=True)
    pe = models.FloatField(blank=True, null=True)
    pe_ttm = models.FloatField(blank=True, null=True)
    pb = models.FloatField(blank=True, null=True)
    ps = models.FloatField(blank=True, null=True)
    ps_ttm = models.FloatField(blank=True, null=True)
    total_share = models.FloatField(blank=True, null=True)
    float_share = models.FloatField(blank=True, null=True)
    free_share = models.FloatField(blank=True, null=True)
    total_mv = models.FloatField(blank=True, null=True)
    circ_mv = models.FloatField(blank=True, null=True)
    codess = models.ForeignKey('TestsgujuStockBasic', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Testsguju_daily_basic'


class TestsgujuDayhangqing(models.Model):
    ts_code = models.CharField(max_length=100, blank=True, null=True)
    td_date = models.CharField(max_length=100)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    fudu = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    vol = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    huanshou = models.FloatField(blank=True, null=True)
    codess = models.ForeignKey('TestsgujuStockBasic', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Testsguju_dayhangqing'


class TestsgujuStockBasic(models.Model):
    symbol = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    area = models.CharField(max_length=25)
    industry = models.CharField(max_length=100)
    fullname = models.CharField(max_length=20)
    enname = models.CharField(max_length=18)
    market = models.CharField(max_length=100)
    exchange = models.CharField(max_length=100)
    curr_type = models.CharField(max_length=100)
    list_status = models.CharField(max_length=100)
    list_date = models.CharField(max_length=100)
    delist_date = models.CharField(max_length=18)
    is_hs = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Testsguju_stock_basic'


class TestsgujuStockCompany(models.Model):
    ts_code = models.CharField(max_length=100, blank=True, null=True)
    exchange = models.CharField(max_length=100, blank=True, null=True)
    chairman = models.CharField(max_length=100, blank=True, null=True)
    manager = models.CharField(max_length=100, blank=True, null=True)
    secretary = models.CharField(max_length=100, blank=True, null=True)
    reg_capital = models.CharField(max_length=100, blank=True, null=True)
    setup_date = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    introduction = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    employees = models.CharField(max_length=100, blank=True, null=True)
    main_business = models.CharField(max_length=100, blank=True, null=True)
    business_scope = models.CharField(max_length=100, blank=True, null=True)
    codess = models.ForeignKey(TestsgujuStockBasic, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Testsguju_stock_company'


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Dayhangqing(models.Model):
    time = models.CharField(max_length=50, blank=True, null=True)
    opens = models.CharField(max_length=255, blank=True, null=True)
    closes = models.CharField(max_length=255, blank=True, null=True)
    high = models.CharField(max_length=255, blank=True, null=True)
    low = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=255, blank=True, null=True)
    volumemoney = models.CharField(max_length=255, blank=True, null=True)
    huanshou = models.CharField(max_length=255, blank=True, null=True)
    names = models.CharField(max_length=255, blank=True, null=True)
    codes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dayhangqing'


class Dayhangqing1(models.Model):
    time = models.CharField(max_length=50, blank=True, null=True)
    opens = models.CharField(max_length=255, blank=True, null=True)
    closes = models.CharField(max_length=255, blank=True, null=True)
    high = models.CharField(max_length=255, blank=True, null=True)
    low = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=255, blank=True, null=True)
    volumemoney = models.CharField(max_length=255, blank=True, null=True)
    huanshou = models.CharField(max_length=255, blank=True, null=True)
    names = models.CharField(max_length=255, blank=True, null=True)
    codes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dayhangqing1'


class Dayhangqing2(models.Model):
    time = models.DateField(blank=True, null=True)
    opens = models.CharField(max_length=255, blank=True, null=True)
    closes = models.CharField(max_length=255, blank=True, null=True)
    high = models.CharField(max_length=255, blank=True, null=True)
    low = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=255, blank=True, null=True)
    volumemoney = models.CharField(max_length=255, blank=True, null=True)
    huanshou = models.CharField(max_length=255, blank=True, null=True)
    names = models.CharField(max_length=255, blank=True, null=True)
    codes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dayhangqing2'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Fenshihangqing(models.Model):
    times = models.CharField(max_length=50, blank=True, null=True)
    names = models.CharField(max_length=50, blank=True, null=True)
    codes = models.CharField(max_length=50, blank=True, null=True)
    buy = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    avgjg = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fenshihangqing'


class Hussheng(models.Model):
    names = models.CharField(max_length=255, blank=True, null=True)
    ids = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hussheng'


class Ww(models.Model):
    ww = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ww'
