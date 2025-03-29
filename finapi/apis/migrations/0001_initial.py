# Generated by Django 5.1.7 on 2025-03-29 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CBNData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('exchange_rate_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inflation_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('treasury_bill_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bond_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('interest_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CBN Data',
                'verbose_name_plural': 'CBN Data Entries',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='InvestmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_key', models.CharField(choices=[('treasury_bill', 'Treasury Bill'), ('bond', 'Government Bond'), ('fixed_deposit', 'Fixed Deposit'), ('mutual_fund', 'Mutual Fund'), ('stock', 'Stock Market')], max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Investment Type',
                'verbose_name_plural': 'Investment Types',
                'db_table': 'investment_types',
            },
        ),
        migrations.CreateModel(
            name='UserFinancialProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('total_investment_budget', models.DecimalField(decimal_places=2, help_text='Total investment budget in NGN', max_digits=12)),
                ('investment_goal', models.CharField(choices=[('short_term', 'Short-Term (1-3 years)'), ('medium_term', 'Medium-Term (3-7 years)'), ('long_term', 'Long-Term (7+ years)')], max_length=20)),
                ('risk_tolerance', models.CharField(choices=[('low', 'Low Risk'), ('medium', 'Medium Risk'), ('high', 'High Risk')], max_length=10)),
                ('preferred_investment_duration', models.IntegerField(help_text='Duration in years')),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_return', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('calculation_date', models.DateTimeField(auto_now_add=True)),
                ('cbn_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.cbndata')),
                ('investment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.investmenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.userfinancialprofile')),
            ],
        ),
    ]
