import spacy
import os
import string
import random
import json
import tensorflow as tf

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


def run_coreference_resolution(data, dir):
    doc = nlp(data)
    save_clusters_to_file(dir, doc)

    return doc._.coref_resolved


def save_clusters_to_file(dir, doc):
    reference_cluster_file = os.path.join(dir, "%s.json" % random_file_name_generator())
    clusters = doc._.coref_clusters

    with open(reference_cluster_file, "w") as f:
        json.dump({str(doc): str(clusters)}, f)


def random_file_name_generator():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64))
