# Mac

## Install Python 3

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
```

## Fix pip3 install <module> -t option
```bash
cp ./.pydistutils.cfg ~/.pydistutils.cfg
```

## Install MyQR

```bash
pip3 install myqr --user
pip3 install pyqrcode --user
```

## Generate QR Code

```bash
python3 ./generate_qr.py 
```
