try:
    import numpy as np
    print("NumPy is installed.")
    # Simple test
    arr = np.array([1, 2, 3])
    print("Array created:", arr)
    print("Sum of array:", np.sum(arr))
except ImportError:
    print("NumPy is not installed. Please run: pip install numpy")
