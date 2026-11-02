# REFLECTION

# 1. I came into this class not really knowing how to code, so I thought lists would be way more 
# complicated than they are. What surprised me most is that counting starts at 0 instead of 1, 
# so the first item is inventory[0]. I also didn’t know you could use [-1] to grab the last 
# item without even knowing how long the list is.

# 2.  When I worked as a server, I wanted to know how much I made in tips each
#    week and which night was my best. In Excel I would have to type in every
#    shift and set up formulas, but with a Python list I could take each
#    night's tips and use sum(), max(), and min() to get the answers in a few
#    lines. I could also pull out just the big nights with a loop. 
 
 

# Exercise 1: 

print("--- Exercise 1: Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
 
 

# Exercise 2:

print("\n--- Exercise 2: Index practice ---")
print(inventory[0])            # first item (positive index)
print(inventory[-1])           # last item (negative index)
middle = len(inventory) // 2   # middle position computed from the length
print(inventory[middle])
 
 

# Exercise 3: 
 
print("\n--- Exercise 3: Slicing ---")
print(inventory[:3])    # first three items
print(inventory[-2:])   # last two items (negative slice)
print(inventory[::2])   # every other item (step slice)
 
 

# Exercise 4:

print("\n--- Exercise 4: Modify ---")
inventory.append("envelope")
print("After append:", inventory)
inventory.remove("tape")
print("After remove:", inventory)
inventory.sort()
print("After sort:", inventory)
 
 

# Exercise 5: 

print("\n--- Exercise 5: Tuple comparison ---")
coords = (40.7128, -74.0060)   # NYC latitude and longitude
try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples can't be changed after they are created. That makes them good")
    print("for coordinates, because a location's latitude and longitude should")
    print("never get overwritten by accident.")
print(coords)
 
 

# Exercise 6: 

print("\n--- Exercise 6: Average of a list of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))
 
 

# Exercise 7:

print("\n--- Exercise 7: Accumulator pattern ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    new_price = round(price * 0.90, 2)   # take 10% off, round to 2 decimals
    discounted.append(new_price)
print("Original:", prices)
print("Discounted:", discounted)
 
 
# Exercise 8:

print("\n--- Exercise 8: Filter above threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for day in sales:
    if day > 300:
        high_sales.append(day)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
