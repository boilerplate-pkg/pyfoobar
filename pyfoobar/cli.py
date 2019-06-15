import sys
import getopt


# if __name__ == "main":
opts, args = getopt.getopt(sys.argv, "?hH")
print(sys.argv)

msg = "hello, world"
msg.split(",")