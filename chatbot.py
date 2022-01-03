from chatterbot import ChatBot

bot = ChatBot(
    'paul',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
    ],
    database_uri='sqlite:///database.sqlite3'
)
while True:
    try:
        bot_input = bot.get_response(input("You:"))
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break