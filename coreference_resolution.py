import spacy
import os
import string
import random
import time
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
    file_name = ''.join(c for c in str(doc)[0:75] if c.isalnum())
    reference_cluster_file = os.path.join(dir, "%s.txt" % file_name)
    clusters = doc._.coref_clusters

    if clusters == None:
        return

    while True:
        try:
            with open(reference_cluster_file, "a+") as f:
                f.write(str(clusters))
                break
        except (OSError, IOError):
            while not os.path.exists(reference_cluster_file):
                tf.logging.info("%s does not exist." % reference_cluster_file)
                time.sleep(0.1)
