# Generated by Django 3.2.7 on 2021-09-24 21:50

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortcut_user_id', models.CharField(default='me', max_length=40)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('selected_category_id', models.IntegerField(blank=True, default=1)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('reputation', models.IntegerField(default=0)),
                ('position', models.CharField(default='member', max_length=50)),
                ('subject_of_memo', models.CharField(max_length=60)),
                ('skill_note_reputation', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, max_length=20)),
                ('public', models.CharField(default='yes', max_length=5)),
                ('github', models.CharField(default='www.github.com', max_length=20)),
                ('site2', models.CharField(blank=True, max_length=20)),
                ('site1', models.CharField(blank=True, max_length=20)),
                ('site3', models.CharField(blank=True, max_length=20)),
                ('site4', models.CharField(blank=True, max_length=20)),
                ('completecount', models.IntegerField(default=0)),
                ('uncompletecount', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
