#basic stuff needed to import from other files
import random

lp_template = open("resources/lilypond_template.txt", "r")
template_text = lp_template.read()

ts_file = "resources/time_signatures.txt"
time_signatures = []
with open(ts_file) as file:
    line = file.readline().rstrip()
    count = 1
    while line:
        time_signatures.append(line)
        print(time_signatures)
        line = file.readline().rstrip()
        count += 1

rthm_file = "resources/rhythmic_values.txt"
rhythmic_values = []
with open(rthm_file) as file:
    line = file.readline().rstrip()
    count = 1
    while line:
        rhythmic_values.append(line)
        print(rhythmic_values)
        line = file.readline().rstrip()
        count += 1

#stuff needed to write a new lilypond file as the output
file_name = "lilypond-test-" + (str(random.randrange(0, 1000, 1)) + ".ly")
print(file_name)

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
    """used to set parameters for sightreading piece with preset data or to
    save a custom preset group of parameters set by the user"""
    def __init__(time_signatures, note_values, pickup):
        self.signatures = time_signatures
        self.rhythms = note_values
        self.pickup = pickup
        return
    def get_signatures(self):
        return self.signatures
    def get_rhythms(self):
        return self.rhythms
    def get_pickup(self):
        return self.pickup

"""level_counter = 1
while level_counter < 5:
    lvl_time_sig = 0
    lvl_note_values = 0
    lvl_pick_up = 0
    level_to_add = Level(lvl_time_sig, lvl_note_values, lvl_pick_up)
    level_counter += 1"""

#make_lilypond("test")
lp_template.close()
