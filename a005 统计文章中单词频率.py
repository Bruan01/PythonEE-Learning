#coding=utf-8
word_string = """ 
    Long ago in a small, faraway village, there was a place known as the House of 1000 Mirrors. 
    A small, happy little dog learned of this place and decided to visit. 
    When he arrived, he hounced happily up the stairs to the doorway of the house. 
    He looked through the doorway with his ears lifted high and his tail wagging as fast as it could. 
    To his great surprise, he found himself staring at 1000 other happy little dogs with their tails wagging just as fast as his. 
    He smiled a great smile, and was answered with 1000 great smiles just as warm and firendly. """
word_string=word_string.replace('.','')  
word_string=word_string.replace(',','')  
wordlsit=word_string.split()

wordfreq=[]
for w in wordlsit:
    wordfreq.append(wordlsit.count(w))

d= dict(zip(wordlsit,wordfreq))
print(d)    