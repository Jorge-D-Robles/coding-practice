# Week 1 Notes - CS61b

## Lecture 1

### Introduction  
<br>

1. All code in Java must be part of a class.

2. We delimit the beginning and end of segments of code with a {}.

3. All statements in Java must end with a semicolon.

4. For code to run we need public static void main(String[] args) { ... }

5. We can use the System.out.println() method to print things to the screen.

6. We can use the System.out.print() method to print things to the screen without a newline.

7. We can use the System.out.printf() method to print things to the screen with formatting.

```
public class helloWorld {
    public static void main(String[] args) {
        string x = "Hello World";
        System.out.println(x);
    }
}
```

---

### Primitive Types
Before Java variables can be used, they must be declared and have a type. (int, string, double, etc.)
In Java, there are two types of variables: primitive types and reference types.

<br>

### Functions

To declare a function we use the following syntax:

Starting with public static (for now), then the return type, then the function name. Then we have the parameters in parentheses, and finally the body of the function in curly braces.

```
public static int add(int x, int y) {
    return x + y;
}
```

All functions must be part of a class. A function that is part of a class is called a "method", so all functions in Java are methods.

<br>

---

<br>

## Lecture 2

### Compiling Java Code

In terminal: Type: javac filename.java
This will compile the code into a bytecode file with a .class extension.

To run this class, type java filename

Note - to run a class, you *must* define a main method.

<br>

## Terminology
```
public class Dog {
    public int weightInPounds; // instance variable

    public Dog(int startWeight) { // constructor 

        weightInPounds = startWeight;
    }
    
    public void makeNoise() //instance method, non-static
    {
        if (weightInPounds < 10) {
            System.out.println("yip!");
        } else if (weightInPounds < 30) {
            System.out.println("bark.");
        } else {
            System.out.println("woof!");
        }
    }
}
```
### *Constructor* 
- A special method that is called when an object is created. It is used to initialize the state of the object. It has the same name as the class.

### *Instance Variable*

- A variable that is declared inside a class, but outside of any method. It is called an instance variable because its value is unique to each instance of the class.

### *Instance Method*

- A method that is called on an object. It can access and modify the state of the object with which it is associated.

### *Static Method*

- A method that is called on a class. It cannot access or modify instance variables.

### *Static Variable*

- A variable that is declared with the static keyword. It belongs to the class, not the object.

