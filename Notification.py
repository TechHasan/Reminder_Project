#import time
import time
#import notification from plyer module
from plyer import notification


if __name__ == "__main__":

    print("How much longer to see that remider...?")
    timeo= int(input() )
    print("after differece time remider...?")
    times=  int( input() )
    
    #use while loop to create notification indefinetly
    print("What shall I remind you about?")
    print("water Or Exercise Or Food \n")
    text = str(input())
    
    while True:
        if( (text=="water") or (text=="exercise") or (text=="food") ):
            
            
            #For Water
            if(text=="water"):
                #notification
                notification.notify(
                    #title= "***Please Drink Water Now!!!",
                    title= text,
                    message= "Water Can Help Control Calories."
                             "Water Helps Energize Muscles."            
                             "Water Helps Keep Skin Looking Good."
                             "Water Helps Your Kidneys. " ,

                    app_icon = "waterg.ico",
                    timeout= timeo
                )
                #after time.sleep second execute again for timeout(second)
                time.sleep(times)
               

            #For Exercise
            elif(text=="exercise"):
                #notification
                notification.notify(
                    #title= "***Please Do Exercise Now!!!",
                    title= text,
                    message= "Weight Management."
                             "Strengthen Your Bones and Muscles."
                             "Increase Your Chances of Living Longer."
                             "Manage Chronic Health Conditions & Disabilities." ,
                    
                    app_icon = "exercise.ico",
                    timeout= timeo
                    )
                #after time.sleep second execute again for timeout(second)
                time.sleep(times)

            #For Food
            elif(text=="food"):
                #notification
                notification.notify(
                    #title= "***Please Eat Food Now!!!",
                    title= text,
                    message= "Strengthens bones."
                             "Supports muscles."
                             "Keeps skin, teeth, and eyes healthy."
                             "Lowers risk of heart disease, type 2 diabetes, and some cancers." ,
                    
                    app_icon = "meal.ico",
                    timeout= timeo
                    )
                #after time.sleep second execute again for timeout(second)
                time.sleep(times)

            
        #Else enter correct choice    
        else:
            print("Pls Enter Correct Choice Give Above ")
            exit()
            

            
