#!/usr/bin/python3

# Programmed by Luiz Felipe
# GitHub: https://github.com/DieBoy/
# Distributed under the MIT license.


import sys, os

def msg(attrib, string):
	print("\033[%sm%s\033[00m" % (attrib, string), end="")

cerror = os.system("nasm -h >/dev/null")
if cerror != 0:
	print("NASM executable not found.")
	sys.exit(1)


print("Shellcoder.py - Programmed by Luiz Felipe")
print("GitHub: https://github.com/DieBoy/\n")
print("\tType 'show' for show the shellcode string.")
print("\tType 'reset' for reset the shellcode.")
print("\tType '#' + the name of the syscall for show your number.")
print("\tWrite Assembly code for view your machine code and add this for the shellcode string.")


shellstr = ""

try:
	while True:
		msg("31;1", "\n> ")
		asm = input()

		if asm == "":
			continue
		elif asm == "show":
			msg("34;1", shellstr + "\n")
			continue
		elif asm == "reset":
			msg("1", "Shellcode reseted.\n")
			shellstr = ""
			continue
		elif asm[0] == "#":
			os.system("cat /usr/include/x86_64-linux-gnu/asm/unistd_64.h | grep -m 1 '%s '>/tmp/ress; tail -c +14 /tmp/ress" % asm[1:])
			continue

		source = open("/tmp/shell.asm", "w")
		source.write(asm + "\ndb 0x90, 0xFF")
		source.close()

		cerror = os.system("nasm -f elf64 /tmp/shell.asm -o /tmp/shell.o")
		if cerror != 0:
			msg("31", "Error on Assembly the code. %d\n" % cerror)
			continue

		code = open("/tmp/shell.o", "rb")
		code.seek(0x180)
		shellcode = code.read()
		code.close()

		for i in range(0, len(shellcode)):
			if shellcode[i] == 0x90 and shellcode[i+1] == 0xFF: break

			c = format(shellcode[i], "02X")

			if(shellcode[i] == 0):
				msg("31;1", c + " ")
			else:
				msg("32;1", c + " ")

			shellstr += "\\x" + c

		print("")

except KeyboardInterrupt:
	print("\nExiting...")
	sys.exit(0)
