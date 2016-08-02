def fRange(valMin, valMax, valN):
  
  if valMin > valMax: raise Exception, "valMin > valMax"
  if valN < 2:        raise Exception, "valN < 2"
  
  vals = []

  for i in range(valN):
    val = valMin + float(i)/(valN - 1)*(valMax - valMin)
#    print i, val
    vals.append(( val ))
  
  return vals

def fRangeDecending(valMax, valMin, valN):
  
  if valMin > valMax: raise Exception, "valMin > valMax"
  if valN < 2:        raise Exception, "valN < 2"
  
  vals = []

  for i in range(valN):
    val = valMax - float(i)/(valN - 1)*(valMax - valMin)
#    print i, val
    vals.append(( val ))
  
  return vals
