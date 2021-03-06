# Generated by Django 3.2.6 on 2022-01-18 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accountsapp', '0007_address_is_primary'),
        ('food', '0004_cuisine_foodcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuisine',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='foodcategory',
            name='is_active',
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('name', models.CharField(default='', max_length=40)),
                ('imageId', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('pickup_location', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='chef_profile', to='accountsapp.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='chef_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('status', '-activate_date'),
                'abstract': False,
            },
        ),
    ]
