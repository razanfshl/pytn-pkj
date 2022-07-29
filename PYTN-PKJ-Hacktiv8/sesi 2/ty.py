name = "taeyeon"
age_now = 33
hobby = ["eat", "sleep", "rest"]

def greet(time, age, name="Sir/Mam"):
    print ("Hi " + str(name.title()) + ", Good " + str(time))
    print ("It's me your", "older sister" 
        if (age < age_now) 
        else "younger sister")    
    
    
def activity(go):
    if (go in hobby):
        print ("Sure let's " + str(go))
    else:
        print ("No thanks")
