from chatterbot import ChatBot


bot = ChatBot(
    "Tiberius",
    io_adapters=[
        "chatterbot_voice.Voice"
    ]
)

bot.train("chatterbot.corpus.english")

user_input = ""

while True:
    try:
        user_input = bot.get_input()
        bot_input = bot.get_response(user_input)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
