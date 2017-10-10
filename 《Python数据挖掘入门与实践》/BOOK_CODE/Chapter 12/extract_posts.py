import os
import re
from mrjob.job import MRJob
from mrjob.step import MRStep

word_search_re = re.compile(r"[\w']+")


class ExtractPosts(MRJob):

    post_start = False
    post = []

    def mapper(self, key, line):
        filename = os.environ["map_input_file"]
        gender = filename.split(".")[1]
        try:
            docnum = int(filename[0])
        except:
            docnum = 8
        if filename.startswith("51"):
            # remove leading and trailing whitespace
            line = line.strip()
            if line == "<post>":
                self.post_start = True
            elif line == "</post>":
                self.post_start = False
                yield gender, repr("\n".join(self.post))
                self.post = []
            elif self.post_start:
                self.post.append(line)



if __name__ == '__main__':
    ExtractPosts.run()
