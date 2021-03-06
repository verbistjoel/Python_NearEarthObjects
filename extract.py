"""Extract data on NEOS and CAs from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of
`NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON
file, formatted as described in the project instructions, into a collection
of `CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.
"""

import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []  # create list of neo objects
    with open(neo_csv_path) as f:
        reader = csv.reader(f)
        next(reader)
        # parse row of csv into pdes(design.) ,name,diameter, and hazardous
        for row in reader:
            if row[3] is not None or row[3] != '':
                if row[7] == 'Y':
                    H = True
                else:
                    H = False
                # create Neo obj with designation,name,diameter,hazardous
                neo_obj = NearEarthObject(row[3], row[4], row[15], H)
                neos.append(neo_obj)    # append obj to the list
    return neos


def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about
    close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as f:
        contents = json.load(f)  # Parse JSON data into a Python object.
    contents = contents['data']   # just grab the data part
    approaches = []    # create list of approach objects
    for item in contents:
        if item[0] is not None or item[0] != '':
            # create approach obj designation,name, distance, velocity
            app_obj = CloseApproach(item[0], item[3],  item[4], item[7])
            approaches.append(app_obj)     # append approach obj to list
    return approaches
