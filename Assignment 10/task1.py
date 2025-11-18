def discount(price, category):
    """
    Calculate discounted price based on the shopper category.

    Parameters
    ----------
    price : float
        Original price of the purchase.
    category : str
        Shopper category (e.g., "student", "monday").
    """

    def apply_threshold(price, threshold, high_discount, low_discount=1.0):
        """Apply a high or low discount depending on a price threshold."""
        return price * (high_discount if price > threshold else low_discount)

    # Map each category to a function that computes its discounted price
    rules = {
        "student": lambda p: apply_threshold(p, 1000, 0.9, 0.95),
        "monday": lambda p: apply_threshold(p, 2000, 0.85, 1.0),
    }

    handler = rules.get(category.lower())
    if handler is None:
        raise ValueError(f"Unsupported category: {category}")

    return handler(price)


if __name__ == "__main__":
    # Simple interactive usage example
    try:
        price_input = float(input("Enter the original price: "))
        category_input = input('Enter shopper category (e.g., "student" or "monday"): ')

        final_price = discount(price_input, category_input)
        print(f"Final price after discount: {final_price:.2f}")
    except ValueError as exc:
        print(f"Error: {exc}")
