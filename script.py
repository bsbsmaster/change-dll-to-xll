import os
from ctypes import CDLL

def load_dll(dll_path):
    """Load the DLL using ctypes."""
    if not os.path.isfile(dll_path):
        print(f"File not found: {dll_path}")
        return None

    try:
        dll = CDLL(dll_path)
        return dll
    except Exception as e:
        print(f"Failed to load DLL: {e}")
        return None

def create_xll(dll_path, xll_path):
    """Create an XLL file from the DLL using pyxll."""
    try:
        import pyxll
        from pyxll import create_xll
        
        # Define the settings for the XLL
        settings = {
            "modules": [dll_path],
            "name": "MyXLL",
            "version": "1.0.0"
        }
        
        # Create the XLL
        create_xll(xll_path, **settings)
        print(f"XLL created successfully at {xll_path}")
    except ImportError:
        print("pyxll package is not installed. Install it using 'pip install pyxll'.")
    except Exception as e:
        print(f"Failed to create XLL: {e}")

def main(dll_path):
    """Main function to load DLL and create XLL."""
    xll_path = dll_path.replace(".dll", ".xll")
    
    # Load the DLL
    dll = load_dll(dll_path)
    if not dll:
        return
    
    # Create the XLL
    create_xll(dll_path, xll_path)

if __name__ == "__main__":
    dll_path = "reverse_32bit.dll"  # Provide the correct DLL path here
    main(dll_path)
