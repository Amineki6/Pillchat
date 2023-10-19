from django.core.management.base import BaseCommand
import pandas as pd
from personal.models import table

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('tableUpdate.csv', sep=';')
        for ID,TITLEandLABELER,TITLE,LABELER,RXCUI,STRENGTH,QUERY in zip(df.ids , df.TITLEandLABELER, df.TITLE, df.LABELER, df.RXCUI, df.STRENGTH, df.QUERY):
            models = table(ids=ID,
                title_labeler=TITLEandLABELER,
                title=TITLE,
                labeler=LABELER,
                rxcui=RXCUI,
                strength=STRENGTH,
                query=QUERY)
            models.save()