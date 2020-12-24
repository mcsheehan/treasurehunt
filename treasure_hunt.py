from cmd import Cmd
import codecs
from termcolor import colored
import colorama
colorama.init()
number_of_letters = 4 + 3 + 3

list_of_locations = ["Apurv",
                     "Hannes",
                     "Divia",
                     "Lee",
                     "Srijan",
                     "Hao",
                     "Darkroom",
                     "Christmas",
                     "Jingle bells",
                     "Have a lovely break"]

class RiddlesAndAnswers:
    def __init__(self, riddle, answer):
        self.riddle = riddle
        self.answer = answer


list_of_riddle_and_answers = [RiddlesAndAnswers("2 squared", "4"),
                              RiddlesAndAnswers("What gets wetter the more it dries?", "towel"),
                              RiddlesAndAnswers("decode : " + codecs.encode("mark", 'rot_13'), "mark"),
                              RiddlesAndAnswers("What is greater than god?\n"
                                                "More evil than the devil!\n"
                                                "The poor have it!\n"
                                                "The rich need it, and if you eat it you die", "nothing"),
                              RiddlesAndAnswers(codecs.encode("how do you cook a chicken","rot_13"), "how do you cook a chicken"),
                              RiddlesAndAnswers("What is between two e's and contains a letter", "envelope"),
                              RiddlesAndAnswers("37 - 23 + 7 * 5", "49"),
                              RiddlesAndAnswers("What has a head and a tail, but no body?", "coin"),
                              RiddlesAndAnswers("decode : " + codecs.encode("happy christmas", 'rot_13'), "happy christmas"),
                              RiddlesAndAnswers("What has hands, but cannot clap?", "clock"),
                              ]
#                              RiddlesAndAnswers("I'm tall when I'm young and short when I'm old. What am I?", "candle")


class MyPrompt(Cmd):
    current_location_printed = 0

    prompt = '> '

    intro = "Welcome to the Sheehan Christmas treasure hunt\n" \
            "Type the answer into the prompt and if you get it right you'll " \
            "get the location of the first treasure\n" \
            "Don't use articles. For example instead of \"a banana\" just enter \"banana\"\n" \
            "Your first riddle is : {}\n" \
            "Type help for a list of commands and to get your first riddle" .format(list_of_riddle_and_answers[0].riddle)

    def do_riddle(self, line):
        '''Repeats the last riddle'''
        self.print_current_riddle()

    def print_current_riddle(self):
        print(colored("Your new riddle is:",
                      'green', 'on_red'))
        print("{}".format(list_of_riddle_and_answers[self.current_location_printed].riddle))


    def last_succesful_answer(self):
        print("You got all the puzzles right. You have achieved peak holiday happiness")
        print("TREASURE HUNT COMPLETE!!!")

    def sucessful_answer(self):
        print(colored("HOORAY !!!! You got it right !!!! GREAT SUCCESS!!!", 'green', 'on_red'))
        print("Your next holiday happiness result is : {}".format(list_of_locations[self.current_location_printed]))

        self.current_location_printed += 1

        if self.current_location_printed >= len(list_of_riddle_and_answers):
            self.last_succesful_answer()
            return

        self.print_current_riddle()

    def default(self, line):
        if line == list_of_riddle_and_answers[self.current_location_printed].answer:
            self.sucessful_answer()

    # def do_exit(self, inp):
    #     '''Exit the application'''
    #     print("Bye")
    #     return True

    def do_decode(self, inp):
        '''Decode an encrypted message. Use it by typing "decode hello" replacing the word hello with your word'''
        rot13 = codecs.encode(inp, 'rot_13')
        print("decrypted message {}".format(rot13))


MyPrompt().cmdloop()
