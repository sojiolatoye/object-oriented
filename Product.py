
class Product:
    
    def getProductCode(pc):
        correctvalue = False
        while not correctvalue:
            answer = int(input(pc))
            if answer >= 100 and answer <= 1000:
                correctvalue = True
        return answer
        

 
