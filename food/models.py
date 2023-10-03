# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brand(models.Model):
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Brand'


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category'


class Food(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    carbohydrate = models.FloatField(blank=True, null=True)
    sugar = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    cholesterol = models.FloatField(blank=True, null=True)
    saturate_fat = models.FloatField(blank=True, null=True)
    trans_fat = models.FloatField(blank=True, null=True)
    hydrate = models.FloatField(blank=True, null=True)
    saccharose = models.FloatField(blank=True, null=True)
    glucose = models.FloatField(blank=True, null=True)
    fructose = models.FloatField(blank=True, null=True)
    lactose = models.FloatField(blank=True, null=True)
    maltose = models.FloatField(blank=True, null=True)
    dietary_fiber = models.FloatField(blank=True, null=True)
    calcium = models.FloatField(blank=True, null=True)
    iron = models.FloatField(blank=True, null=True)
    magnesium = models.FloatField(blank=True, null=True)
    phosphorus = models.FloatField(blank=True, null=True)
    kalium = models.FloatField(blank=True, null=True)
    zinc = models.FloatField(blank=True, null=True)
    copper = models.FloatField(blank=True, null=True)
    manganese = models.FloatField(blank=True, null=True)
    selenium = models.FloatField(blank=True, null=True)
    beta_carotene = models.FloatField(blank=True, null=True)
    vitamin_d3 = models.FloatField(db_column='vitamin_D3', blank=True, null=True)  # Field name made lowercase.
    tocopherol = models.FloatField(blank=True, null=True)
    tocotrienols = models.FloatField(blank=True, null=True)
    vitamin_b1 = models.FloatField(db_column='vitamin_B1', blank=True, null=True)  # Field name made lowercase.
    vitamin_b2 = models.FloatField(db_column='vitamin_B2', blank=True, null=True)  # Field name made lowercase.
    niacin = models.FloatField(blank=True, null=True)
    folate = models.FloatField(blank=True, null=True)
    vitamin_b12 = models.FloatField(db_column='vitamin_B12', blank=True, null=True)  # Field name made lowercase.
    vitamin_c = models.FloatField(db_column='vitamin_C', blank=True, null=True)  # Field name made lowercase.
    amino_acid = models.FloatField(blank=True, null=True)
    isoleucine = models.FloatField(blank=True, null=True)
    leucine = models.FloatField(blank=True, null=True)
    lysine = models.FloatField(blank=True, null=True)
    methionine = models.FloatField(blank=True, null=True)
    phenylalanine = models.FloatField(blank=True, null=True)
    threonine = models.FloatField(blank=True, null=True)
    valine = models.FloatField(blank=True, null=True)
    histidine = models.FloatField(blank=True, null=True)
    arginine = models.FloatField(blank=True, null=True)
    tyrosine = models.FloatField(blank=True, null=True)
    cysteine = models.FloatField(blank=True, null=True)
    alanine = models.FloatField(blank=True, null=True)
    aspartic_acid = models.FloatField(blank=True, null=True)
    glutamic_acid = models.FloatField(blank=True, null=True)
    glycine = models.FloatField(blank=True, null=True)
    proline = models.FloatField(blank=True, null=True)
    serine = models.FloatField(blank=True, null=True)
    butyric_acid = models.FloatField(blank=True, null=True)
    caproic_acid = models.FloatField(blank=True, null=True)
    caprylic_acid = models.FloatField(blank=True, null=True)
    capric_acid = models.FloatField(blank=True, null=True)
    lauric_acid = models.FloatField(blank=True, null=True)
    myristic_acid = models.FloatField(blank=True, null=True)
    palmitic_acid = models.FloatField(blank=True, null=True)
    stearic_acid = models.FloatField(blank=True, null=True)
    arachidic_acid = models.FloatField(blank=True, null=True)
    myristoleic_acid = models.FloatField(blank=True, null=True)
    palmitoleic_acid = models.FloatField(blank=True, null=True)
    oleic_acid = models.FloatField(blank=True, null=True)
    vaccenic_acid = models.FloatField(blank=True, null=True)
    gadoleic_acid = models.FloatField(blank=True, null=True)
    linoleic_acid = models.FloatField(blank=True, null=True)
    alpha_linolenic_acid = models.FloatField(blank=True, null=True)
    gamma_linolenic_acid = models.FloatField(blank=True, null=True)
    eicosadienoic_acid = models.FloatField(blank=True, null=True)
    arachidonic_acid = models.FloatField(blank=True, null=True)
    eicosatrienoic_acid = models.FloatField(blank=True, null=True)
    eicosapentaenoic_acid = models.FloatField(blank=True, null=True)
    docosapentaenoic_acid = models.FloatField(blank=True, null=True)
    docosahexaenoic_acid = models.FloatField(blank=True, null=True)
    trans_oleic_acid = models.FloatField(blank=True, null=True)
    trans_linoleic_acid = models.FloatField(blank=True, null=True)
    trans_linolenic_acid = models.FloatField(blank=True, null=True)
    ash = models.FloatField(blank=True, null=True)
    caffeine = models.FloatField(blank=True, null=True)
    retinol = models.FloatField(blank=True, null=True)
    sugar_alcohol = models.FloatField(blank=True, null=True)
    erythritol = models.FloatField(blank=True, null=True)
    iodine = models.FloatField(blank=True, null=True)
    chloride = models.FloatField(blank=True, null=True)
    vitamin_d = models.FloatField(db_column='vitamin_D', blank=True, null=True)  # Field name made lowercase.
    vitamin_d1 = models.FloatField(db_column='vitamin_D1', blank=True, null=True)  # Field name made lowercase.
    vitamin_e = models.FloatField(db_column='vitamin_E', blank=True, null=True)  # Field name made lowercase.
    vitamin_k = models.FloatField(db_column='vitamin_K', blank=True, null=True)  # Field name made lowercase.
    vitamin_k1 = models.FloatField(db_column='vitamin_K1', blank=True, null=True)  # Field name made lowercase.
    vitamin_k2 = models.FloatField(db_column='vitamin_K2', blank=True, null=True)  # Field name made lowercase.
    pantothenic_acid = models.FloatField(blank=True, null=True)
    vitamin_b6 = models.FloatField(db_column='vitamin_B6', blank=True, null=True)  # Field name made lowercase.
    biotin = models.FloatField(blank=True, null=True)
    choline = models.FloatField(blank=True, null=True)
    tryptophan = models.FloatField(blank=True, null=True)
    taurine = models.FloatField(blank=True, null=True)
    omega_3_fatty_acids = models.FloatField(blank=True, null=True)
    total_unsaturated_fats = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Food'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BrandsBrand(models.Model):
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands_brand'


class CategoriesCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'categories_category'


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
    id = models.BigAutoField(primary_key=True)
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


class FoodsFood(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    energy = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    carbohydrate = models.FloatField(blank=True, null=True)
    sugar = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    cholesterol = models.FloatField(blank=True, null=True)
    saturate_fat = models.FloatField(blank=True, null=True)
    trans_fat = models.FloatField(blank=True, null=True)
    brand = models.ForeignKey(BrandsBrand, models.DO_NOTHING)
    category = models.ForeignKey(CategoriesCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'foods_food'


class JtFoodBrandBrandFood(models.Model):
    foodid = models.PositiveIntegerField(db_column='Foodid', primary_key=True)  # Field name made lowercase. The composite primary key (Foodid, Brandid) found, that is not supported. The first column is selected.
    brandid = models.PositiveIntegerField(db_column='Brandid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jt_Food_Brand_Brand_Food'
        unique_together = (('foodid', 'brandid'),)


class KnoxAuthtoken(models.Model):
    digest = models.CharField(primary_key=True, max_length=128)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    expiry = models.DateTimeField(blank=True, null=True)
    token_key = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'knox_authtoken'
