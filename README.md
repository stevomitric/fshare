
# File Share - Local File Sharing Service

fshare is a Python package that serves as a file sharing service over a local network. It utilizes Flask to create a local server on port 8000, allowing users to upload files and share them within the network.

## Installation

To install fshare, use pip:

```bash
pip install fshare
```

All of the required dependencies (`flask >= 1.0.0`) will be installed automatically by pip.

## Running the Service

To start the file-sharing service, run the following command:

```bash
python -m fshare
```

You're all set! Servers is up and running on http://localhost:8000


Default save-location is the temp directory (`/tmp/fshare` on unix like systems or `%tmp%/fshare` on windows)

## Command-Line Options

fshare supports the following command-line options:

```plaintext
usage: python -m fshare [-h] [--bind BIND] [--port PORT] [--location LOCATION]

Starts the python file-sharing service application

options:
  -h, --help            show this help message and exit
  --bind BIND, -b BIND  The local address to bind the server
  --port PORT, -p PORT  File server port to run on
  --location LOCATION, -l LOCATION
                        The path to the folder where files will be stored
                        (default: /tmp/fshare)
```

### Options

- `-h`, `--help`: Displays the help message and exits.
- `--bind BIND`, `-b BIND`: Sets the local address to bind the server (optional).
- `--port PORT`, `-p PORT`: Specifies the file server port to run on (optional).
- `--location LOCATION`, `-l LOCATION`: Sets the path to the folder where files will be stored. By default, files are stored in `/tmp/fshare`.

## Example Usage

Here's an example of running fshare with custom options:

```bash
python -m fshare --port 8080 --location /path/to/custom/folder
```

This will start the file-sharing service on port 8080 and use `/path/to/custom/folder` as the file storage location.

## Running programatically

Fshare can be imported in your project alongside with a reference to the `FileManager` class and the `flask` app.

```python
from fshare.main import app, fileManager

# change the save-location path
# fileManager.changeLocation('/new/location/path')

app.run(host='0.0.0.0', port=8000, debug=True)

```

## Contributing

We welcome contributions from the community! If you find any issues, have suggestions for improvements, or want to add new features, please feel free to open an issue or submit a pull request on our GitHub repository.

## License

fshare is open-source software released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Issues

For any issues or feedback, please visit the [Bug Tracker](https://github.com/stevomitric/fshare/issues) on GitHub.

## Contact

For questions or inquiries, you can reach out to Stevo Mitric at stevomitric2000@gmail.com.

## Disclaimer

File-Share is provided "as is" without warranty of any kind, express or implied. Use it at your own risk. The authors of File-Share are not responsible for any damages or liabilities resulting from the use of this package.

## Acknowledgments

- fshare is built with the help of Flask and other open-source libraries.
- Special thanks to the Python community for their continuous support.
