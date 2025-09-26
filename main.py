import random
import string

text = input("Enter message: ")
st = text.split(" ")
coding = input("0 for Encoding 1 for Decoding: ")
coding = True if (coding == "0") else False

if coding:
  nwords = []
  for word in st:  
    if (len(word) >= 3 and len(word) <= 5):
      stnew = word[2:] + word[0:2]
      nwords.append(stnew)
    elif (len(word) > 5 ):
      stnew = word[-2:] + word[-3:1:-1] + word[:2]
      
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])

  newtext = ' '.join(''.join(random.choices(string.ascii_lowercase, k=2)) + word + ''.join(random.choices(string.ascii_lowercase, k=3)) for word in nwords)

  print(newtext)


else:
  nwords = []
  for word in st:  
    if (len(word) >= 8 and len(word) <= 10):
      stnew = word[-5:-3] + word[2:-5]
      nwords.append(stnew)

    elif (len(word) > 10 ):
      stnew = word[-5:-3] + word[-6:3:-1] + word[2:4]
      nwords.append(stnew)
    else:
      nwords.append(word[-4:1:-1])

  print(' '.join(nwords))
  