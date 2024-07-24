# File Sharing System Host

(WIP)

## How to start the Flask Server

### Setup a virtual environment (Optional)
``` cmd
python -m venv env
.\env\Scripts\activate
```

### Update pip (Optional)
``` cmd
python.exe -m pip install --upgrade pip
```

### Install the requirements
``` cmd
pip install -r requirements.txt
```
or
```
pip install flask
```

### Start the Flask Server
``` cmd
python app.py
```

## Using the FSS 

### Method 1
First you need to get the host IPv4, you can get using this command on Windows:
``` cmd
ipconfig
```
and this command on Linux and Mac:
``` bash
ifconfig
```

Look for the code after "IPv4 Address" at the main adapter, then access the URL using the IPv4 code, see the example:
```
http://255.255.0.1:2024
```

Use it in another device, such as your smartphone, but make sure that it is connected to the same wi-fi as your host device.

### Method 2
(WIP)

## Licence
This repository is currently under a [LICENCE](LICENCE)
