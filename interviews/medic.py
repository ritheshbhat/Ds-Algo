def fraction_to_decimal(numerator, denominator):
    try:
        # Convert numerator and denominator to integers
        numerator = int(numerator)
        denominator = int(denominator)

        # Handle zero denominator case
        if denominator == 0:
            return "Invalid input"

        # Determine the integer part of the division
        integer_part = numerator // denominator
        remainder = numerator % denominator

        # If there is no remainder, return the integer part
        if remainder == 0:
            return str(integer_part)

        # Use a dictionary to store remainders and their positions
        remainder_dict = {}
        decimal_part = ""
        position = 0

        while remainder != 0:
            # If the remainder is already in the dictionary, we found a cycle
            if remainder in remainder_dict:
                start = remainder_dict[remainder]
                non_repeating = decimal_part[:start]
                repeating = decimal_part[start:]
                return f"{integer_part}.{non_repeating}({repeating})"

            # Store the remainder and its position
            remainder_dict[remainder] = position
            position += 1

            # Perform long division manually
            remainder *= 10
            decimal_part += str(remainder // denominator)
            remainder %= denominator

        return f"{integer_part}.{decimal_part}"

    except (ValueError, ZeroDivisionError):
        return "Invalid input"


# Example usage
print(fraction_to_decimal(1, 2))  # Output: 0.5
print(fraction_to_decimal(1, 3))  # Output: 0.(3)
print(fraction_to_decimal(22, 7))  # Output: 3.(142857)
print(fraction_to_decimal(1, 6))  # Output: 0.1(6)
print(fraction_to_decimal(1, 333))  # Output: 0.(003)
print(fraction_to_decimal(10, 0))  # Output: Invalid input
print(fraction_to_decimal("a", 2))  # Output: Invalid input
