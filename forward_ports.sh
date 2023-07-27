#!/bin/bash
sudo apt update;
sudo apt install ufw;
sudo ufw enable;
sudo ufw allow 80;
sudo ufw allow 443;