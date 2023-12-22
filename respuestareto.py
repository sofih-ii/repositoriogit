import datetime

class Greeter:
    def __init__(self):
        pass

    def greet(self, name):
        name = name.strip()
        
        name = name.capitalize()

        current_time = datetime.datetime.now().time()

        if datetime.time(6, 0) <= current_time < datetime.time(12, 0):
            greeting = "Good morning"
        elif datetime.time(18, 0) <= current_time < datetime.time(22, 0):
            greeting = "Good evening"
        else:
            greeting = "Good night"

        final_greeting = f"{greeting} {name}"

        print(final_greeting)

        return final_greeting

greeter = Greeter()
greeter.greet("Alice")
greeter.greet("Bob")
