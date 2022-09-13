# Python Modules

Modules refer to a file containing,
* Python statements
* Definitions
##### A file containing Python code, for example: ` example.py,` is called a module, and its module name would be `example`.
We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.

### Let us create a module. Type the following and save it as `example.py.`

## Python Module example
````python
def add(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return result
 ````
### Python import statement
We can import a module using the import statement and access the definitions inside it using the dot operator as described above. Here is an example.

#### import statement example
````python
import math
print("The value of pi is", math.pi)
````
### Python from...import statement
We can import specific names from a module without importing the module as a whole. Here is an example.
#### import only pi from math module
````python
from math import pi
print("The value of pi is", pi)
````
Here, we imported only the pi attribute from the math module.
In such cases, we don't use the dot operator. We can also import `multiple attributes` as follows:
````python
 from math import pi, e
````

# Python Package
Similar files are kept in the same directory, for example, we may keep all the songs in the `"music"` directory. Analogous to this, Python has packages for `directories` and modules for `files.`
A directory must contain a file named
````python
__init__.py
````
in order for Python to consider it as a `package.`
#### Here is an example.
Suppose we are developing a game. One possible organization of packages and modules could be as shown in the `figure` below.


![Screenshot (264)](https://user-images.githubusercontent.com/81691323/189830165-0ab7267b-5426-49f2-a55b-c660024c7806.png)




### Importing module from a package
We can import modules from packages using the dot `(.) operator.`

For example, if we want to import the `start` module in the above example, it can be done as follows:
````python
import Game.Level.start
````
Now, if this module contains a `function` named `select_difficulty()`, we must use the full name to reference it.
````python
Game.Level.start.select_difficulty(2)
````
If this construct seems lengthy, we can import the module without the package `prefix` as follows:
````python
from Game.Level import start
````
We can now call the function simply as follows:
````python
start.select_difficulty(2)
````
Another way of importing just the required function (or class or variable) from a `module` within a `package` would be as follows:
````python
from Game.Level.start import select_difficulty
````
Now we can directly call this function.
````python
select_difficulty(2)
````




