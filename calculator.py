def calculate_total(items, discount_percent):
    """
    Calculates the total price after a discount.
    BUG: The discount is currently being ADDED instead of SUBTRACTED.
    """
    subtotal = sum(items)

    # Logic error here: + instead of -
    total = subtotal - (subtotal * (discount_percent / 100))

    return total

def test_calculator():
    # 100 - 10% should be 90, but this code will give 110
    result = calculate_total([50, 50], 10)
    print(f"Result: {result}")
    assert result == 90

if __name__ == "__main__":
    test_calculator()

