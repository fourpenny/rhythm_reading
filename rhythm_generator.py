import random

#stuff needed to write a new lilypond file as the output
file_name = "lilypond-test-" + (str(random.randrange(0, 1000, 1)) + ".ly")
print(file_name)

lp_template = open("resources/lilypond_template.txt", "r")
template_text = lp_template.read()

def make_lilypond(notes):
    """writes the given notes to a new lilypond file with a random name"""
    global file_name
    global template_text
    new_file = open(file_name, "w+")
    new_file.write(template_text)
    new_file.close()
    return

#this actually figures out what notes to put

class Level(object):
    def __init__(time_signatures, note_values, pickup)

make_lilypond("test")
