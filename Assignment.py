# Section : All
# Student_1 : Ahmed Osama Fawzy - 20210008
# Student_2 : Omar Ammer - 20210257

def ReturnString(Earray):
    ex = "" 
    for i in range(len(Earray)):
        ex += Earray[i] + " "
    return ex[:-1]

print("Main Expresion = ∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]")

def Eliminate_Implication(e):
    Earray = e.split(" ")
    for i in range(len(Earray)):
        if(Earray[i] == "=⇒"):
            Earray[i] = "V"
            if(Earray[i-1] == "]"):
                Earray.insert(Earray.index("["), "~")
            else:
                Earray.insert(i-1,"~")
    return ReturnString(Earray)
print("Eliminate_Implication =  " + Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]"))

def Demorgan_Law(e):
    Earray = e.split(" ")
    for i in range(len(Earray)):
        if(Earray[i] == "~"):
            if(Earray[i+1] == "["):
                Earray.insert(Earray.index("]") + 2, "~")
                Earray.remove('~')
                Earray.insert(i + 1, "~")
                if(Earray[Earray.index("]")+1] == "V"):
                    Earray[Earray.index("]") + 1] = '∧'
                elif(Earray[Earray.index("]")+1] == "∧"):
                    Earray[Earray.index("]") + 1] = 'V'
                break
    return ReturnString(Earray)
print("Demorgan_Law =  " + Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]")))

def Remove_Double_Not(e):
    Earray = e.split(" ")
    for i in range(len(Earray)):
        if(Earray[i] == "~"):
            Earray.remove("~")
            if (Earray[i+1] == "~"):
                Earray.remove("~")
            elif(Earray[i+2] == "~"):
                Earray.remove("~")
            elif(Earray[i+3] == "~"):
                Earray.remove("~")
            break
    return ReturnString(Earray)
print("Remove_Double_Not =  " + Remove_Double_Not(Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]"))))

def Standardize_Variable(e):
    Earray = e.split(" ")
    indexs = []
    for i in range(len(Earray)):
       if(Earray[i].__contains__("∀") or Earray[i].__contains__("∃")):
           indexs.append(i)
    indexs.append(len(Earray))
    return ReturnString(Earray)
print("Standardize_Variable =  " + Standardize_Variable(Remove_Double_Not(Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]")))))

def Skolemization(e):
    Earray = e.split(" ")
    for i in range(len(Earray)):
        if(Earray[i].__contains__("∃")):
            Earray.remove(Earray[i])
            for j in range(i , len(Earray)):
                newtext1 = Earray[j].replace("x", "No", 1).replace("y", "No", 1)
                Earray[j] = newtext1
            break
    return ReturnString(Earray)
print("Skolemization =  " + Skolemization(Standardize_Variable(Remove_Double_Not(Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]"))))))

def Prenex_Form(e):
    Earray = e.split(" ")
    exx = ""
    for i in range(len(Earray)):
        if (Earray[i].__contains__("∀") or Earray[i].__contains__("∃")):
            exx += Earray[i] + " "
    arrayA = [item for item in Earray if '∀' not in item]
    arrayE = [item for item in arrayA if '∃' not in item]
    return ReturnString(arrayE)
print("Prenex_Form =  " + Prenex_Form(Skolemization(Standardize_Variable(Remove_Double_Not(Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]")))))))

def Eliminate_Universal_quantifiers(e):
    Earray = e.split(" ")
    Earray = [element for element in Earray if "∀" not in element]
    return ReturnString(Earray)
print("Eliminate_Universal_quantifiers =  " + Eliminate_Universal_quantifiers(Prenex_Form(Skolemization(Standardize_Variable(Remove_Double_Not(Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]"))))))))

def Convert_to_Conjunctive(e):
    Earray = e.split(" ")
    i = 0
    while i < len(Earray):
        if(Earray[i] == "∧"):
            if(Earray[i+1] == "[" or Earray[i+2] == "["):
                Earray[i] = "V"
        i += 1
    return ReturnString(Earray)
print("Convert_to_Conjunctive =  " + Convert_to_Conjunctive(Eliminate_Universal_quantifiers(Prenex_Form(Skolemization(Standardize_Variable(Remove_Double_Not(Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]")))))))))

def Turn_Conjunctions(e):
    Earray = e.split(" ")
    Earray = [element for element in Earray if "[" not in element]
    Earray = [element for element in Earray if "]" not in element]
    Earray = [element for element in Earray if "∧" not in element]
    Earray = [element for element in Earray if "V" not in element]
    ex = "{ "
    for i in range(len(Earray)):
        ex += Earray[i] + " ,"
    ex[:-2]
    ex += " }"
    return ex
print("Turn_Conjunctions =  " + Turn_Conjunctions(Convert_to_Conjunctive(Eliminate_Universal_quantifiers(Prenex_Form(Skolemization(Standardize_Variable(Remove_Double_Not(Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]"))))))))))

def Rename_Variables(e):
    Earray = e.split(" ")
    i = 0 
    while i < len(Earray):
        if(Earray[i].__contains__("x")):
            new = Earray[i].replace("x","par1",1)
            Earray[i] = new

        if(Earray[i].__contains__("y")):
            new = Earray[i].replace("y","par2",1)
            Earray[i] = new
        
        if(Earray[i].__contains__("z")):
            new = Earray[i].replace("z","par3",1)
            Earray[i] = new
        
        if(Earray[i].__contains__("w")):
            new = Earray[i].replace("w","par4",1)
            Earray[i] = new
        i += 1
    return ReturnString(Earray)
print("Rename_Variables =  " + Rename_Variables(Turn_Conjunctions(Convert_to_Conjunctive(Eliminate_Universal_quantifiers(Prenex_Form(Skolemization(Standardize_Variable(Remove_Double_Not(Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]")))))))))))

print("Last Exprestion =  " + Rename_Variables(Turn_Conjunctions((Convert_to_Conjunctive(Eliminate_Universal_quantifiers(Prenex_Form(Skolemization(Standardize_Variable(Remove_Double_Not(Demorgan_Law(Eliminate_Implication("∀x [ ∀y Animal(y) =⇒ Loves(x,y) ] =⇒ [ ∃y Loves(y,x) ]"))))))))))))