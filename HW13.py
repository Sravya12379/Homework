a="ssr@ray1v1"
b="sr@vy1_a"
dict={}
def generate_phrase(char,ph):

  for i in char:
    count=char.count(str(i))
    dict[i]=str(count)
  print(dict)

  dict1={}
  for j in ph:
    count1=ph.count(str(j))
    dict1[j]=str(count1)
  print(dict1)

  if len(char)< len(ph):
      print("Phrase can't be generated")
      return False
  else:
    for i in dict:
        for j in dict1:
            if i==j :
                if dict[i]>=dict1[j]:
                 return True

x=generate_phrase("cbacba","aabbcc")
print(x)











