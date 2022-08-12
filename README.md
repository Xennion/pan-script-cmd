# PAN click command to run a script on a pan/panorama device

## Usage

```bash
# get help
❯ python pan.py -h
Usage: pan.py [OPTIONS] HOST FILE

  Sends a config FILE to a pan-os HOST with netmiko

  HOST is the hostname or IP address of the device
  FILE is the path to the config file to send

Options:
  -h, --help           Show this message and exit.
  -u, --username TEXT
  -p, --password TEXT

# run the cmd with the example input file
python pan.py sjpanorama01.tivo.com commands-example.txt
Username: mygooduser
Password: mygooderpass
```