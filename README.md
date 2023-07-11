# Groningen Apartment Hunter Bot

This Python bot helps you find your perfect apartment in Groningen. It continuously checks various apartment rental websites, looking for new listings that match your preferences. Whenever it finds a potential match, the bot sends a notification to your Telegram account.

## Features

- Monitors several apartment rental websites, including Pararius, Kamernet, 123Wonen, and more.
- Periodically refreshes the pages to find new listings.
- Sends Telegram notifications for new apartments that match your preferences.
- Uses threading for efficient resource usage, with one thread running the Telegram bot and another managing the apartment hunting process.

## Usage

Firstly, install the necessary dependencies. This project uses Selenium for website interactions, so ensure you have the correct webdriver installed for your system.

Next, set up your Telegram bot and obtain the bot token and your chat ID. These should be set as environment variables (`BOT_TOKEN` and `CHAT_ID` respectively) before running the bot. 

Finally, run the bot. The Telegram bot will keep running and listening for commands, while the apartment hunters work in the background.

Please refer to the Python scripts for more detailed information on the setup and operations of the hunters and the bot.

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for the full text.
