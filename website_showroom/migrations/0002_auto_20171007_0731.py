# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import website_showroom.models


class Migration(migrations.Migration):

    dependencies = [
        ('website_showroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='active_color',
            field=models.CharField(help_text='Format: #ffffff', max_length=7),
        ),
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(help_text='Format: #ffffff', max_length=7),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Only used in admin context, not displayed on site (edition specific category names)', max_length=40),
        ),
        migrations.AlterField(
            model_name='edition',
            name='contact_title',
            field=models.CharField(help_text='Title of contact navi', max_length=40),
        ),
        migrations.AlterField(
            model_name='edition',
            name='country',
            field=models.CharField(help_text="2-letter-country-code for showing a corresponding flag (e.g. 'de', 'en'). Careful, not existing code will break site.", max_length=2),
        ),
        migrations.AlterField(
            model_name='edition',
            name='facebook_url',
            field=models.CharField(blank=True, help_text='Optional, link to Facebook page', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='edition',
            name='footer_left',
            field=models.CharField(help_text='Left footer (HTML tags possible)', max_length=200),
        ),
        migrations.AlterField(
            model_name='edition',
            name='footer_right',
            field=models.CharField(help_text='Right footer (HTML tags possible)', max_length=200),
        ),
        migrations.AlterField(
            model_name='edition',
            name='google_plus_url',
            field=models.CharField(blank=True, help_text='Optional, link to Google+ page', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='edition',
            name='home_menu_active_color',
            field=models.CharField(help_text="HTML color code, e.g. '#000000", max_length=7),
        ),
        migrations.AlterField(
            model_name='edition',
            name='home_menu_color',
            field=models.CharField(help_text="HTML color code, e.g. '#999999", max_length=7),
        ),
        migrations.AlterField(
            model_name='edition',
            name='home_menu_title',
            field=models.CharField(help_text="Something like - e.g. - 'Home'", max_length=40),
        ),
        migrations.AlterField(
            model_name='edition',
            name='home_num_websites',
            field=models.IntegerField(help_text='Number of websites for home category'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='html_title',
            field=models.CharField(help_text='Used for html title tag', max_length=100),
        ),
        migrations.AlterField(
            model_name='edition',
            name='order',
            field=models.IntegerField(help_text='Numeric value for edition order. Tip: Use 100-200-300-... steps for easy reordering. Edition first in order will be used as edition default.'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='rss_description',
            field=models.CharField(help_text='Description for rss feed', max_length=200),
        ),
        migrations.AlterField(
            model_name='edition',
            name='rss_title',
            field=models.CharField(help_text='Title for rss feed', max_length=100),
        ),
        migrations.AlterField(
            model_name='edition',
            name='short_description',
            field=models.CharField(help_text="Something like 'English version', used for mouseover on flag", max_length=40),
        ),
        migrations.AlterField(
            model_name='edition',
            name='site_subtitle',
            field=models.CharField(help_text='Subtitle (HTML tags possible)', max_length=125),
        ),
        migrations.AlterField(
            model_name='edition',
            name='site_title',
            field=models.CharField(help_text='Main title shown on page', max_length=40),
        ),
        migrations.AlterField(
            model_name='edition',
            name='twitter_url',
            field=models.CharField(blank=True, help_text='Optional, link to Twitter page', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='editioncategory',
            name='name',
            field=models.CharField(help_text='Edition specific category name', max_length=40),
        ),
        migrations.AlterField(
            model_name='editioncategory',
            name='order',
            field=models.IntegerField(help_text='Numeric value for category order. Tip: Use 100-200-300-... steps for easy reordering.'),
        ),
        migrations.AlterField(
            model_name='editioncategory',
            name='url_name',
            field=models.SlugField(help_text="Every url-conform string except 'contact' (e.g. 'my-category-1')", max_length=40),
        ),
        migrations.AlterField(
            model_name='editionwebsite',
            name='desc',
            field=models.TextField(help_text='Edition specific description'),
        ),
        migrations.AlterField(
            model_name='editionwebsite',
            name='order',
            field=models.IntegerField(help_text='Numeric value for website order. Tip: Use 100-200-300-... steps for easy reordering.'),
        ),
        migrations.AlterField(
            model_name='editionwebsite',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='editionwebsite',
            name='title',
            field=models.CharField(blank=True, help_text='Edition specific title, if left empty, generic title is used', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='country',
            field=models.CharField(blank=True, help_text="Optional, 2-letter-country-code for showing a corresponding flag (e.g. 'de', 'en'). Careful, not existing code will break site.", max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='website',
            name='screenshot',
            field=models.ImageField(help_text='Image file, size: 300x200, name will be unified. Larger file image will be resized. Greater height will be cropped (making screen capture with website width and height generously higher than aspect ratio is easiest)', upload_to=website_showroom.models.get_path),
        ),
        migrations.AlterField(
            model_name='website',
            name='title',
            field=models.CharField(help_text='Generic title, used if no extra edition specific title is provided', max_length=50),
        ),
    ]
