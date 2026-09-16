# TkPasswordGen

## Releases



## Install Dependencies

Install [uv](https://docs.astral.sh/uv/#installation).

Then run the command below to read the lockfile, create the virtual environment and install required dependencies.
```
uv sync
```

Install Tkinter as it requires OS-level compilatiion and system packages.

ex: `sudo pacman -S tk`

Run program using the command below.
```
uv run tkpasswordgen
```

## Build

```
uv run pyinstaller --onedir --windowed src/tkpasswordgen/__main__.py --name PasswordGen 
mkdir -p PasswordGen.AppDir/usr/bin
cp -r ./dist/PasswordGen/* ./PasswordGen.AppDir/usr/bin/
```

Add an icon `passwordgen.svg` file of your choosing at `./PasswordGen.AppDir`.

Create `.AppImage` using [appimagetool](https://github.com/AppImage/appimagetool/releases/tag/continuous).
```
./appimagetool-x86_64.AppImage PasswordGen.AppDir
```
