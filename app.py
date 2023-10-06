from Product import Product



userinput = int(Product.getProductCode("Please enter the Product Code:"))

if userinput >= 100 and userinput <= 1000: 
     print("Product Code:", userinput)
else:
     print("Please enter correct value")





# userinput2 = str(input("Please enter the Product Name:"))
# userinput3 = float(input("Please enter the Product Sale Price:"))
#userinput4 = float(input("Please enter the Product Manufacture Cost:"))
#userinput5 = int(input("Please enter the Current Stock:"))
#userinput6 = int(input("Please enter estimated monthly production:"))


#print("Product Name:", userinput2)
#print("Sale Price:", userinput3)
#print("Manufacture cost:", userinput4)
#print("Monthly Production:", userinput6, "Approx.")