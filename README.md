# Re4u bot

This is a simple Python program that monitors the USD/BRL forex rate and sends an event to a [Nostr](https://nostr.io) network node when the rate changes. The program runs in a loop, checking the forex rate every hour between 10am and 6pm GMT-3.
## Prerequisites

To run this program, you'll need the following:

- Python 3.9 or higher
- The following Python packages: `cachetools`, `pytz`, `requests`, `nostr`

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

<li>Edit the config.py file and replace KEY with your Nostr private key.</li>
</ol>

## Usage

To run the program, run the following command:

```bash
└─$ python main.py
```

The program will start monitoring the forex rate and sending events to the Nostr network when the rate changes.

## License

This project is licensed under the [WTFPL License](http://www.wtfpl.net/). See the `LICENSE` file for more information.

## Acknowledgments

This program uses the [AwesomeAPI](https://github.com/public-apis/public-apis#currency-exchange) to retrieve the USD/BRL forex rate.