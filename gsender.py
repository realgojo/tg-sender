import json
import sys
from telegram import Bot
from telegram.error import TelegramError
import os

CONFIG_FILE_PATH = "config.json"

def save_config(config):
    with open(CONFIG_FILE_PATH, "w") as config_file:
        json.dump(config, config_file)

def load_config():
    try:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        return None

async def handle_command(args, config):
    if args[0] == "last":
        if len(args) > 1 and args[1] in {"yes", "y"}:
            await send_last_file(config)
        else:
            await ask_file_repeated(config)
    elif args[0] == "help":
        print_help()
    else:
        print("Invalid command. Use 'gsender help' to see available commands.")

async def ask_file_repeated(config):
    answer = input("Is the previous file repeated? (yes/no): ").lower()
    if answer in {"yes", "y"}:
        await send_last_file(config)
    else:
        await send_new_file(config)

async def send_last_file(config):
    if not config:
        print("No previous configuration found. Please provide token, chat ID, and file path.")
        return

    bot = Bot(token=config["bot_token"])
    try:
        with open(config["last_file_path"], 'rb') as file:
            await bot.send_document(chat_id=config["chat_id"], document=file)
        print(f"File '{config['last_file_path']}' has been sent to chat ID {config['chat_id']}.")
    except TelegramError as e:
        print(f"Failed to send the file: {str(e)}")

async def send_new_file(config):
    bot_token = config["bot_token"]
    chat_id = config["chat_id"]
    file_path = input("Please enter the path to the new file you want to send: ")

    try:
        with open(file_path, 'rb') as file:
            bot = Bot(token=bot_token)
            await bot.send_document(chat_id=chat_id, document=file)
        print(f"New file '{file_path}' has been sent to chat ID {chat_id}.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except TelegramError as e:
        print(f"Failed to send the file: {str(e)}")

def print_help():
    print("Usage:")
    print("  gsender <bot_token> <chat_id> <file_path>   Send file via Telegram")
    print("  gsender last               Send last file using last configuration")
    print("  gsender help               Show this help message")

async def main():
    config = load_config()

    if len(sys.argv) >= 2:
        await handle_command(sys.argv[1:], config)
    else:
        # Interactive mode
        bot_token = input("Please enter your bot token: ")
        chat_id = input("Please enter your numeric Telegram user ID: ")
        file_path = input("Please enter the path to the file you want to send: ")

        # Validate chat_id is an integer
        try:
            chat_id = int(chat_id)
        except ValueError:
            print("Chat ID must be a number.")
            return

        config = {
            "bot_token": bot_token,
            "chat_id": chat_id,
            "last_file_path": file_path
        }
        save_config(config)

        await send_last_file(config)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
