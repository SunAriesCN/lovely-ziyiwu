
# coding: utf-8

# In[1]:


WORDS= "mongolian lamb wool mohair sheep tibetan penny lane Sloppy rock punk wild west gypsy hipster ghetto artisanal artist Y2K gritty folk bohemian grunge boho hippie alternative upcycled remade artsy club kids mod moschino Marques Almeida raw"
SIZE_OF_CHARACTERS_IN_A_ROW = 20

size_of_chars = SIZE_OF_CHARACTERS_IN_A_ROW
words= WORDS.split()

def helper(_start, _words, _sums):
    i = _start
    # print(f"{i} {len(_sums)}")
    sums_ = _sums.copy()
    if i < len(_words):

        for key in _sums.keys():
            
            # sentence = f"{key} {_words[i]}"
            sentence = "{} {}".format(key, _words[i])
            if sentence in _sums.keys() or len(sentence) > 20:
                continue
                                               
            sums_[sentence]=len(sentence)

        sums_[words[i]] = len(_words[i])
        i = i + 1
        sums_ = helper(i, _words, sums_)

    return sums_

while len(words) > 0:
    sums = {}
    sums = helper(0, words, sums)
    best_item = sorted(sums.items(), key=lambda item:item[1], reverse=True)[0]
    print(best_item)
    
    removed_words = best_item[0].split()
    for word in removed_words:
        words.remove(word)

