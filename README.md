# Discord.py Example Tutorial Bot

Welcome to the Discord.py Example Tutorial Bot! This bot is designed to help you get started with creating your own Discord bots using the Discord.py library. This README will guide you through the setup process and provide an overview of the features included in this example bot.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Features

- Basic command handling
- Event handling
- Example commands:
  - `!hello` - Responds with a greeting message
  - `!ping` - Responds with "Pong!" and the bot's latency
  - `!info` - Provides information about the server
- Error handling

## Prerequisites

- Python 3.8 or higher
- Discord.py library (version 1.7.3 or higher)
- A Discord account
- A Discord server where you have permission to add bots

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/maxiroe140/Discord-Example-Bot.git
    cd discordpy-example-tutorial-bot
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Create a new Discord application and bot:**
    - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    - Click "New Application" and give it a name.
    - Click "Bot" and under "Token", click "Copy" to copy your bot token. Keep this token secure!

2. **Set up your configuration file:**
    - Open `config.py` and replace `'YOUR_BOT_TOKEN_HERE'` with your actual bot token.

    ```python
    TOKEN = 'YOUR_BOT_TOKEN_HERE'
    ```

## Running the Bot

1. **Start the bot:**

    Console:

    ```bash
    python bot.py
    ```
    Or press the start button in youre IDE (if you using a IDE)

2. **Invite the bot to your server:**
    - Go to the "OAuth2" tab in your Discord application.
    - Under "OAuth2 URL", select "bot" and "application.commands" and the permissions your bot needs.
    - Copy the generated URL and open it in your browser.
    - Select your server and invite the bot.

## Usage

Once the bot is running and invited to your server, you can use the following commands in any text channel the bot has access to.

## Commands



## Contributing

We welcome contributions! If you have suggestions for improvements or new features, please create an issue or submit a pull request. Make sure to follow the existing code style and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using the Discord.py Example Tutorial Bot! We hope this guide has been helpful in getting you started with Discord.py. If you have any questions or run into issues, feel free to open an issue on GitHub.
