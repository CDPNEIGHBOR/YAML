from pprint import pprint
import yaml


with open(r"C:\Users\Stephen Hendry\PycharmProjects\YAML\stephen.yaml", 'r') as file:
    yaml_data = yaml.load(file, Loader=yaml.FullLoader)

pprint(yaml_data)


