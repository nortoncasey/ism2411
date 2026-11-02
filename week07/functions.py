# --- Self-Assessment ---
# Q1: The first bug I found was the missing colon after
# "for sale in sales". I found it from the traceback because the
# code wouldn't even run. I think that means I rely on error
# messages a lot. I need to also check if the output is right,
# since the total bug didn't show any error.
#
# Q2: apply_discount takes a price and a tier gold, silver,
# bronze, and gives back the new price after
# the discount. Gold is 15% off, silver is 10%, bronze is 5%,
# and anything else gets no discount. A colleague could use it
# without reading the code as long as they know the tier names.
#
# Q3:  
#It was a little of both. It helped me understand scope, 
# like how the x inside the function is different from the x outside. 
# But it was also kind of a shortcut, so next time I want to try 
# fixing my mistakes  myself first.
 
# --- Exercise 1 ---
def calculate_tax(price, rate):
    """Return the tax amount for a given price and rate."""
    return price * rate
 
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")
 
 
# --- Exercise 2 ---
def apply_discount(price, tier):
    """Return the discounted price based on the customer tier."""
    if tier == "gold":
        return price * 0.85     
    elif tier == "silver":
        return price * 0.90      
        return price * 0.95      
    else:
        return price             
 
print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")
 
 
# --- Exercise 3 ---

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + tax:.2f}")
 
def final_price(price, tier, tax_rate):
    """Return the final price: discounted price + tax."""
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
 
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')
 
 
# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
 
 
# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90]
 
total = 0
for sale in sales:
    # Fix 1: "total = sale" replaced the total with each sale, so it only
    # kept the last sale ($90). Using += adds every sale to the total ($715).
    total += sale
print(f"Total: ${total}")
 
count = 0
# Fix 2: SyntaxError: expected ':' - this for loop was missing the colon
# at the end of the line. Added the colon.
for sale in sales:
    count += 1
print(f"Count: {count}")
 
i = 0
# Fix 3: IndexError: list index out of range - "i <= len(sales)" let i
# reach 5, but the list only has indexes 0-4. Changed <= to < so the
# loop stops after the last item.
while i < len(sales):
    print(sales[i])
    i += 1
 
 
# --- Exercise 6 ---
# Prediction: 100, then 1998, then 100
x = 100   # global variable
 
def double_it():
    x = 999   # local variable — different from global x!
    return x * 2
 
print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?
 
# Output: 100, 1998, 100 - x did not change.
# Scope is where a variable can be used. A variable made inside a function
# is local, so it only works inside that function. The x = 999 in double_it()
# is a different x from the global x = 100, even though they share a name.
# The function doubled its own x (999 * 2 = 1998), so the global x stayed 100
 