def weight_on_planets():
   # write your code here

   weight = float(input("What do you weigh on earth? "))

   wMars = weight * 0.38
   wJupiter = weight * 2.34

   print("\nOn Mars you would weigh " + str(wMars) + " pounds.\nOn Jupiter you would weigh " + str(wJupiter) + " pounds.");
   
if __name__ == '__main__':
   weight_on_planets()