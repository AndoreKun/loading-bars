# -------------------------------------------------- Progress Bar ---------------------------------------------------- #

def progress_bar(current_percentage, total=100, bar_size=30):
    """
    Function generates simple progress bar. To update the bar, just call the function again with the new one
    percentage you want, it will erase the last bar and create a new one with the new percentage

    :param int current_percentage: Desired percentage the user wants the bar to print
    :param int total: Total percentage, can be higher than 100%, values will adjust for that
    :param int bar_size: Size(number of substrings) the bar will have in total
    """
    # The percentage is equal to the percentage of the current_percentage multiplied by 100 and then divided by
    # the total percentage defined by the user e.g.: (80 * 100) / 100 = 80; (80 * 100) / 200 = 40
    # This way, the user can define a value greater than 100% for the bar
    percentage = int(float(current_percentage) * 100 / total)
    # The arrows are multiplied by the percentage (e.g. 80), which are divided by one hundred (0.8) and multiplied
    # by the size of the bar minus one (23). This result will show how much of the bar will be filled
    arrows = "=" * int(percentage / 100 * bar_size - 1) + ">"
    # Spaces are the size of the bar minus the total number of arrows (30-23 = 7)
    spaces = " " * (bar_size - len(arrows))
    # The print of this will start cleaning the previous bar, then it will start with arrows, followed by spaces
    # with the percentage at the end
    print("\rProgress: [{0}{1}] {2} %".format(arrows, spaces, percentage), end="", flush=True)


# --------------------------------------------------- Dinamic Bar ---------------------------------------------------- #


def dinamic_bar(total_percentage=100, stop_at="", messages="", time=1200, final_message="Done!"):
    """
    Function generates a dynamic progress bar that can print messages in certain percentages

    :param int total_percentage: Total percentage, can be higher than 100%, values will adjust for that
    :param list stop_at: If set, in a certain percentage the function will print something (E.g. [25, 50])
    :param list messages: List with messages you want to print, number of elements must equal to parameter stop_at
    :param int time: Time the bar will take to complete 100% (1200 is approximately 3s)
    :param str final_message: Message that will be shown after the bar reaches 100%
    :author André Pereira:
    """
    posicao_mensagem = 0
    numero_mensagens = len(stop_at)
    # adds 1 since last number wouldn't be counted otherwise
    for p in range(total_percentage + 1):
        # Creates time and prints the bar
        for t in range(time):
            progress_bar(p, 100)
        if stop_at:
            try:
                if p == stop_at[posicao_mensagem]:
                    print("\r" + messages[posicao_mensagem])
                    # Adds 1 to message position until it equals the number of elements in stop
                    if posicao_mensagem != numero_mensagens:
                        posicao_mensagem += 1
            except IndexError:
                continue
    print("\n" + final_message)

# --------------------------------------------------- loading bar ---------------------------------------------------- #


def loading_info(info="Loading", dot_type=".", number_dots=3, info_type="info", dot_speed=1):
    """
    Function prints a dot after a text every x seconds (E.g. Loading ...)

    :param str info: Information to be printed
    :param str dot_type: Type of symbol to be printed (E.g. '.' , '-', etc), they will appear after info
    :param int number_dots: Number of dots, increasing this will obviously increase loading time
    :param str info_type: Type of info (E.g. '[info]', '[error]', '[warning]') this will appear before info, can be none
    :param float dot_speed: Speed at which points will appear, must be greater than zero, but may be less than 1
    """
    if info_type:
        info_type = "[{}]".format(info_type.upper())
    for loading in range(number_dots + 1):
        print("\r{0} {1}".format(info_type, info) + dot_type * loading, end="")
        # Creates time by adding 1 to t
        for t in range(int(5000000 * dot_speed)):
            t += 1
    print("\n")

