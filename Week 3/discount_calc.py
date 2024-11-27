def calculate_discount(price, discount_percentage):
    """
    Calculate the total price after applying a discount.

    Parameters:
    price (float): The original price before discount.
    discount_percentage (float): The percentage of discount to apply.

    Returns:
    float: The total price after discount.
    """
    # Calculate the amount of discount
    discount = price * discount_percentage / 100
    
    # Subtract the discount from the original price to get the total price
    total_price = price - discount
    return total_price

# Prompt the user to enter the original price
price = int(input("Enter the price: \n"))

# Prompt the user to enter the discount percentage
discount_percentage = int(input("Enter the discount percentage: \n"))

# Check if the discount percentage is 20% or more
if discount_percentage >= 20:
    print(f"You are eligible for a discount of {discount_percentage}%")
    # Calculate and display the total price after applying the discount
    print(f"The total price after discount is: {calculate_discount(price, discount_percentage)}")
else:
    print("You are not eligible for a discount of 20% or more")
    # Display the original price since no discount is applied
    print(f"The total price after discount is: {price}")