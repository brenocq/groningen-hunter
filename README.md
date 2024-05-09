# Groningen Apartment Hunter Bot

This Python bot helps you find your perfect apartment in Groningen. It continuously checks various apartment rental websites, looking for new listings that match your preferences. Whenever it finds a potential match, the bot sends a notification to your Telegram account. (Yes I did find the place I'm living today using this bot 😜)

<p align="center">
  <img src="https://github.com/brenocq/groningen-hunter/assets/17342434/6a83c8bc-a704-4d02-be39-b0df89974cc3">
</p>

## Features

- Monitors several apartment rental websites, including Pararius, Kamernet, 123Wonen, and more.
- Periodically refreshes the pages to find new listings.
- Sends Telegram notifications for new apartments that match your preferences.
- Uses threading for efficient resource usage, with one thread running the Telegram bot and another managing the apartment-hunting process.

## Getting the bot to work

### Create a Telegram bot
On Telegram, search for "BotFather"
Send him the message
```
/newbot
```
Follow the BotFather steps!

When you are done, he should tell you the HTTP API token, we'll need this later.

### Windows setup
We will install the Windows Subsystem for Linux. Open the "Command Prompt" (you can seach cmd on Windows search bar) and run the following command:

```
wsl --install
```

Open the Ubuntu program. I got some Firefox errors on my WSL, I followed the steps [here](https://askubuntu.com/questions/1444962/how-do-i-install-firefox-in-wsl-when-it-requires-snap-but-snap-doesnt-work) to solve it.


You can now follow the Ubuntu setup.

### Ubuntu setup
Run the following commands
```
sudo add-apt-repository ppa:mozillateam/ppa
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git python3 python3-pip firefox
git clone https://github.com/brenocq/groningen-hunter.git
cd groningen-hunter
pip install -r requirements.txt
```

### Arch setup
Run the following commands
```
sudo pacman -Sy firefox geckodriver
git clone https://github.com/brenocq/groningen-hunter.git
cd groningen-hunter
pip install -r requirements.txt
```

### Running the bot
Before running the bot we need to set the BOT API TOKEN, create a file `.env` with the the bot token. You can also set the chat ID, minimum price, and maximum price you are looking for.

```
touch src/.env
```

The file should look like this:
```
BOT_TOKEN="YOUR-BOT-HTTP-API-TOKEN"
CHAT_ID="YOUR-CHAT_ID"
MAXIMUM_PRICE=1000
MINIMUM_PRICE=300
```

Let's run the bot to test if it is working:

```
cd src
python3 main.py
```

The bot is now running, but we need to get the Chat ID to be able to receive the apartment notifications. Send the following message to your bot on Telegram:

```
/chatid
```

The bot should answer you with the Chat ID, set the Chat ID on the `.env` file and run the bot again

```
python3 main.py
```

If you implement new hunters or develop new features, please create a PR. If you find any bugs, please open a new issue. All help is welcome ;)

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for the full text.
