# Generated by Django 4.1.7 on 2023-03-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Khalti', 'Khalti')], default='Cash On Delivery', max_length=100, null=True),
        ),
    ]
