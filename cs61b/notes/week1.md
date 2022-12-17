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

