<style lang="scss">
    @import '@/assets/styles/app.css';
</style>

<template>
    <div id="app">
        <h1>Weather App</h1>
        <div class="input_container">
            <input class="city_input" v-model="city" placeholder="City" />
            <input class="state_input" v-model="stateOrCountry" placeholder="State or Country" />
            <button class="btn_input" @click="refreshWeatherData">Get Weather</button>
        </div>

        <div class="main-container" v-if="weatherData">
            <h2>Location: {{ weatherData.name }}</h2>
            <div class="weather-container">
                <h2>Current Weather</h2>
                <p>Weather: {{ weatherData.weather[0].description }}</p>
                <p>Temperature: {{ weatherData.main.temp }} °F</p>
                <p>Humidity: {{ weatherData.main.humidity }} %</p>
                <p>Wind Speed: {{ weatherData.wind.speed }} mph</p>
                <p>Wind Direction: {{ weatherData.wind.deg }}°</p>
                <p>Air Pressure: {{ weatherData.main.pressure }} hPa</p>
            </div>
            
            <div class="sun-container">
                <h2>Sunrise / Sunset</h2>
                <p>Sunrise: {{ formatDate(weatherData.sys.sunrise, weatherData.timezone) }}</p>
                <p>Sunset: {{ formatDate(weatherData.sys.sunset, weatherData.timezone) }}</p>
            </div>
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
                intervalId: null,
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

            formatDate(timestamp) 
            {
                const date = new Date(timestamp * 1000);

                return date.toLocaleTimeString(navigator.language, {
                    hour: "2-digit",
                    minute: "2-digit",
                });
            },

            refreshWeatherData()
            {
                if (this.intervalId)
                    clearInterval(this.intervalId);

                this.fetchWeatherData();

                this.intervalId = setInterval(this.fetchWeatherData, 5000);
            },
        },
    };
</script>
