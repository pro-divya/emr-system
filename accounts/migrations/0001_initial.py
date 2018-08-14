# Generated by Django 2.1 on 2018-08-14 05:20

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('organizations', '0002_auto_20180814_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('type', models.CharField(choices=[('CLT', 'Client'), ('GP', 'General Practice')], max_length=3)),
                ('is_medidata', models.BooleanField(default=False, help_text='Designates that this user can create Other Organization users', verbose_name='Medidata status')),
                ('is_client_admin', models.BooleanField(default=False, help_text='Designates that this user can create their client users', verbose_name='Client Admin status')),
                ('is_practice_manager', models.BooleanField(default=False, help_text='Designates that this user can create their gp users', verbose_name='GP Manager status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfileBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255)),
                ('maiden_name', models.CharField(blank=True, max_length=255)),
                ('date_of_birth', models.DateField()),
                ('address_name_number', models.CharField(max_length=255)),
                ('address_line2', models.CharField(max_length=255)),
                ('address_line3', models.CharField(max_length=255)),
                ('address_line4', models.CharField(max_length=255)),
                ('address_postcode', models.CharField(max_length=255)),
                ('address_country', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephone_home', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('telephone_mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
            options={
                'verbose_name': 'User Profile Base',
                'verbose_name_plural': 'User Profile Bases',
            },
        ),
        migrations.CreateModel(
            name='ClientUser',
            fields=[
                ('userprofilebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.UserProfileBase')),
                ('organization_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.OrganizationClient')),
            ],
            options={
                'verbose_name': 'Client User',
            },
            bases=('accounts.userprofilebase',),
        ),
        migrations.CreateModel(
            name='GeneralPracticeUser',
            fields=[
                ('userprofilebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.UserProfileBase')),
                ('gp_code', models.CharField(max_length=255)),
                ('payment_bank_holder_name', models.CharField(max_length=255)),
                ('payment_bank_account_number', models.CharField(max_length=255)),
                ('payment_bank_sort_code', models.CharField(max_length=255)),
                ('can_complete_amra', models.BooleanField(default=False)),
                ('can_complete_sars', models.BooleanField(default=False)),
                ('organization_gp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.OrganizationGeneralPractice')),
            ],
            options={
                'verbose_name': 'General Practice User',
            },
            bases=('accounts.userprofilebase',),
        ),
        migrations.AddField(
            model_name='userprofilebase',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
