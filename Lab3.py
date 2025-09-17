# Program Name: Lab3.py
# Course: IT1114/Section 3
# Student Name: Elhadj Diallo
# Assignment Number: Lab3
# Due Date: 9/21/ 2025
# Purpose:The purpose of the program is to calculate the cost of pizza and salads based on inputs and discounts

#Salads

salads=int(input("How many salads:> "))
costOfSalads=7.99
salads_total=costOfSalads*salads
discount=.15
if salads>10:
  print(f"Salad Cost: {salads_total}")
print(f"Discount: {salads_total*.15}")

#pizza 
pizza_cost=7.99
pizza_slices=int(input("How many Pizza Slices:> "))
if pizza_slices<12:
  print("You can only order whole pizzas, which are atleast 12 slices")
elif pizza_slices>=12:
  whole_pizzas=int((pizza_slices+11)/12)
  print(whole_pizzas)
