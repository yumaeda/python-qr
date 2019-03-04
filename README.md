# CentOS 7

## Install Prerequisites

```bash
sudo yum install gcc openssl-devel bzip2-devel
sudo yum install -y libffi-devel
```

## Download and Extract Python 3.7

```bash
sudo cd /usr/src
sudo wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
sudo tar xzf Python-3.7.2.tgz
sudo rm Python-3.7.2.tgz
```

## Install Python 3.7

```bash
cd Python-3.7.2
sudo ./configure --enable-optimizations
sudo make altinstall
```

## Execute

```bash
python3.7 generate_qr
```
