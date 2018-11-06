import spacy

nlp = spacy.load('en_coref_md')

def run_coreference_resolution(data):
    doc = nlp(data)
    print(doc)
    print(doc._.coref_clusters)
