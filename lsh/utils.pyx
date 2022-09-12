def shingles(str text, int char_ngram = 5):
    cdef int head
    cdef set result = set()

    for head in range(0, len(text) - char_ngram):
        result.add(text[head:head + char_ngram])
    
    return result


def jaccard(str s1, str s2):
    set1 = shingles(s1)
    set2 = shingles(s2)

    cdef float jaccard_sim = 0
    cdef Py_ssize_t length_intersect = 0
    if len(set1) + len(set2) > 0:
        length_intersect = len(set1 & set2)
        jaccard_sim = float(length_intersect) / float(len(set1) + len(set2) - length_intersect)

    return jaccard_sim
