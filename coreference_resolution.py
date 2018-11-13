import spacy
import os
import string
import random
import time
import tensorflow as tf

nlp = spacy.load('en_coref_md')

def run_coreference_resolution(data, dir):
    doc = nlp(data)
    save_clusters_to_file(dir, doc)

    return doc._.coref_resolved


def save_clusters_to_file(dir, doc):
    dict = {}
    clusters = doc._.coref_clusters
    if clusters == None:
        return
    else:
        for cluster in clusters:
            list = []
            mentions = cluster.mentions
            for mention in mentions:
                list.append(str(mention))
            dict[str(cluster.main)] = list

    reference_cluster_file = create_file_path(dir, doc)
    while True:
        try:
            with open(reference_cluster_file, "a+") as f:
                f.write(str(dict))
                break
        except (OSError, IOError):
            while not os.path.exists(reference_cluster_file):
                tf.logging.info("%s does not exist." % reference_cluster_file)
                time.sleep(0.1)


def create_file_path(dir, doc):
    file_name = ''.join(c for c in str(doc)[0:75] if c.isalnum())
    return os.path.join(dir, "%s.txt" % file_name)
