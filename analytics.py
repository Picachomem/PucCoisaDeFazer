import random
def mergulha_registrinho(foodAmount):
    wasteNot=[]
    foodSum=0
    foodAvg=0
    for i in range(len(foodAmount)):
        wasteNot.append(random.randint(0,1))
    print (wasteNot)
    for i in range(len(wasteNot)):
        if wasteNot[i]==0:
            foodSum+=foodAmount[i]
            foodAvg=foodSum/(i+1)
            if (foodAmount[i]-foodAvg)<0:
                print(0.0)
            else:
                print(foodAmount[i]-foodAvg)
                
        else:
            if (foodAmount[i]-foodAvg)<0:
                print(0.0)
            else:
                print(foodAmount[i]-foodAvg)
    
        
    
        
    
        
        
    
    
    
    
