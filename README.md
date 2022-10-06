# Gotify-GPG-Extractor

## What does it do??? :boom:

This program connects to your Gotify instance, filters all of the messages in an Application for GPG-Files, downloads them AND DELETES THEM

## Prerequisites

1. Gotify Server
2. Application on Gotify Server
3. Client on Gotify Server
4. Docker / Python on Host

## Limitations

- Can only search one Application at a time
- Only supports Client-Access
- Only interprets "Files" starting with `-----BEGIN PGP MESSAGE-----`
- No toggle for keeping messages


## Build

`docker build -t gotify-gpg-extractor:1 .`

## Run

Docker:

`docker run -d --rm -e GOTIFY_URL=<your_gotify_url_without_/> -e GOTIFY_APP_ID=<your_app_id> -e GOTIFY_KEY=<your_client_key> -v c/Users/Unrea1/Desktop/out/:/home/gotify/output/ gotify-gpg-extractor:1`

example:

`docker run -d --rm -e GOTIFY_URL=http://192.168.1.53:8071 -e GOTIFY_APP_ID=3 -e GOTIFY_KEY=CCFCu7Rhen4gVAF -v c/Users/Unrea1/Desktop/out/:/home/gotify/output/ gotify-gpg-extractor:1`

---

Python:
`python src/receive.py`
:exclamation:(must set env variables first) & (must install requirements)

## How to send a File with Gotify-CLI

1. `gotify init`
2. `gotify push < file.gpg` 
