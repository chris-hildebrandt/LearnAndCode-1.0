# **Week 7: Code Review - Example**

This README showcases an example of a code review process with a focus on improving code quality and maintainability. The purpose of this example is to demonstrate the positive impact of code review and implementing feedback on software quality and technical excellence.

## **Table of Contents**

- **[Before Code Review](#before-code-review)**
- **[Feedback from Code Review](#feedback-from-code-review)**
- **[After Implementing Feedback](#after-implementing-feedback)**
- **[Code Review Impact](#code-review-impact)**

## **Before Code Review**

```cs
// Sample code before code review
using System;
using System.Collections.Generic;

public class DataProcessor
{
    public void ProcessData(List<int> input)
    {
        List<int> p1 = new List<int>();
        List<int> p2 = new List<int>();

        for (int i = 0; i < input.Count; i++)
        {
            if (input[i] % 2 == 0)
            {
                p1.Add(input[i]);
            }
            else
            {
                p2.Add(input[i]);
            }
        }
    }
}

```

## **Feedback from Code Review**

1. Rename **`ProcessData()`** to a more descriptive name.
2. Rename variables **`p1`** and **`p2`** to provide more context.
3. Consider separating the logic for filtering even and odd numbers into separate methods.
4. Consider returning the results instead of modifying the data in place.

## **After Implementing Feedback**

```cs
// Sample code after implementing feedback from code review
using System;
using System.Collections.Generic;

public class DataProcessor
{
    public (List<int>, List<int>) SeparateEvenAndOddNumbers(List<int> input)
    {
        List<int> evenNumbers = new List<int>();
        List<int> oddNumbers = new List<int>();

        for (int i = 0; i < input.Count; i++)
        {
            if (IsEven(input[i]))
            {
                evenNumbers.Add(input[i]);
            }
            else
            {
                oddNumbers.Add(input[i]);
            }
        }

        return (evenNumbers, oddNumbers);
    }

    private bool IsEven(int number)
    {
        return number % 2 == 0;
    }
}

```

## **Code Review Impact**

The code review process and the subsequent implementation of feedback have led to the following improvements in the code:

1. The **`ProcessData()`** method has been renamed to **`SeparateEvenAndOddNumbers()`** for better clarity on its purpose.
2. Variables **`p1`** and **`p2`** have been renamed to **`evenNumbers`** and **`oddNumbers`** to provide more context.
3. The logic for checking even numbers has been moved to a separate method named **`IsEven()`**, making the code more modular and easier to understand.
4. The method **`SeparateEvenAndOddNumbers()`** now returns the separated even and odd numbers as a tuple, providing a clearer and more functional approach to handling data.

These changes have made the code more readable, maintainable, and adherent to best practices, showcasing the importance of code review in ensuring high-quality software.
