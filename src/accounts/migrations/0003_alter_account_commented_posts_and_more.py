# Generated by Django 4.1.6 on 2023-03-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_comment_post'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='commented_posts',
            field=models.ManyToManyField(related_name='commented_users', to='posts.post', verbose_name='Прокомментированные публикации'),
        ),
        migrations.AlterField(
            model_name='account',
            name='liked_posts',
            field=models.ManyToManyField(related_name='liked_users', to='posts.post', verbose_name='Понравившиеся публикации'),
        ),
    ]
