# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_search_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_id', models.IntegerField()),
                ('geo_id', models.CharField(max_length=50)),
                ('file_as_name', models.CharField(max_length=70)),
                ('pct_ownership', models.DecimalField(decimal_places=0, max_digits=14)),
                ('dba_name', models.CharField(max_length=50)),
                ('addr_line1', models.CharField(max_length=60)),
                ('addr_line2', models.CharField(max_length=60)),
                ('addr_line3', models.CharField(max_length=60)),
                ('addr_city', models.CharField(max_length=50)),
                ('addr_state', models.CharField(max_length=50)),
                ('addr_zip', models.CharField(max_length=10)),
                ('ml_deliverable', models.CharField(max_length=1)),
                ('abs_subdv_cd', models.CharField(max_length=10)),
                ('abs_subdv_ref', models.CharField(max_length=50)),
                ('abs_subdv_desc', models.CharField(max_length=60)),
                ('block', models.CharField(max_length=50)),
                ('tract_or_lot', models.CharField(max_length=50)),
                ('legal_desc', models.CharField(max_length=255)),
                ('legal_desc_2', models.CharField(max_length=255)),
                ('mapsco', models.CharField(max_length=20)),
                ('condo_pct', models.DecimalField(decimal_places=10, max_digits=13)),
                ('situs_num', models.CharField(max_length=15)),
                ('situs_street_prefx', models.CharField(max_length=10)),
                ('situs_street', models.CharField(max_length=50)),
                ('situs_street_sufix', models.CharField(max_length=10)),
                ('situs_city', models.CharField(max_length=30)),
                ('situs_state', models.CharField(max_length=2)),
                ('situs_zip', models.CharField(max_length=10)),
                ('situs_display', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=5)),
                ('school', models.CharField(max_length=5)),
                ('tif', models.CharField(max_length=5)),
                ('exemptions', models.CharField(max_length=100)),
                ('all_entities', models.CharField(max_length=100)),
                ('deed_book_id', models.CharField(max_length=20)),
                ('deed_book_page', models.CharField(max_length=20)),
                ('deed_num', models.CharField(max_length=50)),
                ('deed_dt', models.DateTimeField()),
                ('deed_type_cd', models.CharField(max_length=10)),
                ('legal_acreage', models.DecimalField(decimal_places=4, max_digits=14)),
                ('eff_size_acres', models.DecimalField(decimal_places=4, max_digits=14)),
                ('land_sqft', models.DecimalField(decimal_places=2, max_digits=18)),
                ('land_total_sqft', models.DecimalField(decimal_places=2, max_digits=18)),
                ('living_area', models.DecimalField(decimal_places=0, max_digits=14)),
                ('state_cd', models.CharField(max_length=10)),
                ('class_cd', models.CharField(max_length=10)),
                ('property_use_cd', models.CharField(max_length=10)),
                ('prop_type_cd', models.CharField(max_length=5)),
                ('commercial_flag', models.CharField(max_length=1)),
                ('eff_yr_blt', models.DecimalField(decimal_places=0, max_digits=4)),
                ('yr_blt', models.DecimalField(decimal_places=0, max_digits=4)),
                ('zoning', models.CharField(max_length=50)),
                ('land_type_cd', models.CharField(max_length=10)),
                ('beds', models.CharField(max_length=20)),
                ('baths', models.CharField(max_length=20)),
                ('stories', models.IntegerField()),
                ('units', models.IntegerField()),
                ('percent_complete', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pool', models.CharField(max_length=1)),
                ('prop_create_dt', models.DateTimeField()),
                ('property_status', models.CharField(max_length=50)),
                ('curr_val_yr', models.DecimalField(decimal_places=0, max_digits=4)),
                ('curr_imprv_hstd_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_imprv_non_hstd_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_land_hstd_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_land_non_hstd_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_ag_use_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_ag_market', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_market', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_ag_loss', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_appraised_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_ten_percent_cap', models.DecimalField(decimal_places=0, max_digits=14)),
                ('curr_assessed_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_val_yr', models.DecimalField(decimal_places=0, max_digits=4)),
                ('cert_imprv_hstd_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_imprv_non_hstd_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_land_hstd_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_land_non_hstd_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_ag_use_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_ag_market', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_market', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_ag_loss', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_appraised_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_ten_percent_cap', models.DecimalField(decimal_places=0, max_digits=14)),
                ('cert_assessed_val', models.DecimalField(decimal_places=0, max_digits=14)),
                ('parent_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('parent_id', models.IntegerField()),
                ('parent_block', models.CharField(max_length=50)),
                ('parent_tract', models.CharField(max_length=50)),
                ('parent_acres', models.DecimalField(decimal_places=4, max_digits=14)),
            ],
        ),
    ]
