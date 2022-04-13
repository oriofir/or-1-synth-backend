# Generated by Django 4.0.4 on 2022-04-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('or1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='synth',
            name='delay_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='synth',
            name='filter_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='synth',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='synth',
            name='synth_type',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]