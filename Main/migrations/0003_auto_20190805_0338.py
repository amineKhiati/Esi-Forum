# Generated by Django 2.2.4 on 2019-08-05 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_remove_profile_date_naissance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='numero_telephone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='promotion',
            field=models.CharField(choices=[('1cpi', '1CPI'), ('2cpi', '2CPI'), ('1cs', '1CS'), ('2cs', '2CS'), ('3cs', '3CS')], default='1cpi', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='publication_enregistrer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.Publication'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique=True),
        ),
    ]