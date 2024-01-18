Task 1

Let’s imagine that you’re visiting a country where it’s a custom to have breakfast at 7:00 to 8:00 window, lunch at 12:00 to 13:00, and finish with dinner at 18:00 to 19:00. Let’s create a helper for us to check if it’s time to have a meal and what kind of meal it will be. 

Implement a program that asks the user to enter a time and outputs “time for breakfast”, “time for launch”, “time for dinner”. 
If it’s not yet time to eat, just don’t output anything.

Time windows specified above are inclusive, so 12:00, 12:05 and 13:00 - are all good times to get a launch according to our helper. 
Accepted time format will be a 24 hour time, so something like *:** (7:00) or **:** (07:00) should work.
To make our code a bit more reusable, we want to structure our program to also include a “time_convert” function, that accepts time in the described string format and will return it back in float format. So for the “9:30” input it will return “9.5”. This useful function should be a part of the algorithm that produces the final result, so we will call this function at one point of our program.

Let’s assume that inputs are valid, we don’t need to validate them.


Task 2

You have json containing meta information about a game build.

Create update() function that takes following arguments:
* initial_meta - initial meta information to modify
* command - append or delete
* namespace - namespace of value that needs to be appended or deleted
* value/s - value or list of values
* type - optional argument for append command, default is "1"

1) Load json to python as "meta" variable
2) Run update() with args (meta, "append", "GTL::Build::Tags", ["DX13", "Uplay", "DLSS"], 1)
3) Run update() with arguments (meta_new, "delete", "GTL::Build::Categories", "NODRM")
4) Output new meta info to json

All values of a namespace must be unique
Number order shouldn't have gaps f.e. 1, 3, 4 is wrong
Number order in the input/output array can be random f.e 4,2,3,1

Input json example:
[
    {
        "Name": "GTL::Build::Tags::1",
        "Type": 1,
        "Value": "Aftermath"
    },
    {
        "Name": "GTL::Build::Tags::2",
        "Type": 1,
        "Value": "SL"
    },
    {
        "Name": "GTL::Build::Tags::3",
        "Type": 1,
        "Value": "NVNGX"
    },
    {
        "Name": "GTL::Build::Tags::4",
        "Type": 1,
        "Value": "Steam"
    },
    {
        "Name": "GTL::Build::Tags::5",
        "Type": 1,
        "Value": "DLSS"
    },
    {
        "Name": "GTL::Build::Categories::1",
        "Type": 1,
        "Value": "NODRM"
    },
    {
        "Name": "GTL::Build::Categories::2",
        "Type": 1,
        "Value": "GPDS"
    },
]


Task 3

Cars are the most popular way of transportation in the USA and many countries around the world. It's only natural that people want to find a way to standout from the crowd when they buy their new vehicle. One of the ways to have some fun with your car is to order what is called a "personalized plate", a special type of vehicle registration plate with a funny word or a number which is important for the driver.
With a system like that there are always ways for abuse, so local or federal governments like to introduce lists or requirements. It can be a list like this:
    • Plates are required to start with at least two letters.
    • Needs to contain a minimum of 2(letters or numbers) characters and a maximum of 6.
    • Numbers should only be used at the end of the plate, so GTL42 is ok, but GPDS2X is not.
    • First number used must not be a '0'.
    • No whitespace characters or punctuation marks are allowed.

In this program you will need to implement a validator for personalized plates. It will ask users to enter plate word/number sequence they want to get, and output "Valid plate!" or "Sorry, invalid plate" in the appropriate cases.

As we like to have our code reusable, we want to implement this program via a number of validator functions. At the very least we want to have a 'main' entry point function and internal 'is_plate_valid' function, that accepts plates in string type and returns bool after checking all the requirements. You can implement additional smaller validation functions to structure your code better.
