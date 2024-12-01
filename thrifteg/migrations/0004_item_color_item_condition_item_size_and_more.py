# Generated by Django 4.2.16 on 2024-11-22 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thrifteg', '0003_alter_cartitem_item_alter_cartitem_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='condition',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Used', 'Used')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]