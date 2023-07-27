#!/bin/bash
sudo apt update;
sudo apt install openssl;
openssl genpkey -algorithm RSA -out key.key;
openssl req -new -key key.key -out csr.csr;
openssl x509 -req -days 365 -in csr.csr -signkey key.key -out cert.crt;
rm csr.csr;