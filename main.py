import json

inputdata = open('code-20210423-mdsurkhab\jsonfile.json', 'r')

jsondata = inputdata.read()

obj = json.load(jsondata)

def bmi(wght, hght):
  hght/=100
  res = wght/(hght*hght)
  return res

def ctgnrisk(bmivalue):
  if bmivalue<=18.4:
    return list("Underweight", "Malnutrition risk")
  elif bmivalue>=18.5 and bmivalue<=24.9:
    return list("Normal weight","Low risk")
  elif bmivalue>=25 and bmivalue<=29.9:
    return list("Overweight","Enhanced risk")
  elif bmivalue>=30 and bmivalue<=34.9:
    return list("Moderately obese", "Medium risk")
  elif bmivalue>=35 and bmivalue<=39.9:
    return list("Severely obese","High risk")
  else:
    return list("Very severely obese", "Very high risk")
  
# calculating bmi of json data
newdata = []
for i in obj:
  out = bmi(int(i["WeightKg"]),int(i["HeightCm"]))
  d = {}
  d["BMI"] = out
  a = ctgnrisk(out)
  d["BMI Category"] = a[0]
  d["Health risk"] = a[1]
  newdata.append(d)
  
for i in newdata:
  j = json.dumps(i)
  f = open("code-20210423-mdsurkhab\jsonfile.json","w")
  f.write(j)
  f.close()
  
  
  
  
