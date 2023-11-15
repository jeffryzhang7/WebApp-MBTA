# WebApp-MBTA
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 
### 1. Project Overview** (~1 paragraph)
#### This project allows me to  demonstrate the use of web APIs to retrieve geographic and public transport information from MBTA. It fetches latitude and longitude coordinates for a specified location using the Mapbox API and extracts coordinates from a JSON response. And then I was able to find the nearest MBTA  stop to a given latitude and longitude, including wheelchair accessibility information. The final functionalitiesenables users to input a location name and receive the nearest MBTA stop details using both Mapbox and MBTA APIs. It was pretty fun to incorporate my functions to a webpage using flask, but I also have met some challenges while running it.

### 2. Reflection
#### The part one of setting up the MBTA helper module went pretty well with testing, thought have I encountered someminor errors while accesing APIs during the process. The result, neverthless, was running well with my tests of multiple locations,a dn it was giving out the accurate and authtic outputs, which is encouraging.

#### Since I am working independently, there is no work dibvision for this assignment.

#### Throughout this assignment, a variety of functions and libraries are utilized to interact with web APIs and process data. The requests library is employed for making HTTP requests to the Mapbox API, while urllib.request and urllib.parse are used for URL handling and encoding parameters. JSON processing is carried out using Python's native json library, facilitating the decoding of API responses into Python data structures. The scripts define custom functions like get_coordinates, extract_coordinates, and find_closest_mbta_stop, which encapsulate the logic for fetching geographic coordinates, extracting data from JSON responses, and determining the nearest public transport stop, respectively. These functions showcase structured programming and API interaction techniques in Python. ChatGPT also played a vital role in debugging and explaining part of the functionalities. 

#### The webapp built by flask however, was not running as well as I expected, so I have to dig into the FLASK a little more to perform better in the future. 