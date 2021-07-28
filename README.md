# Python-Essentials-LAB-3.4.1.12-The-Timer-Class

**Objectives**

•	improving the student's skills in defining classes from scratch;

•	defining and using instance variables;

•	defining and using methods.

**Scenario**

We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

•	objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;

•	the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.

**Use the following hints:**

•	all object's properties should be private;

•	consider writing a separate function (not method!) to format the time string.

**Expected output**
```
23:59:59
00:00:00
23:59:59
```

**Complete code includes**
```
def int_to_str(hrs):
    # This function adds leading zeros when the value is less than 10

def time_to_str(hrs, mins , sec):
    # This function implicitly convert time into string of the following form: "hh:mm:ss"

class Timer:
    def __init__(self, hrs = 0, mins = 0, sec = 0):
        # This constructor initiates private properties of the object

    def __str__(self):
        # This method makes class printable

    def next_second(self):
        # This method adds the next second and handles the overflow

    def prev_second(self):
        # This method substracts the second and handles the overflow
```
