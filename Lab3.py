# Program Name: Lab3.py
# Course: IT1114/Section 3
# Student Name: Elhadj Diallo
# Assignment Number: Lab3
# Due Date: 9/21/ 2025
# Purpose:The purpose of the program is to calculate the cost of pizza and salads based on inputs and discounts
delivery=20
pizza_discount=0
salads_discount=0
total_discount=0

pizza_slices=int(input("How many Pizza Slices:> "))
salads=int(input("How many salads:> "))
#salads
costOfSalads=7.99
salads_total=costOfSalads*salads
discount=.15


#pizza 
pizza_cost=15.99

whole_pizzas=int((pizza_slices+11)/12)
pizza_total=pizza_cost*whole_pizzas
if whole_pizzas>=10: # If theres more than 10 WHOLE pizzas add a discount on pizzas
  pizza_discount=pizza_total*discount
if salads>10: # If theres more than 10 salads, add a discount salads
  salads_discount= salads_total*discount
total=pizza_total+salads_total
#Delivery logic:
# The delivery must be at least 20 dollars
if total*.07>delivery:
  delivery=total*.07
total_discount=salads_discount+pizza_discount
print(f"Whole Pizzas: {whole_pizzas}")
print("Pizza cost: ",pizza_total)
print(f"Salad Cost: {salads_total}")

print(f"Discount: {total_discount}")
print(f"Delivery: ",delivery)
print(f"Total: {total+delivery-total_discount}")