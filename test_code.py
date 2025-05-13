## Write a sample code that does fibonacci sequence
def fibonacci(n):
    """Return the Fibonacci sequence up to n."""
    a, b = 0, 1
    sequence = []
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Test the fibonacci function
def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(3) == [0, 1, 1]
    assert fibonacci(4) == [0, 1, 1, 2]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]

# Run the test
if __name__ == "__main__":
    test_fibonacci()
    print("All tests passed!")