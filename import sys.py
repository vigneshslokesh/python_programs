import sys

# Add the custom site-packages path to sys.path
package_path = r'c:\users\vigne\appdata\local\programs\python\python311\lib\site-packages'
if package_path not in sys.path:
    sys.path.append(package_path)

# Now import numpy
import numpy as np

# Example usage of numpy
print(np.__version__)