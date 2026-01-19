import argparse
from encoding import encode
from encoding import decode

parser = argparse.ArgumentParser(description="Pingu translator CLI")
parser.add_argument("mode", choices=["encode", "decode"], help="encode or decode")
parser.add_argument("text", help="text to process")
args = parser.parse_args()

if args.mode == "encode":
    output = encode(args.text)
elif args.mode == "decode":
    output = decode(args.text)
else:
    print("Invalid mode. Use 'encode' or 'decode'.")
    exit(1)
print(output)
