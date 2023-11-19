# API Microservice

# Request Data
1) Add APIcall.py into the project directory
2) Make a subroccess call to the given python file, with arguments as (lat,lon) coordinates. These will be system arguments 1, and 2, the data requested will be in the JSON format. Example file shows how to access data within the file.
3) This will send data as a regular string type via print()
   
# Recieve Data
1) To receive data, request data with the subproccess call, then take the stdout of the microservice either sending JSON file or error message.
2) With the stdout of the json data, use json.loads in order to turn string back into a json string type.
3) Then either save jsoin file via a write loop using json.dump(), or use data using correct json syntax (as seen in example).
   
# Example use of service
<img width="601" alt="image" src="https://github.com/allecole/microservice/assets/107892544/e526152e-0667-4484-b82c-2c0f8b9290c3">

# UML Diagram
<img width="800" alt="uml diagram" src="https://github.com/allecole/microservice/assets/107892544/67dbefc8-3993-4018-ae9c-0b24e070b9f2">
