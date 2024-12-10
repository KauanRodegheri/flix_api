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
            linha = int(input('qual linha deseja começar? '))
            cont = 0
            for row in csv_reader:
                cont += 1
                if cont >= linha - 1:
                    try:
                        if actor.filter(name=row['name'], birthday=row['birthday']).exists():
                            while True:
                                opc = input(f"o ator {row['name']} ja existe, deseja inserir mesmo assim?").lower()
                                match opc:
                                    case "n":
                                        list_actors_repeat.append(row['name'])
                                        break
                                    case "s":
                                        self.create_actor(actor, row['name'], row['birthday'], row['nationality'])
                                        break
                                    case _:
                                        continue
                        else:
                            self.create_actor(actor, row['name'], row['birthday'], row['nationality'])
                            self.stdout.write(self.style.SUCCESS(f"ator {row['name']} cadastrado"))
                    except Exception as error:
                        print(f'houve um erro no salvamento {error}')
        if list_actors_repeat:
            self.stdout.write(self.style.NOTICE(f'actors exists in database: {list_actors_repeat}'))
        else:
            self.stdout.write(self.style.SUCCESS('Todos atores cadastrados com sucesso'))

    def create_actor(self, queryset, name, birthday, nationality):
        queryset.create(
            name=name,
            birthday=datetime.strptime(birthday, '%Y-%m-%d').date(),
            nationality=nationality
        )
