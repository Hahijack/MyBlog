# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_nick_name', models.CharField(default=b'', max_length=24, verbose_name='\u7528\u6237\u6635\u79f0')),
                ('user_gender', models.CharField(default=b'1', max_length=10, verbose_name='\u6027\u522b\u9009\u62e9', choices=[(b'1', b'\xe7\x94\xb7'), (b'0', b'\xe5\xa5\xb3')])),
                ('user_birday', models.DateField(null=True, verbose_name='\u7528\u6237\u751f\u65e5', blank=True)),
                ('user_mobile', models.CharField(max_length=11, null=True, verbose_name='\u7535\u8bdd\u53f7\u7801', blank=True)),
                ('user_address', models.CharField(default=b'', max_length=200, verbose_name='\u7528\u6237\u5730\u5740')),
                ('user_detail', models.CharField(default=b'', max_length=200, verbose_name='\u4e2a\u4eba\u7b80\u4ecb')),
                ('user_image', models.ImageField(default=b'image/user/default.png', upload_to=b'image/user/%Y/%m', verbose_name='\u7528\u6237\u5934\u50cf')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8868',
                'verbose_name_plural': '\u7528\u6237\u8868',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Acimage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_title', models.CharField(default=b'', max_length=20, verbose_name='\u56fe\u7247\u6807\u9898')),
                ('image_detail', models.CharField(default=b'', max_length=200, verbose_name='\u56fe\u7247\u7b80\u4ecb')),
                ('image_path', models.ImageField(default=b'upload/default.jpg', upload_to=b'upload/%Y/%m', verbose_name='\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u7f51\u7ad9\u76f8\u518c',
                'verbose_name_plural': '\u7f51\u7ad9\u76f8\u518c',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_title', models.CharField(default=b'', max_length=50, verbose_name='\u65e5\u5fd7\u6807\u9898')),
                ('article_synopsis', models.TextField(default=b'', verbose_name='\u65e5\u5fd7\u7b80\u4ecb')),
                ('article_image', models.ImageField(default=b'image/article/default.png', upload_to=b'image/article/%Y/%m', verbose_name='\u6587\u7ae0\u914d\u56fe')),
                ('article_tag', models.CharField(default=b'', max_length=50, verbose_name='\u65e5\u5fd7\u6807\u7b7e')),
                ('article_content', models.TextField(default=b'', verbose_name='\u535a\u5ba2\u6b63\u6587')),
                ('article_type', models.CharField(default=b'0', max_length=10, verbose_name='\u6587\u7ae0\u7c7b\u522b', choices=[(b'0', '\u8349\u7a3f'), (b'1', b'\xe8\xbd\xaf\xe5\x88\xa0\xe9\x99\xa4'), (b'2', b'\xe6\xad\xa3\xe5\xb8\xb8')])),
                ('article_original', models.CharField(default=b'1', max_length=10, verbose_name='\u662f\u5426\u539f\u521b', choices=[(b'1', b'\xe5\x8e\x9f\xe5\x88\x9b'), (b'0', b'\xe8\xbd\xac\xe8\xbd\xbd')])),
                ('article_click', models.PositiveIntegerField(default=0, verbose_name='\u6587\u7ae0\u70b9\u51fb\u91cf')),
                ('article_up', models.CharField(default=b'0', max_length=10, verbose_name='\u6587\u7ae0\u7f6e\u9876', choices=[(b'1', '\u7f6e\u9876'), (b'0', b'\xe5\x8f\x96\xe6\xb6\x88\xe7\xbd\xae\xe9\xa1\xb6')])),
                ('article_support', models.CharField(default=b'0', max_length=10, verbose_name='\u6587\u7ae0\u63a8\u8350', choices=[(b'1', '\u63a8\u8350'), (b'0', b'\xe5\x8f\x96\xe6\xb6\x88\xe6\x8e\xa8\xe8\x8d\x90')])),
                ('article_create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article_update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u8868',
                'verbose_name_plural': '\u6587\u7ae0\u8868',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(default=b'', max_length=20, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('category_detail', models.CharField(default=b'', max_length=100, verbose_name='\u5206\u7c7b\u4ecb\u7ecd')),
                ('category_icon', models.CharField(default=b'', max_length=100, verbose_name='\u5206\u7c7b\u56fe\u6807')),
                ('category_sort_id', models.IntegerField(default=1, verbose_name='\u5206\u7c7b\u6392\u5e8f')),
            ],
            options={
                'verbose_name': '\u535a\u5ba2\u5206\u7c7b',
                'verbose_name_plural': '\u535a\u5ba2\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Siteinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(default=b'', max_length=20, verbose_name='\u7ad9\u70b9\u540d\u79f0')),
                ('site_detail', models.CharField(default=b'', max_length=100, verbose_name='\u7ad9\u70b9\u4ecb\u7ecd')),
                ('site_logo', models.ImageField(default=b'image/site/default.png', upload_to=b'image/site/', verbose_name='\u7ad9\u70b9logo')),
                ('site_topimage', models.ImageField(default=b'image/site/topbg.jpg', upload_to=b'image/site/', verbose_name='\u9876\u90e8\u5927\u56fe')),
                ('site_powered', models.TextField(default=b'', verbose_name='Powered By')),
                ('site_links', models.TextField(default=b'', verbose_name='links')),
                ('site_contact', models.TextField(default=b'', verbose_name='contact me')),
                ('site_footer', models.TextField(default=b'', verbose_name='\u7ad9\u70b9\u5e95\u90e8\u4ee3\u7801')),
                ('site_changyan', models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\xba\x95\xe9\x83\xa8\xe5\xb9\xbf\xe5\x91\x8a\xe4\xbb\xa3\xe7\xa0\x81')),
                ('site_user', models.ForeignKey(verbose_name='\u7ba1\u7406\u5458', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u7f51\u7ad9\u4fe1\u606f',
                'verbose_name_plural': '\u7f51\u7ad9\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5206\u7c7b', blank=True, to='blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='article_user',
            field=models.ForeignKey(verbose_name='\u6587\u7ae0\u4f5c\u8005', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
