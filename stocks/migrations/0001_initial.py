# Generated by Django 2.0.2 on 2019-04-17 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0003_auto_20190414_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='StocksDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Company')),
            ],
        ),
        migrations.CreateModel(
            name='StocksDatabasePointer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pointer', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='stocksdatabase',
            name='pointer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.StocksDatabasePointer'),
        ),
    ]
