***Overview***
- The Stringmethods.py module provides a collection of custom string manipulation functions. These functions are designed to perform various operations on strings, including changing case, checking character properties, and more. This module is particularly useful for those who want to understand the basics of string operations by implementing them without relying on built-in Python methods.

***Module Functions***
Below is a detailed description of each function in the Stringmethods.py module:

**1. upper(x)**
- ***Purpose***: Converts all lowercase letters in the input string to uppercase.
- **Parameters:**
- x (str): The string to convert.
Returns: A new string with all lowercase letters converted to uppercase. Non-alphabetic characters remain unchanged.
- **Example:**
upper("Hello World!")  # Returns "HELLO WORLD!"
- **Description:**
The function iterates over each character in the string.
If the character is a lowercase letter (ASCII range 97-122), it converts it to its uppercase equivalent by adjusting the ASCII value.
Uppercase and non-alphabetic characters are added to the result without changes.

**2. lower(x)**
- Purpose: Converts all uppercase letters in the input string to lowercase.
- **Parameters:**
- x (str): The string to convert.
 Returns: A new string with all uppercase letters converted to lowercase. Non-alphabetic characters remain unchanged.
- **Example:**
lower("Hello World!")  # Returns "hello world!"
- **Description:**
The function iterates over each character in the string.
If the character is an uppercase letter (ASCII range 65-90), it converts it to its lowercase equivalent by adjusting the ASCII value.
Lowercase and non-alphabetic characters are added to the result without changes.

**3. swapcase(x)**
- Purpose: Converts all uppercase letters to lowercase and vice versa.
- **Parameters:**
- x (str): The string to convert.
Returns: A new string with all uppercase letters converted to lowercase and vice versa. Non-alphabetic characters remain unchanged.
- **Example:**
swapcase("Hello World!")  # Returns "hELLO wORLD!"
- **Description:**
The function iterates over each character in the string.
If the character is a lowercase letter, it converts it to uppercase.
If the character is an uppercase letter, it converts it to lowercase.
Non-alphabetic characters are added to the result without changes.

**4. isupper(x)**
- Purpose: Checks if all alphabetic characters in the string are uppercase.
- **Parameters:**
- x (str): The string to check.
Returns: True if all alphabetic characters are uppercase; False otherwise.
- **Example:**
isupper("HELLO")  # Returns True
isupper("Hello")  # Returns False
- **Description:**
The function iterates over each character in the string.
It returns False if it encounters any character that is not an uppercase letter (ASCII range 65-90).
If all alphabetic characters are uppercase, it returns True.

**5. islower(x)**
- Purpose: Checks if all alphabetic characters in the string are lowercase.
- **Parameters:**
- x (str): The string to check.
Returns: True if all alphabetic characters are lowercase; False otherwise.
- **Example:**
islower("hello")  # Returns True
islower("Hello")  # Returns False
- **Description:**
The function iterates over each character in the string.
It returns False if it encounters any character that is not a lowercase letter (ASCII range 97-122).
If all alphabetic characters are lowercase, it returns True.

**6. isdigit(x)**
- Purpose: Checks if all characters in the string are digits.
- **Parameters:**
x (str): The string to check.
Returns: True if all characters are digits; False otherwise.
- **Example:**
isdigit("12345")  # Returns True
isdigit("12345a")  # Returns False
- **Description:**
The function iterates over each character in the string.
It returns False if it encounters any character that is not a digit (ASCII range 48-57).
If all characters are digits, it returns True.

**7. isalpha(x)**
- Purpose: Checks if all characters in the string are alphabetic.
- **Parameters:**
- x (str): The string to check.
Returns: True if all characters are alphabetic; False otherwise.
- **Example:**
isalpha("Hello")  # Returns True
isalpha("Hello123")  # Returns False
- **Description:**
The function iterates over each character in the string.
It returns False if it encounters any character that is not an alphabetic letter (ASCII ranges 65-90 and 97-122).
If all characters are alphabetic, it returns True.

**8. isalnum(x)**
- Purpose: Checks if all characters in the string are either alphabetic or digits.
- **Parameters:**
- x (str): The string to check.
Returns: True if all characters are alphabetic or digits; False otherwise.
- **Example:**
isalnum("Hello123")  # Returns True
isalnum("Hello 123!")  # Returns False
- **Description:**
The function iterates over each character in the string.
It returns False if it encounters any character that is not an alphabetic letter or digit (ASCII ranges 65-90, 97-122, and 48-57).
If all characters are alphabetic or digits, it returns True.

**9. capitalize(x)**
- Purpose: Capitalizes the first character of the string.
- **Parameters:**
- x (str): The string to capitalize.
Returns: A new string with the first character converted to uppercase and all subsequent characters unchanged.
- **Example:**
capitalize("hello world!")  # Returns "Hello world!"
- **Description:**
The function iterates over each character in the string.
The first character is converted to uppercase if it is a lowercase letter.
Subsequent characters remain unchanged except if the first character was a non-letter and the subsequent characters are uppercase, they are converted to lowercase.

**10. startswith(x)**
- Purpose: Checks if the given string starts with a specified character.
- **Parameters:**
- x (str): The character to check against the start of the string.
Returns: True if the string starts with the specified character; False otherwise.
- **Example:**
startswith("H")  # Enter the string "Hello" when prompted, returns True
- **Description:**
The function prompts the user to input a string.
It checks if the first character of the input string matches the specified character x.

**11. endswith(x)**
- Purpose: Checks if the given string ends with a specified character.
- **Parameters:**
- x (str): The character to check against the end of the string.
Returns: True if the string ends with the specified character; False otherwise.
- **Example:**
endswith("!")  # Enter the string "Hello!" when prompted, returns True
- **Description:**
The function prompts the user to input a string.
It checks if the last character of the input string matches the specified character x.

**Usage**
- To use the Stringmethods.py module, follow these steps:

![image](https://github.com/ragh945/String_Module/assets/65483520/b49a0866-5ae8-48ca-84d1-95d717a5df92)







**Save the Module:**
- Save the code provided above in a file named Stringmethods.py.
  ![image](https://github.com/ragh945/String_Module/assets/65483520/6bcecb3d-f7e6-4033-8d4b-5753c69abfe8)





**Import the Module:**
- In your Python script or interactive shell, import the module
- import Stringmethods
  
**Call the Functions:**
- Use the functions by calling them with the appropriate arguments. For example:
- import Stringmethods
- print(Stringmethods.upper("hello"))  # Output: "HELLO"
- print(Stringmethods.isalpha("Hello123"))  # Output: False
  
**Summary**
The Stringmethods.py module offers a variety of string manipulation and checking functions that mimic some of the built-in Python string methods but implemented manually for educational purposes. Each function is designed to be simple and focus on a single aspect of string handling, making the module a useful learning tool for understanding string operations at a low level.
