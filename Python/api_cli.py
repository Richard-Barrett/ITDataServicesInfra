import click


@click.group()
def API():
        """A CLI wrapper for the API of ITDataServicesInfra."""


if __name__ == '__main__':
    API(prog_name='ITDataServicesInfra')
