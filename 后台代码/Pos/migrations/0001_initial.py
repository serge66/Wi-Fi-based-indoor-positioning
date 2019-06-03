# Generated by Django 2.1.4 on 2019-05-25 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='关联号')),
                ('ap', models.CharField(max_length=256, verbose_name='指纹 AP 组')),
                ('model', models.CharField(max_length=24, unique=True, verbose_name='学习模型')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('lid', models.AutoField(max_length=5, primary_key=True, serialize=False, verbose_name='地点编号')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='地点名称')),
                ('longitude', models.CharField(max_length=10, verbose_name='经度')),
                ('latitude', models.CharField(max_length=10, verbose_name='纬度')),
                ('apnum', models.IntegerField(max_length=3, verbose_name='AP 数量')),
            ],
        ),
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False, verbose_name='信号强度号')),
                ('apid', models.IntegerField(verbose_name='指纹 AP 编号')),
                ('bssid', models.CharField(max_length=17, unique=True, verbose_name='BSSID')),
                ('strength', models.IntegerField(verbose_name='信号强度')),
                ('lid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Pos.Location')),
            ],
        ),
        migrations.AddField(
            model_name='ap',
            name='lid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Pos.Location'),
        ),
    ]
