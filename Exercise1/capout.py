import io
import sys

# Function to capture print output
def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        func(*args, **kwargs)
    finally:
        sys.stdout = old_stdout

    return new_stdout.getvalue()

# Example function to demonstrate capturing output
def example_print():
    print("Hello, World!")

# Capture the output of the example_print function
output = capture_output(example_print)
print(f"Captured Output: {output}")