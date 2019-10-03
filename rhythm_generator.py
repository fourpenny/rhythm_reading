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
        line = file.readline().rstrip()
        count += 1

rthm_file = "resources/rhythmic_values.txt"
rhythmic_values = []
with open(rthm_file) as file:
    line = file.readline().rstrip()
    count = 1
    while line:
        rhythmic_values.append(line)
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
    new_file.write(make_measure)
    new_file.close()
    return

#define the level class and create default levels
class Level(object):
    """used to set parameters for sightreading piece with preset data or to
    save a custom preset group of parameters set by the user"""
    def __init__(self, time_signatures, note_values, pickup):
        self.signatures = time_signatures
        self.rhythms = note_values
        self.pickup = pickup
        self.name = None
        return
    def get_signatures(self):
        return self.signatures
    def get_rhythms(self):
        return self.rhythms
    def get_pickup(self):
        return self.pickup
    def set_name(self, name):
        self.name = name
        return
    def __str__(self):
        return "Level " + str(self.name) + " has the time signatures: " + str(self.signatures) + " and will have the rhythms: " + str(self.rhythms)

default_levels = []
level_counter = 0
while level_counter <= 4:
    lvl_time_sig = []
    for signatures in time_signatures:
        if time_signatures.index(signatures) <= level_counter:
            lvl_time_sig.append(signatures.split())
    lvl_note_values = []
    for rhythms in rhythmic_values:
        if rhythmic_values.index(rhythms) <= level_counter:
            lvl_note_values.append(rhythms.split())
    if level_counter < 2:
        lvl_pick_up = False
    else:
        lvl_pick_up = True
    level_to_add = Level(lvl_time_sig, lvl_note_values, lvl_pick_up)
    level_to_add.set_name(level_counter)
    default_levels.append(level_to_add)
    #for level in default_levels:
    #    print(level)
    level_counter += 1

#sets chosen time signature for sightreading and rhythms available for use
def set_time_sig(level):
    pick_group = level.get_signatures()
    if len(pick_group) > 1:
        pick_sig = pick_group[random.randrange(len(pick_group)-1)]
    else:
        pick_sig = pick_group[0]
        return pick_sig[random.randrange(len(pick_sig)-1)]

time_sig = set_time_sig(default_levels[0])

#make a measure using given parameters
def make_measure(ts, rhythms):
    split_sig = ts.split("/")
    beat = int(split_sig[0])
    beat_note = int(split_sig[1])
    notes_in_meas = []
    beat_total = 0
    while beat_total < beat:
        picker_1 = random.randrange(len(rhythms)- 1)
        picker_2 = random.randrange(len(rhythms[picker_1]) - 1)
        to_add = rhythms[picker_1][picker_2]
        notes_in_meas.append(to_add)
        print(to_add)
        if "/" in to_add:
            make_decimal = to_add.split("/")
            reciprocal = int(make_decimal[1])/int(make_decimal[0])
        else:
            reciprocal = 1/int(to_add)
        beat_total += reciprocal
        print(beat_total)
    return notes_in_meas

#the generator itself

def generate_score(level):
    return

print(make_measure(time_sig, default_levels[3].get_rhythms()))
#generate_score()
#make_lilypond("test")
lp_template.close()
