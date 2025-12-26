import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.tapdance import TapDance
from kmk.extensions.rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

tapdance = TapDance()
keyboard.modules.append(tapdance)

rgb = RGB(
    pixel_pin=board.TX,
    num_pixels=4,
    val_limit=150,
    animation_mode=AnimationModes.RAINBOW,
    animation_speed=1,
)
keyboard.extensions.append(rgb)

PINS = [board.A0, board.A1, board.A2, board.A3, board.D4, board.D5]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
    pull=True
)

MUTE_MEDIA = KC.TD(KC.AUDIO_MUTE, KC.MEDIA_PLAY_PAUSE)

keyboard.keymap = [
    [
        KC.AUDIO_VOL_UP,
        KC.AUDIO_VOL_DOWN,
        MUTE_MEDIA,
        KC.LALT(KC.TAB),
        KC.LWIN(KC.LCTL(KC.LEFT)),
        KC.LWIN(KC.LCTL(KC.RIGHT)),
    ]
]

if __name__ == "__main__":
    keyboard.go()
