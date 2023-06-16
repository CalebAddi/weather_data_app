<template>
    <div id="app">
        <h1>Weather App</h1>
        <input v-model="city" placeholder="City" />
        <input v-model="stateOrCountry" placeholder="State or Country (Optional)" />
        <button @click="fetchWeatherData">Get Weather</button>

        <div v-if="weatherData">
            <h2>Location: {{ weatherData.name }}</h2>
            <p>Temperature: {{ weatherData.main.temp }} °F</p>
            <p>Humidity: {{ weatherData.main.humidity }} %</p>
            <p>Wind Speed: {{ weatherData.wind.speed }} mph</p>
            <p>Wind Direction: {{ weatherData.wind.deg }}°</p>
            <p>Air Pressure: {{ weatherData.main.pressure }} hPa</p>
            <p>Weather: {{ weatherData.weather[0].description }}</p>
            <p>Sunrise: {{ formatDate(weatherData.sys.sunrise, weatherData.timezone) }}</p>
            <p>Sunset: {{ formatDate(weatherData.sys.sunset, weatherData.timezone) }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        data() 
        {
            return {
                city: "",
                stateOrCountry: "",
                weatherData: null,
            };
        }

        ,methods: 
        {
            async fetchWeatherData() 
            {
                const response = await fetch(
                `http://localhost:8000/api/weather/?city=${this.city}&state_or_country=${this.stateOrCountry}`
                );

                const data = await response.json();
                
                if (data.status === "success")
                    this.weatherData = data.data;

                else 
                console.error("Error fetching weather data");
            },

            formatDate(timestamp, timezoneOffset) 
            {
                const timezone = new Date().getTimezoneOffset() * 60 - timezoneOffset;
                const date = new Date((timestamp + timezone) * 1000);

                return date.toLocaleTimeString(navigator.language, {
                    hour: "2-digit",
                    minute: "2-digit",
                    hour12: false
                });
            },
        },
    };
</script>
