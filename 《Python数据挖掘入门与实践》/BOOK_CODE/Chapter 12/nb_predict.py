import os
import re
import numpy as np
from mrjob.job import MRJob
from mrjob.step import MRStep
from operator import itemgetter

word_search_re = re.compile(r"[\w']+")


class NaiveBayesTrainer(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.extract_words_mapping,
                   reducer=self.reducer_count_words),
            MRStep(mapper=self.predict_mapper),
            ]

    def extract_words_mapping(self, key, value):
        tokens = value.split()
        gender = eval(tokens[0])
        blog_post = eval(" ".join(tokens[1:]))
        all_words = word_search_re.findall(blog_post)
        all_words = [word.lower() for word in all_words]
        #for word in all_words:
        for word in all_words:
            #yield "{0}:{1}".format(gender, word.lower()), 1
            #yield (gender, word.lower()), (1. / len(all_words))
            # Occurence probability
            yield (gender, word), 1

    def reducer_count_words(self, key, counts):
        s = sum(counts)
        gender, word = key #.split(":")
        yield word, (gender, s)

    def predict_mapper(self, key, value):
        per_gender = {}
        for value in values:
            gender, s = value
            per_gender[gender] = s
        yield word, per_gender

    def ratio_mapper(self, word, value):
        counts = dict(value)
        sum_of_counts = float(np.mean(counts.values()))
        maximum_score = max(counts.items(), key=itemgetter(1))
        current_ratio = maximum_score[1] / sum_of_counts
        yield None, (word, sum_of_counts, value)
    
    def sorter_reducer(self, key, values):
        ranked_list = sorted(values, key=itemgetter(1), reverse=True)
        n_printed = 0
        for word, sum_of_counts, scores in ranked_list:
            if n_printed < 20:
                print((n_printed + 1), word, scores)
                n_printed += 1
            yield word, dict(scores)

if __name__ == '__main__':
    NaiveBayesTrainer.run()
