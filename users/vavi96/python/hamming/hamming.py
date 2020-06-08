def distance(strand_a, strand_b):
  count=0
  if len(strand_a)!=len(strand_b): 
    raise ValueError('Not match')
  elif len(strand_a) == len(strand_b): 
    for value in strand_a:
     pos1 = strand_a.index(value)
     for element in strand_b:
      pos2 = strand_b.index(element)
      if value!=element and pos1==pos2:   # pos1,pos2 indexes in   strand_a,strand_b
       count=count + 1
    return count
