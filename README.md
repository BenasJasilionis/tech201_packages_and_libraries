# tech201_packages_and_libraries

# Libraries
* Libraries are a set of RELATED modules or packages bundled together
* Base libraries are libraries that are in built, they still have to be imported though
* Whole libraries can be imported using : `import <library>`
* When importing a whole library, need to specify what package you want to use in your code: `library.package()`
* Can also `import` a specific `package` from a library: `from <library> import <package>`
### Example library- random
* Importing the whole library:
````python
import random

print(random.random()) # Output = Random float
````
* Importing a specific package from the library
````python
from random import random

print(random()) # Output = Random float
````
# Modules
* A `module` is a collection of code or functions that uses the .py extension - allowing you to use that code/functions in your program
* Like `libraries`, they need to be `imported` before they can be used
* `Modules` and `libraries` allow us to carry out tasks while using minimal lines of code, since we do not have to write out the logic
* `Modules` which are in different files can be ran if they are first `imported`
* This can be done in 2 ways:
1) Import the file: `import <file_name`

With this method you will need to specify the file name everytime you want to run a function/module from the other file. For example: `<file_name>.<function>`
2) Import everything from the file: ` from <file_name> import *`
This allows us to just call the function as normal without specifying the file name

### Example modules
* `datetime` - Can tell you the time in your current machine
* `math`- has many built-in arithmetic operations
* `sys`- shows you where you are in your machine

# Packages

