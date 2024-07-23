import click
import pickle
import os
from nook.utils import save, HashMap

if os.path.isfile('hashmap.pickle'):
    pass
else:
    dictionary = HashMap()
    with open('hashmap.pickle', 'wb') as f:
        pickle.dump(dictionary, f)


@click.command(help='adds the key pair value')
@click.option('-k', '--key',help='key to add')
@click.option('-v', '--value',help='value to add')
@save
def add(loaded, key, value):
    loaded.set(key, value)
    click.echo(f'added key-pair \n[{key}]:[{value}]')


@click.command(help='deletes the key-pair value')
@click.option('-k', '--key',help ='requires the key to delete')
@save
def delete(loaded, key):
    loaded.remove_item(key)
    click.echo(f'deleted pair')


@click.command(help='retrieves the key-pair value')
@click.option('-k', '--key',help ='requires key')
@save
def getvalue(loaded, key):
    click.echo(loaded.get(key))