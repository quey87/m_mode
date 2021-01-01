import os


def one():
	os.system("ifconfig wlan0 down")
	os.system("iwconfig wlan0 mode monitor")
	os.system("ifconfig wlan0 up")
	os.system("iwconfig")
def two():
	os.system("ifconfig wlan0 down")
	os.system("iwconfig wlan0 mode managed")
	os.system("ifconfig wlan0 up")
	os.system("iwconfig")

print("""
1) MONITOR MODE
2) MANAGED MODE

""")
a = input(": ")

if a == "1":
	one()
elif a == "2":
	two()
else:
	print("Wrong Key")