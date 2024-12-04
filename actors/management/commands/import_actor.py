from django.core.management.base import BaseCommand, CommandParser
import csv
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='nome do arquivo csv'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                actor = Actor.objects.all()
                try:
                    if actor.filter(name=row['name']).exists():
                        print(f'já existe esse ator {row['name']} no banco de dados')
                        break
                    actor.create(
                        name=row['name'],
                        birthday=row['birthday'],
                        nationality=row['nationality']
                    )
                except:
                    raise 'houve um erro no salvamento'
