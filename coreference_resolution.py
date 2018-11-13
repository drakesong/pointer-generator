import spacy
import os
import string
import random
import time
import ast
import re
import tensorflow as tf

nlp = spacy.load('en_coref_md')

def run_coreference_resolution(data, dir):
    doc = nlp(data)
    save_clusters_to_file(dir, doc)

    return doc._.coref_resolved


def save_clusters_to_file(dir, doc):
    d = {}
    clusters = doc._.coref_clusters
    if clusters == None:
        return
    else:
        for cluster in clusters:
            l = []
            mentions = cluster.mentions
            for mention in mentions:
                l.append(str(mention))
            d[str(cluster.main)] = l

    reference_cluster_file = create_file_path(dir, doc)
    while True:
        try:
            with open(reference_cluster_file, "a+") as f:
                f.write(str(d))
                break
        except (OSError, IOError):
            while not os.path.exists(reference_cluster_file):
                tf.logging.info("%s does not exist." % reference_cluster_file)
                time.sleep(0.1)


def add_pronouns(dir, data):
    doc = nlp(data)
    reference_cluster_file = create_file_path(dir, doc)
    saved_clusters = search_for_saved_references(reference_cluster_file)

    if saved_clusters == None:
        return data

    saved_clusters = ast.literal_eval(saved_clusters)
    clusters = doc._.coref_clusters

    if clusters == None:
        return data

    doc_list = re.findall(r"[\w']+|[^\s\w]", doc.text)
    for cluster in clusters:
        try:
            saved_mentions = saved_clusters[str(cluster.main)]
            mentions = cluster.mentions
            for mention in mentions:
                doc_list[mention.start:mention.end] = mention.text
        except:
            continue

    return str.join(" ", doc_list)

def search_for_saved_references(file):
    try:
        with open(file, "r") as f:
            saved_clusters = f.read()
            print(saved_clusters)
        return saved_clusters if saved_clusters != "None" else None
    except:
        return None


def create_file_path(dir, doc):
    file_name = ''.join(c for c in str(doc)[0:75] if c.isalnum())
    return os.path.join(dir, "%s.txt" % file_name)
