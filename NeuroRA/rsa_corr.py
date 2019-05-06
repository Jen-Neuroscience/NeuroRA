# -*- coding: utf-8 -*-

' a module for calculating the correlation coefficient between two RDMs '

__author__ = 'Zitong Lu'

import numpy as np
from scipy.stats import spearmanr
from scipy.stats import pearsonr

' a function for calculating the Spearman correlation coefficient between two RDMs '
def rsa_correlation_spearman(RDM1, RDM2):

    cons = np.shape(RDM1)[0]

    n = 0

    while cons > 1:
        n = n + cons - 1
        cons = cons - 1

    nn = 0

    v1 = np.zeros([n], dtype=np.float64)
    v2 = np.zeros([n], dtype=np.float64)

    cons = np.shape(RDM1)[0]

    for i in range(cons-1):

        for j in range(cons-1-i):

            v1[nn] = RDM1[i, i+j+1]
            v2[nn] = RDM2[i, i+j+1]

            print(RDM1[i, i+j+1])

            nn = nn + 1

    return spearmanr(v1, v2)

' a function for calculating the Pearson correlation coefficient between two RDMs '
def rsa_correlation_pearson(RDM1, RDM2):
    cons = np.shape(RDM1)[0]

    n = 0

    while cons > 1:
        n = n + cons - 1
        cons = cons - 1

    nn = 0

    v1 = np.zeros([n], dtype=np.float64)
    v2 = np.zeros([n], dtype=np.float64)

    cons = np.shape(RDM1)[0]

    for i in range(cons - 1):

        for j in range(cons - 1 - i):
            v1[nn] = RDM1[i, i + j + 1]
            v2[nn] = RDM2[i, i + j + 1]

            nn = nn + 1

    return pearsonr(v1, v2)

' a function for calculating the Cosine Similarity between two RDMs '

def rsa_similarity(RDM1, RDM2):

    cons = np.shape(RDM1)[0]

    n = 0

    while cons > 1:
        n = n + cons - 1
        cons = cons - 1

    nn = 0

    v1 = np.zeros([n], dtype=np.float64)
    v2 = np.zeros([n], dtype=np.float64)

    cons = np.shape(RDM1)[0]

    for i in range(cons - 1):

        for j in range(cons - 1 - i):
            v1[nn] = RDM1[i, i + j + 1]
            v2[nn] = RDM2[i, i + j + 1]

            nn = nn + 1

    V1 = np.mat(v1)
    V2 = np.mat(v2)

    num = float(V1 * V2.T)

    denom = np.linalg.norm(V1) * np.linalg.norm(V2)

    cos = num / denom

    similarity = 0.5 + 0.5 * cos

    return similarity

' a fuction for calculating the Euclidean Distances between two RDMs '

def rsa_distance(RDM1, RDM2):
    cons = np.shape(RDM1)[0]

    n = 0

    while cons > 1:
        n = n + cons - 1
        cons = cons - 1

    nn = 0

    v1 = np.zeros([n], dtype=np.float64)
    v2 = np.zeros([n], dtype=np.float64)

    cons = np.shape(RDM1)[0]

    for i in range(cons - 1):

        for j in range(cons - 1 - i):
            v1[nn] = RDM1[i, i + j + 1]
            v2[nn] = RDM2[i, i + j + 1]

            nn = nn + 1

    dist = np.linalg.norm(v1 - v2)

    return dist