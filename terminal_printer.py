import tabulate
from termcolor import colored
from utils_objects import Thread
from answer import Answer


class TerminalPrinter:

    @staticmethod
    def print_query(query):
        print(colored("Searching: {}".format(query), "green"))

    @staticmethod
    def print_question(thread):
        TerminalPrinter.print_question_metadata(thread)
        print(thread.question.data)
        TerminalPrinter.print_section_separator()

    @staticmethod
    def print_question_metadata(thread: Thread):
        print(colored("Thread from {}".format(thread.url), "green"))
        TerminalPrinter.print_section_separator()
        print(colored(thread.question.title, "yellow", attrs=['bold', 'underline']))
        print(tabulate.tabulate([
            ["{}: {}".format(colored(k, 'yellow'), colored(v, "magenta", attrs=["bold"])) for k, v
             in
             thread.question.attributes.items()]], tablefmt="pretty"))

    @staticmethod
    def print_answer(answer: Answer):
        print(colored("Answer {}: ".format(answer.id+1), "yellow", attrs=["bold"]))
        print(tabulate.tabulate(
            [["{}: {}".format(colored(k, 'yellow'), colored(v, "magenta", attrs=["bold"])) for k, v
              in
              answer.attributes.items()]], tablefmt="pretty"))
        print(answer.data)
        TerminalPrinter.print_answers_separator()

    @staticmethod
    def print_section_separator():
        print(colored("*" * 100, "yellow", attrs=["bold"]))

    @staticmethod
    def print_answers_separator():
        print(colored("*" * 100, "grey", attrs=["bold"]))

    @staticmethod
    def print_help_menu():
        print("{} - next answer in thread".format(colored("na", "green")))
        print("{} - next thread".format(colored("n", "green")))
        print("{} - open Google in browser".format(colored("g", "green")))
        print("{} - open current thread in browser".format(colored("o", "green")))
        print("{} - show searched command".format(colored("cmd", "green")))
        print("{} - show searched error".format(colored("err", "green")))
        print("{} - edit query".format(colored("e", "green")))
        print("{} - exit".format(colored("x", "green")))