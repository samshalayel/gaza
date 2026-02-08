#!/usr/bin/env python3
"""
Simple Python Test Program
Test file for Python compiler verification
"""

import sys
import datetime

def main():
    """Main function to test Python compiler"""
    
    print("=" * 50)
    print("🐍 Python Compiler Test")
    print("=" * 50)
    
    # Test basic operations
    print(f"Python Version: {sys.version}")
    print(f"Current Time: {datetime.datetime.now()}")
    
    # Test variables and types
    test_number = 42
    test_string = "Hello Gaza!"
    test_list = [1, 2, 3, 4, 5]
    test_dict = {"name": "Gaza Test", "status": "running"}
    
    print(f"\n📊 Variable Tests:")
    print(f"Number: {test_number} (type: {type(test_number).__name__})")
    print(f"String: {test_string} (type: {type(test_string).__name__})")
    print(f"List: {test_list} (type: {type(test_list).__name__})")
    print(f"Dictionary: {test_dict} (type: {type(test_dict).__name__})")
    
    # Test functions
    result = calculate_sum(10, 20)
    print(f"\n🔢 Function Test:")
    print(f"Sum of 10 + 20 = {result}")
    
    # Test loops
    print(f"\n🔄 Loop Test:")
    for i in range(1, 6):
        print(f"  Loop iteration: {i}")
    
    # Test conditionals
    print(f"\n⚖️ Conditional Test:")
    if test_number > 40:
        print("  ✅ Condition test passed!")
    else:
        print("  ❌ Condition test failed!")
    
    # Test list comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"\n📋 List Comprehension Test:")
    print(f"  Squares: {squares}")
    
    # Test exception handling
    print(f"\n🛡️ Exception Handling Test:")
    try:
        result = 10 / 2
        print(f"  Division result: {result}")
        # This will cause an error
        # result = 10 / 0
    except ZeroDivisionError:
        print("  ❌ Division by zero error caught!")
    except Exception as e:
        print(f"  ❌ Unexpected error: {e}")
    else:
        print("  ✅ No errors occurred!")
    
    print(f"\n🎉 Python compiler test completed successfully!")
    print("=" * 50)

def calculate_sum(a, b):
    """Simple function to calculate sum of two numbers"""
    return a + b

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

def test_advanced_features():
    """Test some advanced Python features"""
    print("\n🚀 Advanced Features Test:")
    
    # Generator
    def simple_generator():
        yield 1
        yield 2
        yield 3
    
    gen_values = list(simple_generator())
    print(f"  Generator values: {gen_values}")
    
    # Lambda function
    multiply_by_2 = lambda x: x * 2
    print(f"  Lambda (5 * 2): {multiply_by_2(5)}")
    
    # Fibonacci test
    fib_nums = fibonacci(10)
    print(f"  Fibonacci (10 terms): {fib_nums}")

if __name__ == "__main__":
    main()
    test_advanced_features()
    
    # Final status
    print(f"\n✅ Test file execution completed!")
    print(f"📅 Executed at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")