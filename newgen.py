import time

def elfibo():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0 :
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2 , aux
            
            
            yield aux 

if __name__ == "__main__":
    secuence= elfibo()
    LimitNumb= int(input("Choose limit numb: "))
    if LimitNumb == 0:
        print("choose another number beside zero")
    element = 0
    for element in secuence:
        if element <= LimitNumb:
            print(element)
            time.sleep(0.7)
        else:
            print("reached limit.")
            break
    
    print ("End program.")



