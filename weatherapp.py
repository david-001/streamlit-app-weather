# # Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

# import streamlit as st
# import pandas as pd
# import requests

# # OpenWeatherMap API key (replace with your own key)
# api_key = st.secrets["weather_api"]

# # Streamlit app title
# st.title("Weather Data Visualization")

# # User input for city and country
# city = st.text_input("Enter city name", "London")
# country = st.text_input("Enter country code", "GB")

# # API request to OpenWeatherMap
# url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}"
# response = requests.get(url)
# data = response.json()

# # Display weather information
# if response.status_code == 200:
#     st.subheader("Current Weather in {}:".format(data["name"]))
#     st.write("Temperature: {} °C".format(data["main"]["temp"]))
#     st.write("Weather: {}".format(data["weather"][0]["description"]))
#     st.write("Humidity: {}%".format(data["main"]["humidity"]))
#     st.write("Wind Speed: {} m/s".format(data["wind"]["speed"]))
#     df = pd.DataFrame(
#     [[data["coord"]["lat"],data["coord"]["lon"]]],    
#     columns=['lat', 'lon'])
#     st.map(df)
    
# else:
#     st.write("Error fetching weather data. Please check your input or try again later.")

# # You can add more features and visualizations here based on the weather data


# # API request to OpenWeatherMap
# url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}"
# response = requests.get(url)
# data = response.json()

# # Display weather information
# if response.status_code == 200:
#     st.subheader("Weather Forecast for {}:".format(data["city"]["name"]))

#     # Extract temperature, humidity, and wind speed data
#     timestamps = [entry["dt"] for entry in data["list"]]
#     temperatures = [entry["main"]["temp"] for entry in data["list"]]
#     humidity = [entry["main"]["humidity"] for entry in data["list"]]
#     wind_speed = [entry["wind"]["speed"] for entry in data["list"]]

#     # Create DataFrame for plotting
#     df = pd.DataFrame({
#         "Timestamp": pd.to_datetime(timestamps, unit='s'),
#         "Temperature (°C)": temperatures,
#         "Humidity (%)": humidity,
#         "Wind Speed (m/s)": wind_speed
#     })

#     # Plot temperature, humidity, and wind speed trends
#     st.subheader("Temperature, Humidity, and Wind Speed Trends:")
#     st.line_chart(df,x="Timestamp",y="Temperature (°C)")
# else:
#     st.write("Error fetching weather data. Please check your input or try again later.")





#-----------------------------------------------------
import streamlit as st
import requests
import pandas as pd
import altair as alt

# Streamlit app title
st.title("Movie Rating Visualization")

# User input for movie title
movie_title = st.text_input("Enter Movie Title", "lion king")

# OMDb API key (you need to sign up for a free API key)
api_key = st.secrets["omdb_api"]

# Perform a search on the OMDb API
url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    movie_data = response.json()

    # Display movie details
    st.subheader("Movie Details:")
    st.write(f"Title: {movie_data['Title']}")
    st.write(f"Year: {movie_data['Year']}")
    st.write(f"IMDb Rating: {movie_data['imdbRating']}")

    # Visualize the IMDb rating using a bar chart
    st.subheader("IMDb Rating Visualization:")
    df = pd.DataFrame({'Movie': [movie_data['Title']], 'IMDb Rating': [float(movie_data['imdbRating'])]})
    chart = alt.Chart(df).mark_bar().encode(
        x='Movie',
        y='IMDb Rating',
        color='Movie'
    ).properties(width=300, height=200)

    st.altair_chart(chart, use_container_width=True)

else:
    st.write(f"Error: {response.status_code}. Movie not found or there was an issue fetching data.")