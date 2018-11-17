import spacy

nlp = spacy.load('en_coref_md')

def tag_parts_of_speech(text):
    doc = nlp(text)
    pos = []

    for token in doc:
        pos.append(token.pos_)

    return pos

def get_antecedent(text):
    doc = nlp(text)

    if doc._.has_coref:
        clusters = doc._.coref_clusters
        ant = {}

        for cluster in clusters:
            if cluster.main.__len__() == 1 and cluster.main[0].pos_ == 'NOUN':
                ant[cluster.main[0].text] = cluster.main[0].i
            else:
                for token in cluster.main:
                    if token.pos_ == 'NOUN':
                        ant[token.text] = token.i
        return ant
    else:
        return None
