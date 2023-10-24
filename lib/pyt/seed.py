import click

@click.command()

@click.option('--name', '-n', default= 'Joe', help='Firstname description')


def main(name):
    print('Hello World my name is {}'.format(name))
    
    
    
    
    
    
if __name__  == '__main__':
    main()

