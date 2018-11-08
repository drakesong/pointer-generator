import spacy

nlp = spacy.load('en_coref_md')

def visualize_coreference_resolution(data):
    doc = nlp(data)

    print()
    print("Printing document...")
    print(doc)
    print()
    print("Printing clusters...")
    print(doc._.coref_clusters)
    print()
    print("Printing resolved...")
    print(doc._.coref_resolved)
    print()


def run_coreference_resolution(data):
    doc = nlp(data)
    return doc._.coref_resolved
