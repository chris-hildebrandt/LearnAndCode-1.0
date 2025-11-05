# **Week 12: Error Handling - Example**

This README showcases examples of improving error handling in a project, focusing on creating robust, reliable software that aligns with the Quality Manifesto's emphasis on domain knowledge.

## **Table of Contents**

- **[Before Error Handling Improvements](#before-error-handling-improvements)**
- **[Changes Made](#changes-made)**
- **[After Error Handling Improvements](#after-error-handling-improvements)**
- **[Impact of Changes](#impact-of-changes)**

## **Before Error Handling Improvements**

```cs
public class FileService
{
    public string ReadFile(string filePath)
    {
        using (var reader = new StreamReader(filePath))
        {
            return reader.ReadToEnd();
        }
    }
}

```

## **Changes Made**

- Added proper exception handling using try-catch blocks.
- Introduced custom exception classes for domain-specific errors.
- Implemented logging for better troubleshooting and monitoring.

## **After Error Handling Improvements**

```cs
public class FileService
{
    private readonly ILogger _logger;

    public FileService(ILogger logger)
    {
        _logger = logger;
    }

    public string ReadFile(string filePath)
    {
        try
        {
            using (var reader = new StreamReader(filePath))
            {
                return reader.ReadToEnd();
            }
        }
        catch (FileNotFoundException ex)
        {
            _logger.LogError($"File not found: {filePath}", ex);
            throw new CustomFileNotFoundException($"The file '{filePath}' was not found.", ex);
        }
        catch (Exception ex)
        {
            _logger.LogError($"Error reading file: {filePath}", ex);
            throw new CustomFileReadException($"An error occurred while reading the file '{filePath}'.", ex);
        }
    }
}

```

## **Impact of Changes**

The changes made to the project have led to the following improvements in error handling:

- The **`ReadFile`** method now has proper exception handling, which makes the application more robust and reliable.
- The introduction of custom exception classes improves the readability of the code and makes it easier to understand domain-specific errors.
- Implementing logging allows for better troubleshooting and monitoring of potential issues.

These changes have made the code more resilient and adherent to best practices, showcasing the importance of error handling in ensuring high-quality software.

By improving error handling, we have made our application more reliable and user-friendly. Additionally, these changes help developers better understand the application's domain and allow them to handle errors more effectively. This aligns with the Quality Manifesto's emphasis on domain knowledge and the importance of error handling in creating robust, reliable software.
