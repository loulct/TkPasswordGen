# TkPasswordGen

## Install Dependency

sudo pacman -S tk

## Run

uv run tkpasswordgen

## Build

uv run pyinstaller --onefile --windowed src/tkpasswordgen/__main__.py --name PasswordGen 
