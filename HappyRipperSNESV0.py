import os
from re import M
import sys

def main():
    
    if len(sys.argv) < 3: 
        print("Error: Invalid SMC header")
        return

    with open(sys.argv[1], "rb") as f:
        data = f.read()

    # Check for valid SMC header
    if data[0:4] != b"\xFE\x80\x00\x01":
        print("Error: Invalid SMC header")
        return

    # Get ROM size and calculate number of banks
    rom_size = (data[4] << 8) | data[5]
    num_banks = rom_size // 0x2000

    # Get title of ROM and create output directory based on it
    title = ""
    for i in range(0x10, 0x20):
        if data[i] == 0: break

        title += chr(data[i])

    output_dir = os.path.join(sys.argv[2], title)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    

    # Iterate through all banks and save them to file
    for i in range(num_banks):
        bank = data[0x2000 * i : 0x2000 * (i + 1)]

        with open(os.path.join(output_dir, "{:04X}.bin".format(i)), "wb") as f:
            f.write(bank)

            print("Wrote bank {:04X}".format(i))

            sys.stdout.flush()

main()
print(main())

