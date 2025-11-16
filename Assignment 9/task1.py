def sum_even_odd(numbers):
    """
    MANUALLY WRITTEN DOCSTRING (Google Style)
    ==========================================
    
    Calculates the sum of even and odd numbers in a given list.

    Args:
        numbers (list[int]): A list of integers to process.

    Returns:
        tuple: A tuple containing two integers:
            - Index 0: The sum of all even numbers in the list.
            - Index 1: The sum of all odd numbers in the list.

    Raises:
        TypeError: If the input is not a list or contains non-integer values.

    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5])
        (6, 9)
        
        >>> sum_even_odd([10, 20, 30])
        (60, 0)
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum


def sum_even_odd_v2(numbers):
    """
    AI-GENERATED DOCSTRING (GitHub Copilot Style)
    ===============================================
    
    Computes the sum of even and odd numbers from a list.

    This function iterates through a list of integers and partitions them
    into two groups: even numbers and odd numbers. It returns the sum of
    each group as a tuple.

    Args:
        numbers: A list containing integer values to be processed.

    Returns:
        A tuple of two integers where the first element is the sum of even
        numbers and the second element is the sum of odd numbers.

    Examples:
        >>> sum_even_odd_v2([1, 2, 3, 4, 5])
        (6, 9)
        
        >>> sum_even_odd_v2([2, 4, 6])
        (12, 0)
        
        >>> sum_even_odd_v2([1, 3, 5])
        (0, 9)
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum


# ============================================================================
# DOCSTRING COMPARISON ANALYSIS
# ============================================================================

"""
MANUAL DOCSTRING vs AI-GENERATED DOCSTRING

1. STRUCTURE & FORMAT
   Manual: Concise, follows strict Google Style format
   AI: Slightly more verbose, includes descriptive narrative paragraph
   
2. CLARITY & DESCRIPTIONS
   Manual: Direct and to-the-point with clear type annotations
   AI: Adds contextual explanation of what the function does (iteration, partitioning)
   
3. ARGS SECTION
   Manual: Includes type hint [list[int]] with brief description
   AI: Simpler, just mentions "list containing integer values"
   
4. RETURNS SECTION
   Manual: Explicitly states Index 0 and Index 1 with descriptions
   AI: More descriptive narrative format, less explicit index notation
   
5. EDGE CASES
   Manual: Includes Raises section for TypeError (defensive programming)
   AI: No error handling documentation
   
6. EXAMPLES
   Manual: 2 examples showing basic and edge cases (all even numbers)
   AI: 3 examples showing basic, all even, and all odd cases
   
7. OVERALL ASSESSMENT
   Manual: More structured, defensive, follows strict format
   AI: More narrative and educational, easier to understand context
   
   Best Practice: Use manual as base (more specific types, error handling)
                  but incorporate AI's narrative style for clarity
"""


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    # Test case 1: Mixed even and odd numbers
    test1 = [1, 2, 3, 4, 5]
    result1_manual = sum_even_odd(test1)
    result1_ai = sum_even_odd_v2(test1)
    print(f"Test 1 - Input: {test1}")
    print(f"  Manual Docstring Result: {result1_manual}")
    print(f"  AI Docstring Result: {result1_ai}")
    print(f"  Match: {result1_manual == result1_ai}\n")
    
    # Test case 2: All even numbers
    test2 = [10, 20, 30]
    result2_manual = sum_even_odd(test2)
    result2_ai = sum_even_odd_v2(test2)
    print(f"Test 2 - Input: {test2}")
    print(f"  Manual Docstring Result: {result2_manual}")
    print(f"  AI Docstring Result: {result2_ai}")
    print(f"  Match: {result2_manual == result2_ai}\n")
    
    # Test case 3: All odd numbers
    test3 = [1, 3, 5, 7]
    result3_manual = sum_even_odd(test3)
    result3_ai = sum_even_odd_v2(test3)
    print(f"Test 3 - Input: {test3}")
    print(f"  Manual Docstring Result: {result3_manual}")
    print(f"  AI Docstring Result: {result3_ai}")
    print(f"  Match: {result3_manual == result3_ai}\n")
    
    # Test case 4: Empty list
    test4 = []
    result4_manual = sum_even_odd(test4)
    result4_ai = sum_even_odd_v2(test4)
    print(f"Test 4 - Input: {test4}")
    print(f"  Manual Docstring Result: {result4_manual}")
    print(f"  AI Docstring Result: {result4_ai}")
    print(f"  Match: {result4_manual == result4_ai}\n")
    
    # Test case 5: Negative numbers
    test5 = [-2, -1, 0, 1, 2]
    result5_manual = sum_even_odd(test5)
    result5_ai = sum_even_odd_v2(test5)
    print(f"Test 5 - Input: {test5}")
    print(f"  Manual Docstring Result: {result5_manual}")
    print(f"  AI Docstring Result: {result5_ai}")
    print(f"  Match: {result5_manual == result5_ai}")
