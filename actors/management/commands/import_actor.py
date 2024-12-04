from django.core.management.base import BaseCommand
import csv
from actors.models import Actor
from datetime import datetime

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
            actor = Actor.objects.all()
            list_actors_repeat = []
            for row in csv_reader:
                try:
                    if actor.filter(name=row['name']).exists():
                        list_actors_repeat.append(row['name'])
                    else:
                        actor.create(
                            name=row['name'],
                            birthday=datetime.strptime(row['birthday'], '%Y-%m-%d').date(),
                            nationality=row['nationality']
                        )
                        self.stdout.write(self.style.SUCCESS(f'ator {row['name']} cadastrado'))
                except Exception as error:
                    print(f'houve um erro no salvamento {error}')
        if list_actors_repeat:
            self.stdout.write(self.style.NOTICE(f'actors exists in database: {list_actors_repeat}'))
        else:
            self.stdout.write(self.style.SUCCESS('Todos atores cadastrados com sucesso'))