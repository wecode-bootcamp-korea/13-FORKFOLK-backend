# Generated by Django 3.1.2 on 2020-10-22 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='RelatedStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'related_stories',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('description', models.TextField()),
                ('related_stories', models.ManyToManyField(through='story.RelatedStory', to='story.Story')),
            ],
            options={
                'db_table': 'stories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.maincategory')),
            ],
            options={
                'db_table': 'sub_categories',
            },
        ),
        migrations.CreateModel(
            name='StoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.story')),
            ],
            options={
                'db_table': 'story_images',
            },
        ),
        migrations.AddField(
            model_name='story',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.subcategory'),
        ),
        migrations.AddField(
            model_name='relatedstory',
            name='from_story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_story', to='story.story'),
        ),
        migrations.AddField(
            model_name='relatedstory',
            name='to_story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_story', to='story.story'),
        ),
    ]
