import pandas as pd

#entree menu list initialized
Entree = [["Vegan Fried Mushroom Burger",8],["Califlour Buffalo Taco's",8],["Vegan Cajun Shrimp Burger",12], ["Vegan Impossible Gouda Bacon Burger",11]]
#creating dataframe for entree menu...
ent = pd.DataFrame(Entree, columns = ['Entree','Price'])
ent.index += 1

Sides = [["Sweet Potato Fries",3],["Sweet Southern Onion Rings",4],["Vegan Chili Cheese Tater Tots",4], ["Vegan Garlic Parmesian Fries",3]]
sid = pd.DataFrame(Sides, columns = ['Side','Price'])
sid.index += 1

Drinks = [['Water'0],["Canjun Lemonade",3],["Raspberry Kombucha",4],["Winter Green Tea",3]
dri = pd.DataFrame(Drinks, columns = ['Drink', 'Price'])
dri.index += 1