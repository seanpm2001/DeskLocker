# Start of script
# The Python desktop locker script
# Import section
import pygui()
import os()
# Functions section
def supported_environments():
	print("Supported desktop environments: ")
	# GNOME
	print("GNOME 1\nGNOME 2\nGNOME 3\nGNOME 40\nGNOME 41")
	# KDE
	print("KDE 1\nKDE 2\nKDE 3\nKDE 3.5\nKDE 4\nKDE 5")
	# Cinnamon
	print("CINNAMON")
	# LXQT
	print("LXQT")
	# LXDE
	print("LXDE")
	# Windows NT
	print("WINDOWS_NT 3.1 (Windows NT 3.1, Windows NT 3.11)\nWINDOWS NT 3.5 (Windows NT 3.5/Windows NT 3.51)\nWINDOWS_NT 4.0 (Windows NT workstation 4.0)\nWINDOWS_NT 5.0 (Windows 2000)\nWINDOWS_NT 5.1 (Windows XP)\nWINDOWS_NT 6.0 (Windows Vista)\nWINDOWS_NT 6.1 (Windows 7)\nWINDOWS_NT 6.2 (Windows 8)\nWINDOW_NT 6.3 (Windows 8.1)\nWINDOWS_NT 10.0 (Windows 10)\nWINDOWS_NT 11.0 (Windows 11)")
	# MacOS Aqua
	print("AQUA (Mac OS X, OS X, MacOS 10, MacOS 11, MacOS 12)")
	# Other
	print("Support for other desktop environments coming soon")
	noMore = input("Press [ENTER] key to continue")
	break
def interface_gnome_debian_ubuntu():
	print("Coming soon")
def interface_vanilla_linux():
	# Default fallback interface
	'''
	os.interface("titlebar")
	os.title = ("DLock 0.0.1")
	'''
	print("🔒️ [🔐️] Lock/Unlock grid")
	print("🔒️ [🔐️] Lock/Unlock wallpaper")
	print("🔒️ [🔐️] Lock/Unlock files (permissions required)")
	print("🔒️ [🔐️] Lock/Unlock folders (permissions required)")
	print("[Save settings] [Undo] [Redo] [Restore defaults] [Exit]")
	noMore = input("Press [ENTER] key to exit")
	break
# Variables section
grid_lock = bool(True)
wallpaper_lock = bool(True)
file_lock = bool(False)
folder_lock = bool(False)
permissions_root = bool(False) # Permissions are needed for changing settings
desktop_environment = str("Not set")
Custom_PID = int(44386) # Custom Process ID
# Start of program
return supported_environments()
print("Desktop locker\nLoading interface...")
return interface_vanilla_linux()
noMore = input("Press [ENTER] key to quit")
print("The program is closing...")
break
""" File info
File type: Python source file (*.py)
File version: 1 (2022, Thursday, February 3rd at 4:28 pm)
Line count (including blank lines and compiler line): 63
"""
# End of script
