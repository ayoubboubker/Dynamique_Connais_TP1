import json
from pyld import jsonld


def read_file(file_path):
    f = open(file_path)
    return json.load(f)



def main():
    context = read_file('TP1-Contexte.json')
    raw_doc  = read_file('trace.json')
    expanded = jsonld.expand(raw_doc, {'expandContext': context})
    rdf = jsonld.normalize(expanded, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})
    with open("Transfo.nq", "w", encoding="utf-8") as f:
        f.write(rdf)

main()