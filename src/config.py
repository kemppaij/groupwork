from configparser import ConfigParser
import os

def config(filename=None, section='postgresql'):
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), 'database.ini')
    parser = ConfigParser()
    parser.read(filename)
    return dict(parser.items(section))