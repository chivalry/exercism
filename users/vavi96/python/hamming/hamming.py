def distance(strand_a, strand_b):
  count=0
  if len(strand_a) == len(strand_b): 
   for value in strand_a:
    for element in strand_b:
     if value!=element and t==i:   #t,i indexes of strand_a, strand_b
      count=count + 1
   print count
