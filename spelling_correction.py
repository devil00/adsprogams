def damerau_levenshtein_distance(s1, s2):
    '''
    Compute the damreau levenshtein distance betwweb string s1 and s2.
    '''
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in xrange(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in xrange(-1,lenstr2+1):
        d[(-1,j)] = j+1
 
    for i in xrange(lenstr1):
        for j in xrange(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
 
    return d[lenstr1-1,lenstr2-1]


class SpellingCorrection(object):
    def correct(self, words_dic, unspelled_word):
        possible_match = []
        # spelling will match to any of the word in dic  when damreau 
        # levenshtein distance is equals to 1.
        for w in words_dic:
            if damerau_levenshtein_distance(w, unspelled_word) == 1:
                possible_match.append(w)
        print possible_match

if __name__ == "__main__":
    sc = SpellingCorrection()
    sc.correct(['axle', 'mauti', 'maruty', 'maurti',
                'marutix', 'mymaruti', 'applem'], 'maruti')



