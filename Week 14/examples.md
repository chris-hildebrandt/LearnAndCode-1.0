# **Week 14: Boundaries & Integrations - Example (3rd Party Software)**

This README showcases examples of identifying and improving boundaries in a project when integrating with third-party software, focusing on creating clean interfaces between components and enhancing integrations. The purpose of this example is to demonstrate the positive impact of well-defined boundaries and integrations on software quality and continuous integration and deployment.

## **Table of Contents**

- **[Before Improving Boundaries and Integrations](#before-improving-boundaries-and-integrations)**
- **[After Improving Boundaries and Integrations](#after-improving-boundaries-and-integrations)**
- **[Changes Made](#changes-made)**
- **[Impact of Changes](#impact-of-changes)**

## **Before Improving Boundaries and Integrations**

```cs
public class WeatherService
{
    private readonly HttpClient _httpClient;

    public WeatherService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<WeatherInfo> GetWeatherInfoAsync(string city)
    {
        var response = await _httpClient.GetAsync($"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key");

        if (!response.IsSuccessStatusCode)
        {
            throw new HttpRequestException("Failed to fetch weather data.");
        }

        var json = await response.Content.ReadAsStringAsync();
        var weatherData = JsonConvert.DeserializeObject<WeatherData>(json);

        return new WeatherInfo(weatherData.Main.Temp, weatherData.Weather[0].Description);
    }
}

```

## **After Improving Boundaries and Integrations**

```cs
public interface IWeatherDataProvider
{
    Task<WeatherData> GetWeatherDataAsync(string city);
}

public class WeatherDataProvider : IWeatherDataProvider
{
    private readonly HttpClient _httpClient;

    public WeatherDataProvider(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<WeatherData> GetWeatherDataAsync(string city)
    {
        var response = await _httpClient.GetAsync($"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key");

        if (!response.IsSuccessStatusCode)
        {
            throw new HttpRequestException("Failed to fetch weather data.");
        }

        var json = await response.Content.ReadAsStringAsync();
        return JsonConvert.DeserializeObject<WeatherData>(json);
    }
}

public class WeatherService
{
    private readonly IWeatherDataProvider _weatherDataProvider;

    public WeatherService(IWeatherDataProvider weatherDataProvider)
    {
        _weatherDataProvider = weatherDataProvider;
    }

    public async Task<WeatherInfo> GetWeatherInfoAsync(string city)
    {
        var weatherData = await _weatherDataProvider.GetWeatherDataAsync(city);
        return new WeatherInfo(weatherData.Main.Temp, weatherData.Weather[0].Description);
    }
}

```

## **Changes Made**

- Identified boundaries between the components responsible for fetching weather data and processing it.
- Created a **`WeatherDataProvider`** class to handle interactions with the third-party weather API.
- Created an interface **`IWeatherDataProvider`** to decouple components and improve testability.
- Injected **`IWeatherDataProvider`** into **`WeatherService`** using dependency injection.

## **Impact of Changes**

The changes made to the project have led to the following improvements in managing boundaries and integrations:

- The **`WeatherService`** and **`WeatherDataProvider`** classes now have a clear separation of responsibilities, making the code more modular and maintainable.
- The introduction of the **`IWeatherDataProvider`** interface has decoupled the components, allowing for easier testing and substitution of different weather data provider implementations.
- Dependency injection has been used to improve the flexibility and maintainability of the code.

These changes have made the code more readable, maintainable, and adherent to best practices, showcasing
