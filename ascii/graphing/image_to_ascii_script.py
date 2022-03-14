
import sys
import getopt
from R2_to_bool import image_to_function
from fxn_to_ascii import function_to_ascii

def usage():
    """
    prints simple usage information
    """

    print("\nimage_to_ascii")
    print("args:")
    print("-i {path to image} : required, path to image file")
    print("\talias --image\n")
    print("-s {size} : optional, sets largest dimension, max 200")
    print("\talias --size\n")
    print("-h : prints usage information")
    print("\talias --help\n")

def str_to_int_in_range(opt, arg, min, max):
    """
    converts string to int, min <= x < max
    exits if fail (for use in arg parsing)
    """

    msg = f"{opt} takes an integer between {min} and {max - 1}"

    try:
        arg = int(arg)
    except ValueError as err:
        print(msg)
        sys.exit(1)

    if arg < min or arg >= max:
        print(msg)
        sys.exit(1)

    return arg


def main():
    # C-style arg parse bc I want to 
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:s:h", ["image=","size=","help"])
    except getopt.GetoptError as err:
        # print usage information and exit:
        print(err) # option arg not recognized
        usage()
        sys.exit(1)
    
    size = 100
    image = None

    for opt, arg in opts:
        if opt in ("-s", "--size"):
            size = str_to_int_in_range(opt, arg, 1, 201)
        elif opt in ("-i", "--image"):
            image = arg
        elif opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        else:
            input(f"Unhandled option {arg}. Press ENTER to continue anyways")

    if image == None:
        print("requires image path")
        usage()
        sys.exit(0)

    f = image_to_function(image, max_dim = size)
    function_to_ascii(f, size, size, 0, 0)

if __name__ == "__main__":
    main()