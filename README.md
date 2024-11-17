# PYTHON WEATHER APP
#### Video Demo:  <https://youtu.be/zQCLlMr0mqU>
#### Description:
This is a simple console-based python weather application. At first you are presented with a table for user options such as getting your city's weather, getting a random city's weather and maybe if you want, to get the weather for multiple cities at once.

At first, I did not know what I could build for my final project. I really struggled with my creativity, so I opted for a simple weather application. This weather application uses the free OpenWeatherMap API to get weather data, so I signed up for OpenWeatherMap to get an API Key, then I went to work.

Once you run the program, you are allowed to choose four options. 1 - if you want to check a city's weather, 2 - if you want to check a random city's weather, 3 - if you want to check the weather of multiple cities, and 4 - if you want to exit the program.

With the first option, you are kindly prompted first for the country. This is to ensure that you get the correct city that you want. If you simply provide the city, then the program will end up really buggy! Like there's different San Antonios in the world. Which San Antonio are you getting? So it's better to specify which country you want to check first before moving to the city. After entering the country input, you are prompted for the city input. If the city is found, it will display the weather info such as temperature, max temp, min temp, "feels like" temp, weather description. I wanted to add more info but I feel like it could just cluster up the terminal by adding additional unnecessary info for the user, which is just bad user experience.

Second option allows you to check the weather of a random city. It uses the random module and selects a random city from a pre-defined list composed of several cities around the world, and displays the weather data for that city. It's a neat little feature if you're curious or just want to see some random weather data from some random city.

Third option is about allowing you to type in multiple cities at once, separated by commas, and display them simultaneously. This allows for multiple checkings without having to run the program over and over and over again which is very tedious. This option removes that repetitiveness and has the program to display the weather data from multiple cities at once. This is a very handy feature if you want to check the weather in other cities like your families far from you or friends far from you or if you're planning a trip from your city to out of town.


And we have our final option, which is just the exit option. If you choose this, you'll see an exiting message for a few seconds and then the program will exit using sys.exit(). Pretty simple enough.

I debated if I want to add more features but I feel like that it's pretty simple enough. A simple Python console based app that asks for your location and displays weather data.

This is my final project and this was CS50P!
