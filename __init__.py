# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill
import subprocess
__author__ = 'reaperjudge'

# Creating Backtalk extending MycroftSkill
class Backtalk(MycroftSkill):
    def __init__(self):
        super(Backtalk, self).__init__(name="Backtalk")

    def initialize(self):
        # Creating GreetingsIntent requiring Greetings vocab
        greetings = IntentBuilder("GreetingsIntent"). \
            require("greetings").build()
        # Associating a callback with the Intent
        self.register_intent(greetings,
                             self.handle_shutdown)
        
    def handle_shutdown(self, message):
        # Sending a command to mycroft, speak Greetings Dialog
        subprocess.call(["sudo","shutdown","-h","now"])
        self.speak_dialog("respond")
        
    def stop(self):
        pass

def create_skill():
    return Backtalk()
