##
# Write a program that displays the dimensions of a letter-size (8.5 x 11 inch) sheet of paper in millimeters.
# There are 25.4 millimeters per inch.
# Write a program that computes and displays the perimeter of a letter-size (8.5 x 11 inch) sheet of paper
# and the length of its diagonal.

# create a constant
CONVERTER = 25.4
WIDTH = 8.5
HEIGHT = 11

print("The dimensions of a letter-size sheet of paper in millimeters: %.2f x %.2f" % (WIDTH*CONVERTER, HEIGHT*CONVERTER) )

