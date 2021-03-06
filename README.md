## Dockerized-webapp-flask-bgcolorcode
This is a simple flask webapp that displays a colored background and a dynamic greeting message. 

### Dynamic Color
The color can be specified in two different ways:

  1. As a command line argument with --colorcode as the argument.
  2. As an Environment variable APP_COLORCODE.
    
In any other case, royal blue is set ad the default color.
  
Note: Command line argument precedes over environment variable.

### Dynamic Title
The dynamic greeting message can be specified in two different ways:

  1. As a command line argument with --title as the argument. Accepts any text message!
  2. As an Environment variable APP_TITLE. Accepts any text message.
    
In any other case, the static text "Cloud Computing - University of West Attica" is applied.

Note 3: Command line argument precedes over environment variable.
## Follow these steps in order to create your Dockerized-webapp-flask-bgcolor

1. First of all you have to clone this repository on your server.
```bash
    -$ mkdir -p ~/MyProjects
    -$ cd ~/MyProjects
    -$ git clone https://github.com/ele44339/Dockerized-webapp-flask-bgcolorcode.git
                      OR via SSH
    -$ git clone git@github.com:ele44339/Dockerized-webapp-flask-bgcolorcode.git
```
2. Now you have to build the Docker Image locally.
```bash
    -$ cd ~/MyProjects/Dockerized-webapp-flask-bgcolorcode
    -$ docker build . -t ele44339/flask-bgcolorcode:1.0
```
3. Now you have to spin up as many containers you want in different ports.

Royal blue color and Static title without any command line argument nor environmental variable.
```bash
    -$ docker run -p 8002:8000 ele44339/flask-bgcolorcode:1.0
```
Blue color with environmental variable and the Static title:
```bash
    -$ docker run -p 8000:8000 -e APP_COLORCODE="#0000FF" ele44339/flask-bgcolorcode:1.0
```
Navy color with command line argument and the static title:
```bash
    -$ docker run -p 8001:8000 ele44339/flask-bgcolorcode:1.0 --colorcode="#000080"
```
Red color and Dynamic title with environmental variables:
```bash
    -$ docker run -p 8003:8000 -e APP_COLORCODE="#FF0000" -e APP_TITLE="Test Title" ele44339/flask-bgcolorcode:1.0
```
Olive color and Dynamic title with command line arguments:
```bash
    -$ docker run -p 8004:8000 ele44339/flask-bgcolorcode:1.0 --colorcode="#808000" --title="Test Title"
```
