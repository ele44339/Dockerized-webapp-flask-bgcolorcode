from flask import Flask, render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

# Get color from Environment variable
COLORCODE_FROM_ENV = os.environ.get('APP_COLORCODE')
# Set default color as royal blue
COLOR = "#4169E1"
# Get dynamic title from Environment variable
TITLE_FROM_ENV = os.environ.get('APP_TITLE')
# Set default title
TITLE = "Cloud Computing - University of West Attica"

@app.route("/")
def main():
    # return 'Hello'
    return render_template('index.html', name=socket.gethostname(), color=COLOR, colorname=COLOR, title=TITLE)


if __name__ == "__main__":
    print("This is a simple flask webapp that displays a colored background and a greeting message. \n"
          "The color can be specified in two different ways: \n"
          "    1. As a command line argument with --colorcode as the argument. \n"
          "    2. As an Environment variable APP_COLORCODE. \n"
          "In any other case, the default color is set to pink. \n"
          "\n"
          "Note 2: Command line argument precedes over environment variable.\n"
          "\n"
          "")


    # Check for Command Line Parameters for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--colorcode', required=False)
    # Check for Command Line Parameters for title
    parser.add_argument('--title', required=False)
    args = parser.parse_args()

    if args.colorcode:
        print("Color from command line argument =" + args.colorcode)
        COLOR = args.colorcode
        if COLORCODE_FROM_ENV:
            print("A color was set through environment variable -" + COLORCODE_FROM_ENV + ". However, color from command line argument takes precendence.")
    elif COLORCODE_FROM_ENV:
        print("No Command line argument. Color from environment variable =" + COLORCODE_FROM_ENV)
        COLOR = COLORCODE_FROM_ENV
    else:
        print("No command line argument or environment variable. Setting default color =" + COLOR)

    if args.title:
        print("Title from command line argument =" + args.title)
        TITLE = args.title
        if TITLE_FROM_ENV:
            print("A title was set through environment variable -" + TITLE_FROM_ENV + ". However, title from command line argument takes precendence.")
    elif TITLE_FROM_ENV:
        print("No Command line argument. Title from environment variable =" + TITLE_FROM_ENV)
        TITLE = TITLE_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a default title =" + TITLE)


    # Run Flask Application
    app.run(host="0.0.0.0", port=8000)
