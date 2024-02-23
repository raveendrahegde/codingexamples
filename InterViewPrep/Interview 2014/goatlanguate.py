def string_to_goat_latin(sentence):
  consonents=['b','c','d,'f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
  vowels=['a','e','i','o','u']
  words=sentence.split()
  count = 0
  isConsonent=False
  newsentence=[]
  for word in words:
    count += 1
    if word[0] in consonents:
      newword = word[1:] + word[0] + 'ma'
      isConsonent=True
    else:
      newword2 = word + 'ma'
      isConsonent=False
      
    if isConsonent:
      newsentence.append(newword + count * 'a')
    else:
      newsentence.append(newword2 + count * 'a')

  print " ".join(newsentence)
