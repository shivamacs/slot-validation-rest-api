# Assignment - Slot Validation APIs

## Setup and run server
### 1. Build the Docker image
```
~/$ cd slots
~/slots$ sudo docker build -t slots .
```
### 2. Run the Docker image as a container
```
~/slots$ sudo docker run -p 8000:8000 slots
```
### Docker image size
```
SIZE: 84.9 MB
```
Used ```python: 3.9-alpine```
<br><br>

## How to use the APIs
### 1. POST API to validate a slot with a finite set of values
All post requests to validate a slot with a finite set of values are served at:
```
http://localhost:8000/api/slots/validate1
```
#### Response format for successful request
```
{
    "filled": <filled flag>,
    "partially_filled": <partially filled flag>,
    "trigger": <trigger value>,
    "parameters": <params dict from func>
}
```
#### Response format for failed request
```
{
    "status": "failed",
    "message": "invalid_request"
    "error": <error.message>
}
```
#### Assumptions
1. if ```pick_first``` is true, then response ```parameters[key]``` field is set to the string of first value iff ```filled``` is ```True```.
2. if ```support_multiple``` is ```True``` and not all values are valid, then response ```parameters[key]``` field is sent empty in the response (based on a sample case shown in the assignment).
3. Either of ```pick_first``` or ```support_multiple``` must be present. If both are present, then they must not have same boolean value. If only one of them is present, then it must be ```True``` otherwise ```parameters[key]``` is sent empty in the response.
<br><br>

### 2. POST API to validate a slot with a numeric value extracted and constraints on the value extracted
All post requests to validate a slot with a numeric value extracted with constraints are served at:
```
http://localhost:8000/api/slots/validate2
```
#### Response format for successful request
```
{
    "filled": <filled flag>,
    "partially_filled": <partially filled flag>,
    "trigger": <trigger value>,
    "parameters": <params dict from func>
}
```
#### Response format for failed request
```
{
    "status": "failed",
    "message": "invalid_request"
    "error": <error.message>
}
```
#### Assumptions
1. if ```pick first``` is true, then response ```parameters[key]``` field is set to the string of first value iif it is valid, otherwise it will be empty even if 
all the remaining values are valid.
2. Either of ```pick_first``` or ```support_multiple``` must be present. If both are present, then they must not have same boolean value. If only one of them is present, then it must be ```True``` otherwise ```parameters[key]``` is sent empty in the response.
<br><br>

### Other points (for assignment purpose only)
1. ```@csrf_exempt``` is used here for hassle free POST requests (I do not support it!).
2. ```ALLOWED_HOSTS = ['*']``` in ```slots.settings```
3. ```localhost``` points to IP ```0.0.0.0``` in this project 
