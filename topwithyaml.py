#!/usr/bin/env python3

import yaml
from pprint import pprint
with open(r"C:\Users\Stephen Hendry\PycharmProjects\YAML\topology.yaml", 'r') as yaml_topology:
	yaml_data = yaml.load(yaml_topology, Loader=yaml.FullLoader)

pprint(yaml_data)
