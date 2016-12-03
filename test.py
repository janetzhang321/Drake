import sys
sys.path.insert(0, 'utils/RAKE')
from rake import *

text = "I'm tryna put you in the worst mood, ah P1 cleaner than your church shoes, ah Milli point two just to hurt you, ah All red Lamb' just to tease you, ah None of these toys on lease too, ah Made your whole year in a week too, yah Main bitch out your league too, ah Side bitch out of your league too, ah"

# Split text into sentences
sentenceList = split_sentences(text)
#stoppath = "FoxStoplist.txt" #Fox stoplist contains "numbers", so it will not find "natural numbers" like in Table 1.1
stoppath = "utils/RAKE/SmartStoplist.txt"  #SMART stoplist misses some of the lower-scoring keywords in Figure 1.5, which means that the top 1/3 cuts off one of the 4.0 score words in Table 1.1
stopwordpattern = build_stop_word_regex(stoppath)

# generate candidate keywords
phraseList = generate_candidate_keywords(sentenceList, stopwordpattern)

# calculate individual word scores
wordscores = calculate_word_scores(phraseList)

# generate candidate keyword scores
keywordcandidates = generate_candidate_keyword_scores(phraseList, wordscores)
if debug: print keywordcandidates

sortedKeywords = sorted(keywordcandidates.iteritems(), key=operator.itemgetter(1), reverse=True)
if debug: print sortedKeywords

totalKeywords = len(sortedKeywords)
if debug: print totalKeywords
# print sortedKeywords[0:(totalKeywords / 3)]

rake = Rake("utils/RAKE/SmartStoplist.txt")
keywords = rake.run(text)
# print keywords

ret = []
i = 0
while i < 5:
    li = keywords[i][0]
    ret.append(li)
    i += 1
print ret
