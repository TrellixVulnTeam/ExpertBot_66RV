from chatbot import *
from chatterbot.trainers import *
import json

# First, lets train our bot with some data
def CorpusTrain():
   trainer = ChatterBotCorpusTrainer(bot)

   trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
   )
   print(trainer.show_training_progress)
# Now we can export the data to a file
   trainer.export_for_training('./my_export.json')
#CorpusTrain()
