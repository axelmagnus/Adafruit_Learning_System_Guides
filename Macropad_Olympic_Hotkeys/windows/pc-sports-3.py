# MACROPAD Olympic Hotkeys sports page 3
# pylint: disable=line-too-long

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Sports 3', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Judo', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                            'https://olympics.com/tokyo-2020/olympic-games/en/results/judo/olympic-schedule-and-results.htm\n']),
        (0x3F3F3F, 'Karate', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                              'https://olympics.com/tokyo-2020/olympic-games/en/results/karate/olympic-schedule-and-results.htm\n']),
        (0x004000 , 'MSwim', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                              'https://olympics.com/tokyo-2020/olympic-games/en/results/marathon-swimming/olympic-schedule-and-results.htm\n']),
        # 2nd row ----------
        (0x3F3F3F, 'Pentath', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                               'https://olympics.com/tokyo-2020/olympic-games/en/results/modern-pentathlon/olympic-schedule-and-results.htm\n']),
        (0x400000, 'RGym', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                            'https://olympics.com/tokyo-2020/olympic-games/en/results/rhythmic-gymnastics/olympic-schedule-and-results.htm\n']),
        (0x3F3F3F , 'Row', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                            'https://olympics.com/tokyo-2020/olympic-games/en/results/rowing/olympic-schedule-and-results.htm\n']),
        # 3rd row ----------
        (0x400000, 'Rugby', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                             'https://olympics.com/tokyo-2020/olympic-games/en/results/rugby-sevens/olympic-schedule-and-results.htm\n']),
        (0x3F3F3F, 'Sail', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                            'https://olympics.com/tokyo-2020/olympic-games/en/results/sailing/olympic-schedule-and-results.htm\n']),
        (0x000040, 'Shoot', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                             'https://olympics.com/tokyo-2020/olympic-games/en/results/shooting/olympic-schedule-and-results.htm\n']),
        # 4th row ----------
        (0x3F3F3F, 'Skate', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                             'https://olympics.com/tokyo-2020/olympic-games/en/results/skateboarding/olympic-schedule-and-results.htm\n']),
        (0x000040, 'Climb', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                             'https://olympics.com/tokyo-2020/olympic-games/en/results/sport-climbing/olympic-schedule-and-results.htm\n']),
        (0x3F3F3F, 'Surf', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                            'https://olympics.com/tokyo-2020/olympic-games/en/results/surfing/olympic-schedule-and-results.htm \n']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
