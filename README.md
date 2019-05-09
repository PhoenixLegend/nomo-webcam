

# nomo-webcam

## Intro

This is a web-based camera application using Javascript/CSS/HTML and webcam.min.js API.

Trying to mimic a very well-known application "**NOMO**" both in android and IOS platform.

![filter](C:\Users\陈敬谊\Desktop\nomo-design\readme\filter.png)

<p align="center">Camera 135B</p>

With a built in filter "**LOMO**" using caman.full.min.js API, the filtered image will show in the next page by clicking the Thumbnail right-bottom.

![bg](C:\Users\陈敬谊\Desktop\nomo-design\readme\bg.png)

## Raspberry Pi 3 Model B+

This project is also working in Raspberry 3.5 inch LCD screen.

**Activated LCD touch screen:**

```shell
sudo tar zxvf LCD-show.tar.gz
cd LCD-show/
sudo ./LCD35-show
```

**Activated Camera:**

```shell
sudo apt-get update
sudo apt-get upgrade
sudo raspi-config
```

There's an officially supported V4L2 camera module for the RPI camera (not the same as UV4L). It needs to be loaded, so before the browser detects the camera, you should use the following command::

```shell
sudo modprobe bcm2835-v4l2
```

