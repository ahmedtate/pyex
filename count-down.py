import time

def countdown_timer(seconds):
    while seconds > 0:
        print(seconds, end='\r')  # Print the countdown on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("Time's up!")

# Example usage
countdown_timer(10)  # Set countdown time in seconds
