# jdy_webhook_print


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Architecture](#architecture)
  * [Files Structure](#files-structure)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Run app](#run-app)
  * [Set jdy](#set-jdy)
  * [Receive data](#receive-data)
* [To-Do](#To-Do)
* [License](#license)

<!-- ABOUT THE PROJECT -->
## About the Project
Print data from '简道云' api and webhook, to help you understand the data structure you have got from '简道云'. There are two mainly data source:
- [API](https://hc.jiandaoyun.com/open/10992)(waitting for a further update...)
- [webhook](https://hc.jiandaoyun.com/open/11500)

Project Characteristic:

- Docker-based Deployment
- Flask

### Architecture
* Ubuntu 20.04 : Operating System
* Python 3.6+ : Language
* Flask 1.1.2+: third-party library to serve the application
* Pygments: third-party library to colorful output json

### Files Structure
```
.
├── app.py
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── README.md
├── receive_data.png
├── requirements.txt
└── set_jdy.png

0 directories, 8 files
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Markdown                         1             22              0             92
Python                           1              7              6             48
Dockerfile                       1              5              7             21
YAML                             1              1              3             12
-------------------------------------------------------------------------------
SUM:                             4             35             16            173
-------------------------------------------------------------------------------
```

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
- 64bit Linux like Ubuntu, CentOS etc.
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [docker-compose](https://docs.docker.com/compose/install/)

### Installation

1. ssh to remote server if local pass this step
```sh
>>> ssh xx@xx.xx.xx.xx
```
2. Clone the repo
```sh
>>> git clone https://github.com/MacwinWin/jdy_data_print.git
```
3. up services
```sh
>>> docker-compose up -d
```

<!-- USAGE EXAMPLES -->
## Usage
### run app
```sh
# enter the container
>>> docker exec -it jdy_data_print_1.0 /bin/bash
# run app(defult host is 0.0.0.0, port is 3101, development environment is open)
>>> flask run
```

### set jdy

- xx.xx.xx.xx is your host ip
- Default port is 3101, you can modify it
- Default secret is 'test', you can modify it
- All push time is supported

<p align="center">
    <img src="set_jdy.png">

### receive data
Formatted and colorful json print
<p align="center">
    <img src="receive_data.png">

## To-Do
- Support API data

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.