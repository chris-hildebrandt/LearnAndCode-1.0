# **Week 4: Functions - Refactoring Example**

This README showcases an example of refactoring code with a focus on improving function names and structure. The purpose of this example is to demonstrate the positive impact of well-named and well-structured functions on code readability and maintainability.

## **Table of Contents**

- **[Before Refactoring](#before-refactoring)**
- **[After Refactoring](#after-refactoring)**
- **[Refactoring Explanation](#refactoring-explanation)**

## **Before Refactoring**

```cs
// Sample code with poor function names and structure
using System;

public class Operations
{
    public static int Op(int a, int b, string c)
    {
        if (c == "add") return a + b;
        if (c == "multiply") return a * b;
        return -1;
    }

    public static void Main(string[] args)
    {
        int result = Op(3, 5, "add");
        Console.WriteLine(result);
    }
}

```

## **After Refactoring**

```cs
// Refactored code with improved function names and structure
using System;

public class Operations
{
    public static int Add(int firstNumber, int secondNumber)
    {
        return firstNumber + secondNumber;
    }

    public static int Multiply(int firstNumber, int secondNumber)
    {
        return firstNumber * secondNumber;
    }

    public static void Main(string[] args)
    {
        int result = Add(3, 5);
        Console.WriteLine(result);
    }
}

```

## **Refactoring Explanation**

In this refactoring example, we made the following changes to improve the function names and structure:

1. Renamed the function **`Op()`** to two separate functions, **`Add()`** and **`Multiply()`**. This change makes the code more readable and maintainable by providing clearer context and reducing ambiguity in the function's purpose.
2. Removed the **`string c`** parameter from the original **`Op()`** function and split its functionality into the two new functions. This change simplifies the function signatures and makes the code more modular and easier to understand.

These changes make the code more readable and maintainable by providing clearer context and reducing ambiguity in the function's purpose and structure.
