from pprint import pprint
import json
import platform


def get_launches_from_file():
    dict_from_file = dict()
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        ''' linux path '''
        path += '/'
    else:
        '''  windows path  '''
        path += '\\'

    for year in range(1957, 2015):
        d = path + str(year) + '.json'
        with open(d, 'r', encoding="utf8") as inf:
            try:
                ldict = json.loads(inf.read())
            except UnicodeDecodeError as e:
                print(Exception("Codec Error: " + str(e) + " in " + str(d)))
                raise e
            dict_from_file[str(year)] = ldict
    return dict_from_file