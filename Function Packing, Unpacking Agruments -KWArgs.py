

#-----------------------------------------------------------
#------ Function Packing, Unpacking Agruments **KWArgs------
#-----------------------------------------------------------



def show_skills(*skills) :
    print(type(skills)) # <class "tuple" >
    
    for skill in skills : 
        print(f"{skill}")

show_skills("Html" , "Css" , "Js") # Html , Css , Js


print("$" * 50) # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


mySkills = {
     "Html " : "90% ",
     "Css" : "80%" ,
     "Js" :"40%"
}

def show_skills(**skills) :
    print(type(skills)) # <class "tuple" >
    
    for skill,value  in skills.items() : 
      print(f"{skill} => {value}")

show_skills(Html = "90% ", Css = "80%" , Js= "40%" ) 
# <class "dictionary" >
# Html => 90%
# Css => 80%
# Js => 40%
print(mySkills) # { Html = "90% ", Css = "80%" , Js= "40%" }
print(**mySkills) 
# # <class "dictionary" >
# Html => 90%
# Css => 80%
# Js => 40%

















