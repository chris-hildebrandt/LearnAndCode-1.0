# **Week 10: Organizing Objects and Data Structures - Example**

This README showcases examples of improving object and data structure organization within a project, with a focus on creating modular, maintainable code that aligns with the Quality Manifesto's emphasis on technical excellence.

## **Table of Contents**

- **[Before Refactoring](#before-refactoring)**
- **[After Refactoring](#after-refactoring)**
- **[Changes Made](#changes-made)**
- **[Impact of Changes](#impact-of-changes)**

## **Before Refactoring**

```cs
public class Customer
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    public string Address { get; set; }

    public void Save()
    {
        // Save customer to the database
    }

    public void SendEmail(string message)
    {
        // Send an email to the customer
    }
}

public class Order
{
    public int Id { get; set; }
    public int CustomerId { get; set; }
    public DateTime OrderDate { get; set; }
    public List<OrderItem> Items { get; set; }

    public void Save()
    {
        // Save order to the database
    }
}

```

## **After Refactoring**

```cs
public class Customer
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Email { get; set; }
    public string Address { get; set; }
}

public interface ICustomerRepository
{
    void Save(Customer customer);
}

public interface IEmailService
{
    void SendEmail(string emailAddress, string message);
}

public class CustomerService
{
    private readonly ICustomerRepository _customerRepository;
    private readonly IEmailService _emailService;

    public CustomerService(ICustomerRepository customerRepository, IEmailService emailService)
    {
        _customerRepository = customerRepository;
        _emailService = emailService;
    }

    public void SaveCustomer(Customer customer)
    {
        _customerRepository.Save(customer);
    }

    public void SendEmailToCustomer(Customer customer, string message)
    {
        _emailService.SendEmail(customer.Email, message);
    }
}

public class Order
{
    public int Id { get; set; }
    public int CustomerId { get; set; }
    public DateTime OrderDate { get; set; }
    public List<OrderItem> Items { get; set; }
}

public interface IOrderRepository
{
    void Save(Order order);
}

public class OrderService
{
    private readonly IOrderRepository _orderRepository;

    public OrderService(IOrderRepository orderRepository)
    {
        _orderRepository = orderRepository;
    }

    public void SaveOrder(Order order)
    {
        _orderRepository.Save(order);
    }
}

```

## **Changes Made**

- Separated data storage and business logic by introducing repository and service classes.
- Introduced an **`ICustomerRepository`** interface to enable easier substitution of storage mechanisms.
- Introduced an **`IEmailService`** interface to enable easier substitution of email providers.

## **Impact of Changes**

The changes made to the project have led to the following improvements:

- The **`Customer`** and **`Order`** classes are now focused on their data representation, adhering to the Single Responsibility Principle.
- The introduction of repository and service classes separates data storage and business logic, making the code more modular and maintainable.
- By introducing interfaces for repositories and the email service, the project now adheres to the Dependency Inversion Principle, enabling easier substitution of storage mechanisms and email providers.

These changes have made the code more readable, maintainable, and adherent to best practices, showcasing the importance of organizing objects and data structures in ensuring high-quality software.

Following these improvements, future development tasks, such as adding new features or modifying existing ones, will be more straightforward. Additionally, these changes make the project more adaptable to potential updates in storage mechanisms, email providers, or other dependencies, as they can be easily replaced without impacting the core functionality of the application.

By organizing objects and data structures effectively, we have ensured that our code is modular, maintainable, and efficient, aligning with the Quality Manifesto's emphasis on technical excellence. In summary, the changes made to the project showcase the positive impact of organizing objects and data structures in software development.
