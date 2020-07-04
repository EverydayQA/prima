

class GameDisplay:

    @staticmethod
    def prompt(text):
        input_value = input(text)
        return input_value

    @staticmethod
    def prompt2(text):
        input_value = raw_input(text)
        return input_value
