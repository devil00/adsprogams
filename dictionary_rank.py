class DictionaryRank(object):
    def compute(self, letters_array, word):
        '''
        Find out the rank of a word from the given array of letters.
        :param letters_array: list of letters
        :type letters_array: list
        :param word: word whose rank will be found out.
        :type word: str
        '''
        # Get all the possible arrangements of letters.
        possible_permutations = self.permute(letters_array, 0,
                                             len(letters_array))
        # Sort all possible arrangements.
        possible_permutations = sorted(possible_permutations)

        # If word is available in possible arrangements, print the rank
        # rank = index + 1 (since index starts with 0)
        try:
            rank = possible_permutations.index(word) + 1
            print 'Rank of {} is {}'.format(word, rank)
        except ValueError:
            print 'No Rank'


    def permute(self, letters_array, start, end, results=[]):
        '''
        Method determines all the possible arrangements using back tracking 
        approach. All the arrangements will be stores in param results
        '''
        if start==end:
            results.append("".join(letters_array))
        else:
            for i in range(start, end):
                letters_array[start], letters_array[i] = \
                        letters_array[i], letters_array[start]
                self.permute(letters_array, start+1, end)
                letters_array[start], letters_array[i] = \
                        letters_array[i], letters_array[start]
        return results


if __name__ == "__main__":
    dic_rank = DictionaryRank()
    dic_rank.compute(['a', 'r', 'c'], 'arc')
