from django.core.management.base import BaseCommand, CommandError
from unesco.models import (
    Site, States, Iso, Region, Category,
)

from django.db.models import ObjectDoesNotExist

import pandas as pd
import numpy as np

class Command(BaseCommand):
    help = 'Help text for the command here'

    def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        print("INFO: loading csv...")
        self.csv_df = pd.read_csv("data/whc-sites-2018-small.csv")
        print("INFO: normalizing data...")
        self.normalize_data()
        # TODO: wipe out database
        print("INFO: loading to database...")
        self.load_to_database()
        
    def load_to_database(self):
        """ load data """
        # load all region -> all state -> all category -> all site
        # OR: load each row
        for index, row in self.csv_df.iterrows():
            if (index % 100 == 0):
                print("loading index", index)

            # load Region:(name)
            region = self.model_loader_handle(Region, name=row['region'])

            # load Iso:(name)
            iso = self.model_loader_handle(Iso, name=row['iso'])

            # load State:(name, *region)
            state = self.model_loader_handle(States, name=row['states'])

            # load Category:(name)
            category = self.model_loader_handle(Category, name=row['category'])

            area_hectares = row['area_hectares'] if float(row['area_hectares']) else None
            justification = row['justification'] if str(row['justification'])  else ''

            # load Site:(name, year, description, justification, longitude, latitude, area_hectares, *category, *state)
            site = self.model_loader_handle(Site,
                name=row['name'],
                year=row['year'],
                description=row['description'],
                justification=justification,
                longitude=row['longitude'],
                latitude=row['latitude'],
                area_hectares=area_hectares,
                category=category,
                state=state,
                iso=iso,
                region=region
            )
    
    def model_loader_handle(self, model, **kwargs):
        try:
            return model.objects.get(**kwargs)
        except ObjectDoesNotExist:
            # print("ObjectDoesNotExist: ", model, kwargs)
            pass
        
        try:
            model_instance = model(**kwargs)
            return model_instance.save()
        except:
            if model == Site:
                import ipdb; ipdb.set_trace()
                print("not exist but also create model or save failed: ", model, kwargs)
            return None
    
    def normalize_data(self):
        """ numerical data processing """
        # not a number -> null
        # Integer: `year`
        def transform_integer_column(column_value):
            return int(column_value)
    
        # Float: `longitude, latitude, area_hectares`
        def transform_float_column(column_value):
            return float(column_value)
        
        self.transform_columns(self.csv_df, 
            ['year', 'longitude', 'latitude', 'area_hectares'],
            [transform_integer_column] + [transform_float_column]*3
        )
    
    def transform(self, df, index, column_value, column_name, transform_func):
        # validate
        if not column_value:
            df.loc[index, column_name] = np.NaN

        # transformation
        df.loc[index, column_name] = transform_func(column_value)
    
    def transform_columns(self, df, column_names_list, transform_func_list):
        for index, row in df.iterrows():
            for column_index, column_name in enumerate(column_names_list):
                self.transform(df, index, row[column_name], column_name, transform_func_list[column_index])




    
# reference
# https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/