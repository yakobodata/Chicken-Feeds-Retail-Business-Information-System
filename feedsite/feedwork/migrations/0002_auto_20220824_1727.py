# Generated by Django 3.2.7 on 2022-08-24 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedwork', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='expenses',
            new_name='indirect_expenses',
        ),
        migrations.CreateModel(
            name='direct_expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('unit_price', models.DecimalField(decimal_places=4, default=0.0, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=4, default=0.0, max_digits=10)),
                ('expense_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.expense_names')),
                ('expense_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.expense_units')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedwork.purchases')),
            ],
        ),
    ]