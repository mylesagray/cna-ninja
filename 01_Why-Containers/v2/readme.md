
# App v2

Feel free to look at the files as they are well annotated.

This section contains an [`app.py`](src/app.py) file that will accept an input argument and output the argument encoded as a QR Code.

It also contains a [`Dockerfile`](Dockerfile) to build a container for our app and allows it to be executed.

* To build the container: `docker build -t qrcodegenerator .`
* To run the container `docker run qrcodegenerator [YOUR TEXT HERE]`
* To run and output the file to local filesystem: `docker run -v ~/qrcodes:/app/output qrcodegenerator [YOUR TEXT HERE]`

The QR Code will be in your `~/qrcodes` directory on your local machine.