# Generated by Django 4.1 on 2022-08-23 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gardener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('planting_zone', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IssueCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=50)),
                ('date_planted', models.DateField()),
                ('producing', models.BooleanField()),
                ('url', models.CharField(default='https://i.etsystatic.com/33348027/r/il/ec1edb/3609190565/il_1588xN.3609190565_n82r.jpg', max_length=2000)),
                ('perennial', models.BooleanField()),
                ('gardener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mommasgardenapi.gardener')),
            ],
        ),
        migrations.CreateModel(
            name='PlantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_date', models.DateField()),
                ('url', models.CharField(default='https://i.etsystatic.com/33348027/r/il/ec1edb/3609190565/il_1588xN.3609190565_n82r.jpg', max_length=2000)),
                ('note', models.CharField(max_length=500)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mommasgardenapi.plant')),
            ],
        ),
        migrations.AddField(
            model_name='plant',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mommasgardenapi.planttype'),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('url', models.CharField(default='https://i.etsystatic.com/33348027/r/il/ec1edb/3609190565/il_1588xN.3609190565_n82r.jpg', max_length=2000)),
                ('solution', models.CharField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mommasgardenapi.issuecategory')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mommasgardenapi.plant')),
            ],
        ),
    ]
