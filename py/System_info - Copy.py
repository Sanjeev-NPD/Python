import platform
import os
import shutil

def system_info():
    print("System Information:")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Python Compiler: {platform.python_compiler()}")
    print(f"Python Build: {platform.python_build()}")
    print(f"Platform Info: {platform.platform()}")
    print(f"System User: {os.getlogin()}")

    # Additional information using standard libraries
    print("\nAdditional System Information:")
    total, used, free = shutil.disk_usage("/")
    print(f"Disk Total Space: {total / (1024 ** 3):.2f} GB")
    print(f"Disk Used Space: {used / (1024 ** 3):.2f} GB")
    print(f"Disk Free Space: {free / (1024 ** 3):.2f} GB")

system_info()
