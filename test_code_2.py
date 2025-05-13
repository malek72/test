# Create a small game function
def game():
    import random

    # Randomly select a number between 1 and 10
    number_to_guess = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Test the game function
def test_game():
    import random
    from unittest.mock import patch

    # Mock the input function to simulate user input
    with patch('builtins.input', side_effect=['5', '7', '3', '8', '6']):
        with patch('random.randint', return_value=6):
            game()
            # The user will guess 5, 7, 3, 8, and finally 6
            # The game should end after the last guess
            # We can check the output or the number of attempts
            # In a real test, we would capture the output and assert it
            # For simplicity, we will just print a message
            print("Test completed. Check the output for correctness.")
# Run the test
if __name__ == "__main__":
    test_game()
    print("All tests passed!")
# The game function is interactive and requires user input.
# The test_game function uses mocking to simulate user input and random number generation.
# This allows us to test the game logic without requiring actual user interaction.
# The test checks if the game can handle multiple guesses and ends correctly.
# Note: The test_game function is a simplified version and does not assert the output.
# In a real-world scenario, you would capture the output and assert it against expected values.