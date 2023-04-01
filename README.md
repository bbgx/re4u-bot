# Re4u bot
<!-- empty table header -->
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=bbgx_re4u-bot&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=bbgx_re4u-bot) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=bbgx_re4u-bot&metric=coverage)](https://sonarcloud.io/summary/new_code?id=bbgx_re4u-bot) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=bbgx_re4u-bot&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=bbgx_re4u-bot)
</br>
This is a simple Python program that monitors the USD/BRL forex rate and sends an event to a [Nostr](https://nostr.io) network node when the rate changes. The program runs in a loop, checking the forex rate every hour between 10am and 6pm GMT-3.
## Features
- Retrieves the USD to BRL exchange rate periodically
- Compares the current rate with the previous rate
- Sends updates to a Relay Manager when the rate changes
- Schedules tasks to run during business hours and on weekdays

## Installation
<ol>
<li>Clone the repository:</li>

```bash
└─$ git clone https://github.com/bbgx/re4u-bot.git
└─$ cd re4u-bot
````
<li>Install the required Python packages:</li>

```bash
└─$ pip install -r requirements.txt
```

<li>Create a .env file in the root of the project and add the required environment variables:</li>

```bash
PRIVATE_KEY=your_private_key_here
BASE_URL=api_url_here
```
</ol>

## Usage

To run the program, run the following command:

```bash
└─$ python main.py
```
The program will start monitoring the forex rate and sending events to the Nostr network when the rate changes.

## Testing
To run the unit tests, execute the following command:
```bash
└─$ python -m unittest tests/*.py
```


## License

This project is licensed under the [WTFPL License](http://www.wtfpl.net/). See the `LICENSE` file for more information.

## Acknowledgments

This program uses the [AwesomeAPI](https://github.com/public-apis/public-apis#currency-exchange) to retrieve the USD/BRL forex rate.
