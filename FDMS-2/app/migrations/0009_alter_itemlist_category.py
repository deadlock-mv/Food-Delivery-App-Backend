# Generated by Django 4.1.3 on 2023-02-28 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_foodorder_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='app.categorylist'),
        ),
    ]
