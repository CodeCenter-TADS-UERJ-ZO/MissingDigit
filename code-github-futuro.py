def MissingDigit(strParam):
  temp = strParam.split(" ");

  for item in temp:
    if item.find("x") > -1:
      strParam = strParam.replace(item, "x");
      x = item;
      break;

  valor = find_x(strParam);

  #tamanho = len(int(valor));

  for i, j in zip(str(int(valor)), x):
    if i != j:
      return i;

  return valor

def find_x(strParam):
  # SOMA
  if strParam.find("+") > 0:
    strParam = strParam.split("+");
    strParam[1] = strParam[1].split("=");
    strParam = [strParam[0], strParam[1][0], strParam[1][1]];

    strParam[0] = strParam[0].replace(" ","");
    strParam[1] = strParam[1].replace(" ","");
    strParam[2] = strParam[2].replace(" ","");
    
    if strParam[2] == 'x':
      strParam = int(strParam[0]) + int(strParam[1]);
      return strParam
    
    if strParam[2].find("x") > -1:
      temp = int(strParam[2].replace("x",""))
      strParam = (int(strParam[0]) + int(strParam[1]))/temp;
      return strParam

    if strParam[1] == 'x':
      strParam = int(strParam[2]) - int(strParam[0]);
      return strParam
    
    if strParam[1].find("x") > -1:
      temp = int(strParam[1].replace("x",""))
      strParam = (int(strParam[2]) - int(strParam[0]))/temp;
      return strParam

    if strParam[0] == 'x':
      strParam = int(strParam[2]) - int(strParam[1]);
      return strParam
    
    if strParam[0].find("x") > -1:
      temp = int(strParam[0].replace("x",""))
      strParam = (int(strParam[2]) - int(strParam[1]))/temp;
      return strParam

  # SUBTRACAO
  if strParam.find("-") > 0:
    strParam = strParam.split("-");
    strParam[1] = strParam[1].split("=");
    strParam = [strParam[0], strParam[1][0], strParam[1][1]];

    strParam[0] = strParam[0].replace(" ","");
    strParam[1] = strParam[1].replace(" ","");
    strParam[2] = strParam[2].replace(" ","");
    
    if strParam[2] == 'x':
      strParam = int(strParam[0]) - int(strParam[1]);
      return strParam
    
    if strParam[2].find("x") > -1:
      temp = int(strParam[2].replace("x",""))
      strParam = (int(strParam[0]) - int(strParam[1]))/temp;
      return strParam

    if strParam[1] == 'x':
      strParam = -(int(strParam[2]) - int(strParam[0]));
      return strParam
    
    if strParam[1].find("x") > -1:
      temp = int(strParam[1].replace("x",""))
      strParam = -(int(strParam[2]) - int(strParam[0]))/temp;
      return strParam

    if strParam[0] == 'x':
      strParam = int(strParam[2]) + int(strParam[1]);
      return strParam
    
    if strParam[0].find("x") > -1:
      temp = int(strParam[0].replace("x",""))
      strParam = (int(strParam[2]) + int(strParam[1]))/temp;
      return strParam

  # MULTIPLICACAO
  if strParam.find("*") > 0:
    strParam = strParam.split("*");
    strParam[1] = strParam[1].split("=");
    strParam = [strParam[0], strParam[1][0], strParam[1][1]];

    strParam[0] = strParam[0].replace(" ","");
    strParam[1] = strParam[1].replace(" ","");
    strParam[2] = strParam[2].replace(" ","");
    
    if strParam[2] == 'x':
      strParam = int(strParam[0]) * int(strParam[1]);
      return strParam
    
    if strParam[2].find("x") > -1:
      temp = int(strParam[2].replace("x",""))
      strParam = (int(strParam[0]) * int(strParam[1]))/temp;
      return strParam

    if strParam[1] == 'x':
      strParam = (int(strParam[2]) / int(strParam[0]));
      return strParam
    
    if strParam[1].find("x") > -1:
      temp = int(strParam[1].replace("x",""))
      strParam = (int(strParam[2]) / int(strParam[0]))/temp;
      return strParam

    if strParam[0] == 'x':
      strParam = int(strParam[2]) / int(strParam[1]);
      return strParam
    
    if strParam[0].find("x") > -1:
      temp = int(strParam[0].replace("x",""))
      strParam = (int(strParam[2]) / int(strParam[1]))/temp;
      return strParam

  # DIVISAO
  if strParam.find("/") > 0:
    strParam = strParam.split("/");
    strParam[1] = strParam[1].split("=");
    strParam = [strParam[0], strParam[1][0], strParam[1][1]];

    strParam[0] = strParam[0].replace(" ","");
    strParam[1] = strParam[1].replace(" ","");
    strParam[2] = strParam[2].replace(" ","");
    
    if strParam[2] == 'x':
      strParam = int(strParam[0]) / int(strParam[1]);
      return strParam
    
    if strParam[2].find("x") > -1:
      temp = int(strParam[2].replace("x",""))
      strParam = (int(strParam[0]) / int(strParam[1]))/temp;
      return strParam

    if strParam[1] == 'x':
      strParam = (int(strParam[2]) * int(strParam[0]));
      return strParam
    
    if strParam[1].find("x") > -1:
      temp = int(strParam[1].replace("x",""))
      strParam = (int(strParam[2]) * int(strParam[0]))/temp;
      return strParam

    if strParam[0] == 'x':
      strParam = int(strParam[2]) * int(strParam[1]);
      return strParam
    
    if strParam[0].find("x") > -1:
      temp = int(strParam[0].replace("x",""))
      strParam = (int(strParam[2]) * int(strParam[1]))/temp;
      return strParam

# keep this function call here 
print(MissingDigit(input()))
