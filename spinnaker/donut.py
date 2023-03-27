import math
import time

def render_frame(a, b):
    # Calculate the sin and cos values of a and b
    sin_a = math.sin(a)
    cos_a = math.cos(a)
    sin_b = math.sin(b)
    cos_b = math.cos(b)

    # Initialize the output string
    output = ""

    # Define the donut's parameters
    R1 = 1
    R2 = 2
    K2 = 5
    K1 = 150

    # Loop through the y-axis
    for y in range(-30, 30):
        # Loop through the x-axis
        for x in range(-30, 30):
            # Calculate the denominator of the equation for z
            denom = x * cos_b * cos_a + y * cos_b * sin_a + K2
            
            # Check if the denominator is close to zero
            if abs(denom) < 0.0001:
                z = 0
            else:
                z = 1.0 / denom

            xp = int((40 + K1 * z * (x * cos_b * sin_a - y * sin_b))) # Calculate the x-coordinate of the output point
            yp = int((12 + K1 * z * (x * cos_b * cos_a + y * sin_a))) # Calculate the y-coordinate of the output point

            # If the point is within the bounds of the output string, add it to the output
            if 0 <= xp < 80 and 0 <= yp < 24:
                output += "."

            else:
                output += " "

        output += "\n"

    # Print the output string to the console
    print(output)

# Main loop
def main():
    # Set the initial values for a and b
    a = 0
    b = 0

    # Loop indefinitely
    while True:
        # Clear the console
        print("\033[2J")

        # Render the frame
        render_frame(a, b)

        # Increment a and b
        a += 0.07
        b += 0.03

        # Sleep for a short time to control the animation speed
        time.sleep(0.05)

if __name__ == "__main__":
    main()