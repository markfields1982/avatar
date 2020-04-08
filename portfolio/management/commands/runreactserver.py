from django.conf import settings
from portfolio.management.commandclasses import SubprocessCommand


class Command(SubprocessCommand):
    help = 'Runs Portfolio reactserver'
    commands = [
        f'cd {settings.REACTSERVER_PATH} ; ' +
        settings.REACTSERVER_ENV + ' npm run start:server',
    ]
