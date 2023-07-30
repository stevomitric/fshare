import argparse

from fshare.main import app, fileManager

def main():
    parser = argparse.ArgumentParser(description="Starts the python file-sharing service application")
    parser.add_argument("--bind", "-b", type=str, default="0.0.0.0", help="The local address to bind the server")
    parser.add_argument("--port", "-p", type=int, default=8000, help="File server port to run on")
    parser.add_argument("--location", "-l", type=str, default="", help="The path to the folder where files will be stored (default: /tmp/fshare)")
    args = vars(parser.parse_args())

    if ("location" in args and args["location"]):
        fileManager.changeLocation(args["location"])
    app.run(debug=False, host = args["bind"], port=args["port"] )