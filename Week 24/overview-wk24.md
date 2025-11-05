# **Week 24: Event-Driven Architecture**

Event-Driven Architecture (EDA) is fundamental to modern software development, powering everything from real-time notifications to complex microservices. Understanding EDA is crucial as it solves many common challenges in distributed systems, including real-time updates, system scalability, and loose coupling between services. Whether you're building a simple chat application or a complex e-commerce platform, you'll encounter event-driven patterns as they're used extensively in message queues, webhooks, pub/sub systems, and reactive programming.

## **Table of Contents**

- **[Learning Objectives](#learning-objectives)**
- **[Reading Assignment](#reading-assignment)**
- **[Resources](#resources)**
- **[Weekly Assignment](#weekly-assignment)**
- **[Submission Guidelines](#submission-guidelines)**
- **[Discussion Topics](#discussion-topics)**

## **Learning Objectives**

By the end of this week, you should be able to:

- Understand core concepts of event-driven architecture
- Identify key components: publishers, subscribers, and event brokers
- Recognize when to apply event-driven patterns
- Understand the differences between events, commands, and messages
- Grasp common EDA patterns and anti-patterns
- Identify real-world use cases for event-driven systems

## **Reading Assignment**

- **[What is Event-Driven Architecture?](https://aws.amazon.com/event-driven-architecture/)**
- **[Event-Driven Architecture Fundamentals](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven)**
- **[Event-Driven Architecture Pattern](https://microservices.io/patterns/data/event-driven-architecture.html)**
- **[The Power of Events: An Introduction to Event-Driven Systems](https://martinfowler.com/articles/201701-event-driven.html)**

## **Resources**

**Video Tutorials:**
- **[Event-Driven Architecture Explained](https://www.youtube.com/watch?v=DtuVN5g_e3k)**
- **[Event-Driven Architecture in the Real World](https://www.youtube.com/watch?v=ksRCq0BJef8)**
- **[Event-Driven Microservices](https://www.youtube.com/watch?v=moCcKZ_eHHs)**

**Technical Documentation:**
- **[Apache Kafka Documentation](https://kafka.apache.org/documentation/)**
- **[RabbitMQ Concepts](https://www.rabbitmq.com/tutorials/amqp-concepts.html)**
- **[AWS Event Bridge Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html)**

## **Weekly Assignment**

1. Analyze an existing system (can be your current project) and identify:
   - Potential use cases for events
   - Components that could benefit from loose coupling
   - Current tight coupling that could be improved with events

2. Document your findings, including:
   - Event examples with their producers and consumers
   - Benefits of implementing EDA in this context
   - Potential challenges and considerations
   - Real-world scenarios where EDA would improve system performance or maintainability

## **Submission Guidelines**

- Submit a README file to the submissions folder for your cohort
- Include your analysis and diagrams (if any)
- Open a PR with your name and week number (Example: dallen-pyrah-week-22)
- Review and comment on other students' submissions

## **Discussion Topics**

During your weekly meeting, be prepared to discuss:

- Differences between synchronous and asynchronous communication
- Trade-offs between traditional request-response and event-driven patterns
- Real-world examples of event-driven systems (e.g., social media feeds, e-commerce order processing)
- Common challenges in implementing EDA
- Best practices for event design and naming
- Error handling and reliability in event-driven systems
- How popular platforms use EDA (Netflix, Uber, LinkedIn)
- Integration patterns with existing systems