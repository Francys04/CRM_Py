# Generated by Django 4.0.10 on 2023-09-05 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_alter_team_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='memebers',
            new_name='members',
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='team.plan'),
        ),
    ]