# Write a program that asks the user to enter the width and length of a room.
# Once the values have been read, your program should compute and display the
# area of the room. The length and the width will be entered as floating point
# numbers. Include units in your prompt and output message; either feet or meters,
# depending on which unit you are more comfortable working with.

print("Enter Width of the Room (in metres):")
width = float(input())
print("Enter Length of the Room (in metres):")
length = float(input())

area = width * length

print("Area of the Room is", area, "square metre.")
