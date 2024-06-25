import pandas as pd
import spacy
import fr_core_news_md
# import re
import os


def load_data():
    base_path = os.path.dirname(__file__)

    seg_df = pd.read_csv(
        os.path.join(base_path, 'data/fra.segmentations'),
        names=["source", "target", "features", "segmentation"],
        sep="\t"
    )

    deriv_df = pd.read_csv(
        os.path.join(base_path, 'data/fra.derivations'),
        names=["source", "target", "features", "derivation"],
        sep="\t")
    return seg_df, deriv_df


nlp_fr = spacy.load("fr_core_news_md")


def prepare_data(seg_df, deriv_df):
    dict_uni_2_spacy = {
        'ADJ': 'ADJ',
        'N': 'NOUN',
        'V': 'VERB',
        'ADV': 'ADV',
        'U': 'X'
    }

    # Process segmentation data
    seg_target = seg_df["target"].tolist()
    seg_features = seg_df["features"].tolist()
    seg = seg_df["segmentation"].tolist()

    seg_features_left = [feature.split("|")[0].split(";")[0]
                         for feature in seg_features]

    seg_features_left = [x if x != '' else 'N'
                         for x in seg_features_left]

    seg_features_left = [dict_uni_2_spacy[item]
                         for item in seg_features_left]

    seg_target_pos = [(word, pos)
                      for word, pos in zip(seg_target, seg_features_left)]

    seg_dict = {}
    for k, v in zip(seg_target_pos, seg):
        if k not in seg_dict:
            seg_dict[k] = []
        seg_dict[k].append(v)

    for k in seg_dict:
        seg_dict[k] = list(set(seg_dict[k]))

    seg_dict = {key: val for key, val in sorted(seg_dict.items(), key = lambda ele: ele[1])}

    # Process derivation data
    deriv_source = deriv_df["source"].tolist()
    deriv_target = deriv_df["target"].tolist()
    deriv_features = deriv_df["features"].tolist()
    deriv = deriv_df["derivation"].tolist()

    deriv_features_right = [feature.split(":")[1]
                            for feature in deriv_features]

    deriv_features_right = [dict_uni_2_spacy[item]
                            for item in deriv_features_right]

    deriv_target_pos = [(word, pos)
                        for word, pos in zip(deriv_target, deriv_features_right)]

    deriv_dict = {}
    for k, v in zip(deriv_target_pos, deriv):
        if k not in deriv_dict:
            deriv_dict[k] = []
        deriv_dict[k].append(v)

    for k in deriv_dict:
        deriv_dict[k] = list(set(deriv_dict[k]))


    deriv_dict = {key: val for key, val in sorted(deriv_dict.items(), key = lambda ele: ele[1])}

    
    deriv_lemme_dict = {}
    for k, v in zip(deriv_target_pos, deriv_source):
        if k not in deriv_lemme_dict:
            deriv_lemme_dict[k] = []
        deriv_lemme_dict[k].append(v)

    for k in deriv_lemme_dict:
        deriv_lemme_dict[k] = list(set(deriv_lemme_dict[k]))

    deriv_lemme_dict = {key: val for key, val in sorted(deriv_lemme_dict.items(), key = lambda ele: ele[1])}

    return seg_dict, deriv_dict, deriv_lemme_dict


seg_df, deriv_df = load_data()
seg_dict, deriv_dict, deriv_lemme_dict = prepare_data(seg_df, deriv_df)


def seg_flex(token, seg_dict):
    findings = []
    if token in seg_dict:
        find = seg_dict[token][0].split("|")
        if len(find) > 1:
            findings.append([find[0], "#" + "".join(find[1:])])

    if len(findings) > 0:
        return findings, True
    return findings, False


def seg_deriv(token, deriv_dict, deriv_lemme_dict):
    findings = []
    if token in deriv_dict:
        find = deriv_dict[token][0].split("-")
        if find[0] != '':
            findings.append([find[0] + "?", deriv_lemme_dict[token][0]])
        if find[1] != '':
            findings.append([deriv_lemme_dict[token][0], "?" + find[1]])

    if len(findings) > 0:
        return findings, True
    return findings, False


def flatten_arr(data):
    """Flattens a list of strings using list comprehension."""
    return [item for sublist in data for item in sublist]


def tokenize(text, flatten_output=True):
    """
    Tokenizes the input text and performs morphological segmentation.

    Parameters:
    text (str): The input text to be tokenized.
    flatten_output (bool): Whether to flatten the output list. Defaults to True.

    Returns:
    list: A list of tokenized words with morphological segmentation.
          If flatten_output is True, the list is flattened.

    Example:
    tokenize("Une phrase qui sers d'exemple.")
    ['Une', 'phrase', 'qui', 'servir', '#s', "d'", 'exemple', '.']
    """
    
    # Process the input text with the NLP model
    text_pos = nlp_fr(text)

    # Create a list of tuples with word and part-of-speech (POS) tag
    word_and_pos = [(token.text, 'VERB') if token.pos_ == 'AUX' else (
        token.text, token.pos_) for token in text_pos]

    findings = []

    for token in word_and_pos:
        bool_seg_f = False
        bool_seg_d = False

        if token[1] in ['NOUN', 'ADJ', 'VERB', 'ADV']:
            liste_flex, bool_seg_f = seg_flex(token, seg_dict)
            if bool_seg_f:
                token = (liste_flex[0][0], token[1])
            liste_deriv, bool_seg_d = seg_deriv(
                token, deriv_dict, deriv_lemme_dict)

        if bool_seg_f is False and bool_seg_d is False:
            findings.append([token[0]])
        else:
            if len(liste_flex) > 0 and len(liste_deriv) > 0:
                findings.append(
                    [liste_deriv[0][0], liste_deriv[0][1], liste_flex[0][1]])
            elif len(liste_flex) > 0:
                findings.append(liste_flex[0])
            else:
                findings.append(liste_deriv[0])

    if flatten_output:
        return flatten_arr(findings)

    return findings
