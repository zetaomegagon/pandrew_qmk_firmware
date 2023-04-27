import re

prefix = "xwhatsit/" # will change to ""
ellipse = 'brand_new_model_f'
hand = '' # will change to handwired/

license = r"""/*
Copyright 2020-2023 Purdea Andrei

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
"""

configh_head = license + r"""
#pragma once

#define DEF_SERIAL_NUMBER "purdea.ro:qmk_xwhatsit"

#ifndef SERIAL_NUMBER
#define SERIAL_NUMBER DEF_SERIAL_NUMBER
#endif
"""

common_solenoid = """// We disable haptic feedbeck during USB low power conditions:
#define HAPTIC_OFF_IN_LOW_POWER 1
// You can also tune the following for your solenoid:
#define SOLENOID_DEFAULT_DWELL 20
#define SOLENOID_MIN_DWELL 4
//#define SOLENOID_MAX_DWELL 100
#define NO_HAPTIC_MOD
"""

universal_solenoid = """// By default we set up for support of xwhatsit's solenoid driver board.
// Comment out HAPTIC_ENABLE_PIN if you don't have an enable pin:
#define HAPTIC_ENABLE_PIN D3
// Change this if you are using a different pin for the solenoid:
#define SOLENOID_PIN D2
// If you are not using a solenoid then comment out the above, and also in rules.mk, remove HAPTIC_ENABLE
""" + common_solenoid

wcass_and_xwhatsit_solenoid = """// By default we set up for support of xwhatsit's solenoid driver board.
// Comment out HAPTIC_ENABLE_PIN if you don't have an enable pin:
#define HAPTIC_ENABLE_PIN B7
// Change this if you are using a different pin for the solenoid:
#define SOLENOID_PIN B6
// If you are not using a solenoid then comment out the above, and also in rules.mk, remove HAPTIC_ENABLE
""" + common_solenoid

wcass_and_xwhatsit_solenoid_restricted = """// Here we set up solenoid support, but only for custom wiring
// To make the solenoid driver work with this configuration, you must take the trigger signal
// from pin B7, which is normally the enable pin, and you can take the enable signal from pin B3,
// or you can hardwire it to Vcc.
// Comment out HAPTIC_ENABLE_PIN if you don't have an enable pin:
#define HAPTIC_ENABLE_PIN B3

// ^ Note: The B3 pin on normal classical xwhatsit/wcass controllers is a corner-pin of the atmega,
// which is not used, so it's easy to solder to for custom modifications.
// In the 33-pin version of the wcass board, this pin may be bought out to a header.

// Change this if you are using a different pin for the solenoid:
#define SOLENOID_PIN B7
// If you are not using a solenoid then comment out the above, and also in rules.mk, remove "HAPTIC_ENABLE += SOLENOID"
// You can also tune the following for your solenoid:
""" + common_solenoid

universal_normal_leds = """// If the lock lights are not used, then please don't define the below pins,
// or leave them set as unused pins:

// The following definitions are compatible with the Model F SMD controllers
// from here: https://deskthority.net/viewtopic.php?f=7&t=24597 supporting the
// AT lock lights header
#define LED_NUM_LOCK_PIN D7
#define LED_CAPS_LOCK_PIN E6
#define LED_SCROLL_LOCK_PIN B6

// The following definitions match the lock lights as used by the original
// xwhatsit firmware, but enabling all three of these is not compatible with
// solenoid support
//#define LED_NUM_LOCK_PIN E6
//#define LED_CAPS_LOCK_PIN D2
//#define LED_SCROLL_LOCK_PIN D7

// Uncomment below if the leds are on when the pin is driving zero:
//#define LED_NUM_LOCK_ACTIVE_LOW
//#define LED_CAPS_LOCK_ACTIVE_LOW
//#define LED_SCROLL_LOCK_ACTIVE_LOW
"""

universal_b_exp_leds = """// If the lock lights are not used, then please don't define the below pins,
// or leave them set as unused pins:

#define LED_NUM_LOCK_PIN F5
#define LED_CAPS_LOCK_PIN B4
#define LED_SCROLL_LOCK_PIN B5
#define LED_NON_BASE_LAYER_PIN E6

#define HAPTIC_ENABLE_STATUS_LED D7

// The following definitions match the lock lights as used by the original
// xwhatsit firmware, but enabling all three of these is not compatible with
// solenoid support
//#define LED_NUM_LOCK_PIN E6
//#define LED_CAPS_LOCK_PIN D2
//#define LED_SCROLL_LOCK_PIN D7

// Uncomment below if the leds are on when the pin is driving zero:
#define LED_NUM_LOCK_ACTIVE_LOW
#define LED_CAPS_LOCK_ACTIVE_LOW
#define LED_SCROLL_LOCK_ACTIVE_LOW
#define LED_NON_BASE_LAYER_ACTIVE_LOW

#define HAPTIC_ENABLE_STATUS_LED_ACTIVE_LOW

#define MATRIX_EXTRA_DIRECT_ROWS 1
#define MATRIX_EXTRA_DIRECT_COLS 3

#define MATRIX_EXTRA_DIRECT_PINS_ACTIVE_LOW 1
#define MATRIX_EXTRA_DIRECT_PINS_NEED_INTERNAL_PULLUP 1
#define MATRIX_EXTRA_DIRECT_PINS { { B6, B3, F4 } }
"""

wcass_and_xwhatsit_normal_leds = """// If the lock lights are not used, then please don't define the below pins,
// or leave them set as unused pins:

// The following definitions match the lock lights as used by the original
// xwhatsit firmware, but enabling all three of these is not compatible with
// standard solenoid support, because B6 and B7 pins are already in use:
//#define LED_NUM_LOCK_PIN B5
//#define LED_CAPS_LOCK_PIN B6
//#define LED_SCROLL_LOCK_PIN B4
// Since solenoid support is enabled by default, the above lock light pin
// assignments are disabled by default.
// Instead the more common Num Lock and Caps Lock are assigned the following
// way by default, and this can be used in combination with the solenoid:
#define LED_NUM_LOCK_PIN B4
#define LED_CAPS_LOCK_PIN B5

#define LED_SCROLL_LOCK_PIN B3
// ^ Note: The B3 pin on normal classical xwhatsit/wcass controllers is a corner-pin of the atmega,
// which is not used, so it's easy to solder to for custom modifications.
// In the 33-pin version of the wcass board, pins B3, B4, B5 are all brought as extra pins to the
// row of pins connecting the sense matrix, making it easy to connect up the locklight leds.

// Uncomment below if the leds are on when the pin is driving zero:
//#define LED_NUM_LOCK_ACTIVE_LOW
//#define LED_CAPS_LOCK_ACTIVE_LOW
//#define LED_SCROLL_LOCK_ACTIVE_LOW
"""

wcass_and_xwhatsit_beamspring_full_v2_leds = """// If the lock lights are not used, then please don't define the below pins,
// or leave them set as unused pins:

// The following definitions match the lock lights as used by the Beamspring Full-size V2 keyboards by Model F Labs:
#define LED_NUM_LOCK_PIN B5
#define LED_CAPS_LOCK_PIN B4
#define LED_SCROLL_LOCK_PIN B3
// In the 33-pin version of the wcass board, pins B3, B4, B5 are all brought as extra pins to the
// row of pins connecting the sense matrix, making it easy to connect up the locklight leds.

// Uncomment below if the leds are on when the pin is driving zero:
//#define LED_NUM_LOCK_ACTIVE_LOW
//#define LED_CAPS_LOCK_ACTIVE_LOW
//#define LED_SCROLL_LOCK_ACTIVE_LOW
"""

wcass_and_xwhatsit_old_style_locklights_configuration = """// If the lock lights are not used, then please don't define the below pins,
// or leave them set as unused pins:

// The following definitions match the lock lights as used by the original
// xwhatsit firmware:
#define LED_NUM_LOCK_PIN B5
#define LED_CAPS_LOCK_PIN B6
#define LED_SCROLL_LOCK_PIN B4

// Uncomment below if the leds are on when the pin is driving zero:
//#define LED_NUM_LOCK_ACTIVE_LOW
//#define LED_CAPS_LOCK_ACTIVE_LOW
//#define LED_SCROLL_LOCK_ACTIVE_LOW
"""

wcass_and_xwhatsit_shrunk_f104_locklights_configuration = """// If the lock lights are not used, then please don't define the below pins,
// or leave them set as unused pins:

// The following definitions match how the locklights have been soldered on the "shrunk" f104 round1 keyboards:
#define LED_NUM_LOCK_PIN B5
#define LED_CAPS_LOCK_PIN B4
#define LED_SCROLL_LOCK_PIN B6

// Uncomment below if the leds are on when the pin is driving zero:
//#define LED_NUM_LOCK_ACTIVE_LOW
//#define LED_CAPS_LOCK_ACTIVE_LOW
//#define LED_SCROLL_LOCK_ACTIVE_LOW
"""


locklights_note = """  Note that this version of the firmware is configured primarly for locklights operation (limited solenoid support), where the lock lights are expected to be connected to the expansion
  header using the classic xwhatsit pinout. Some solenoid support is kept, by outputting the slenoid trigger and enable signals on other GPIOs, which the user may choose to manually solder to.
"""

universal_desc = """one of the xwhatsit controller PCBs supported by the 'universal' driver: the TH_XWhatsIt controller, or one of the SMD Model F controllers.

  The open hardware controllers supported by this firmware are published here:
    https://github.com/listofoptions/TH-XWhatsIt
    https://github.com/purdeaandrei/SMDModelFController
    https://github.com/purdeaandrei/SMD4704KishsaverClassModelFController
    https://github.com/purdeaandrei/SMDModelFController/tree/extra_columns
  And they have been discussed in the following threads:
    TH: https://deskthority.net/viewtopic.php?f=7&t=23406
    SMD Model F: https://deskthority.net/viewtopic.php?f=7&t=24597
"""

universal_b_desc = """one of the xwhatsit controller PCBs supported by the 'universal' driver: the TH_XWhatsIt controller, or the Compact Beamspring controller.

  The open hardware controllers supported by this firmware are published here:
    https://github.com/listofoptions/TH-XWhatsIt
    https://github.com/purdeaandrei/CompactBeamSpring
    https://github.com/purdeaandrei/CompactBeamSpringAdditionalExpansion
  And they have been discussed in the following threads:
    https://deskthority.net/viewtopic.php?f=7&t=23406
    https://deskthority.net/viewtopic.php?f=50&t=24512
"""

universal_b_th_only_desc = """the TH-XWhatsIt controller.

  The open hardware controller supported by this firmware are published here:
    https://github.com/listofoptions/TH-XWhatsIt
  And they have been discussed in the following thread:
    https://deskthority.net/viewtopic.php?f=7&t=23406
"""

wcass_desc = """the wcass controller PCB.

  The "wcass" controller design has been developed and published here: https://deskthority.net/viewtopic.php?f=7&t=13479
"""

xwhatsit_desc_common = """  Design documentation for the original Xwhatsit boards can be found here: https://static.wongcornall.com/ibm-capsense-usb-web/ibm-capsense-usb.html
  Installation guides, open hardware source files, (and original firmware) are downloadable here: https://static.wongcornall.com/ibm-capsense-usb/
"""

xwhatsit_desc = "the original Xwhatsit model F rev. 1 or rev. 2 controller PCB.\n\n" + xwhatsit_desc_common
xwhatsit_rev4_desc = "the original Xwhatsit beamspring controller PCB rev. 4.\n\n" + xwhatsit_desc_common
xwhatsit_displaywriter_desc = "the original Xwhatsit displaywriter controller PCB.\n\n" + xwhatsit_desc_common

ellipse_shrunk_and_nonshrunk_are_different = "Note that the locklight leds are soldered to the extension header of the wcass controller, and the wiring is different between the nonshrunk and shrunk variants."

controllers = {
    "universal" : {
        "desc": universal_desc,
        "config" : configh_head + "\n#define CONTROLLER_IS_UNIVERSAL_MODEL_F\n\n%OVERRIDE_TYPE%" + universal_solenoid + "\n" + universal_normal_leds,
    },
    "universal_b" : {
        "path": "universal",
        "desc": universal_b_desc,
        "config" : configh_head + "\n#define CONTROLLER_IS_UNIVERSAL_BEAMSPRING\n\n%OVERRIDE_TYPE%" + universal_solenoid + "\n" + universal_normal_leds,
    },
    "universal_b_th_only" : {
        "path": "universal",
        "desc": universal_b_th_only_desc,
        "config" : configh_head + "\n#define CONTROLLER_IS_UNIVERSAL_BEAMSPRING\n\n%OVERRIDE_TYPE%" + universal_solenoid + "\n" + universal_normal_leds,
    },
    "universal_b_exp" : {
        "path": "universal",
        "desc": universal_b_desc,
        "config" : configh_head + "\n#define CONTROLLER_IS_UNIVERSAL_BEAMSPRING\n\n%OVERRIDE_TYPE%" + universal_solenoid + "\n" + universal_b_exp_leds,
    },
    "wcass" : {
        "desc": wcass_desc,
        "config" : configh_head + "\n#define CONTROLLER_IS_WCASS_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid + "\n" + wcass_and_xwhatsit_normal_leds,
    },
    "wcass_locklights" : {
        "desc": wcass_desc + "\n" + locklights_note,
        "config" : configh_head + "\n#define CONTROLLER_IS_WCASS_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid_restricted + "\n" + wcass_and_xwhatsit_old_style_locklights_configuration,
    },
    "xwhatsit" : {
        "desc": xwhatsit_desc,
        "config" : configh_head + "\n#define CONTROLLER_IS_XWHATSIT_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid + "\n" + wcass_and_xwhatsit_normal_leds,
    },
    "xwhatsit_displaywriter" : {
        "path": "xwhatsit",
        "desc": xwhatsit_displaywriter_desc,
        "config" : configh_head + "\n#define CONTROLLER_IS_XWHATSIT_DISPLAYWRITER\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid + "\n" + wcass_and_xwhatsit_normal_leds,
    },
    "xwhatsit_rev4" : {
        "desc": xwhatsit_rev4_desc,
        "config" : configh_head + "\n#define CONTROLLER_IS_XWHATSIT_BEAMSPRING_REV_4\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid + "\n" + wcass_and_xwhatsit_normal_leds,
    },
    "xwhatsit_locklights" : {
        "desc": xwhatsit_desc + "\n" + locklights_note,
        "config" : configh_head + "\n#define CONTROLLER_IS_XWHATSIT_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid_restricted + "\n" + wcass_and_xwhatsit_old_style_locklights_configuration,
    },
    "wcass_f104_nonshrunk" : {
        "path": "wcass",
        "desc": wcass_desc + "\n  " + ellipse_shrunk_and_nonshrunk_are_different + "\n",
        "config" : configh_head + "\n#define CONTROLLER_IS_WCASS_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid_restricted + "\n" + wcass_and_xwhatsit_old_style_locklights_configuration,
    },
    "wcass_f104_shrunk" : {
        "path": "wcass",
        "desc": wcass_desc + "\n  " + ellipse_shrunk_and_nonshrunk_are_different + "\n",
        "config" : configh_head + "\n#define CONTROLLER_IS_WCASS_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid_restricted + "\n" + wcass_and_xwhatsit_shrunk_f104_locklights_configuration,
    },
    "xwhatsit_f104_nonshrunk" : {
        "path": "xwhatsit",
        "desc": xwhatsit_desc + "\n  " + ellipse_shrunk_and_nonshrunk_are_different + "\n",
        "config" : configh_head + "\n#define CONTROLLER_IS_XWHATSIT_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid_restricted + "\n" + wcass_and_xwhatsit_old_style_locklights_configuration,
    },
    "xwhatsit_f104_shrunk" : {
        "path": "xwhatsit",
        "desc": xwhatsit_desc + "\n  " + ellipse_shrunk_and_nonshrunk_are_different + "\n",
        "config" : configh_head + "\n#define CONTROLLER_IS_XWHATSIT_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid_restricted + "\n" + wcass_and_xwhatsit_shrunk_f104_locklights_configuration,
    },
    "wcass_beamspring_full_v2" : {
        "path": "wcass",
        "desc": wcass_desc,
        "config" : configh_head + "\n#define CONTROLLER_IS_WCASS_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid + "\n" + wcass_and_xwhatsit_beamspring_full_v2_leds,
    },
    "wcass_beamspring_full_v1" : {
        "path": "wcass",
        "desc": wcass_desc + "\n  " + "The locklight leds are soldered to the extension header of the wcass controller." + "\n",
        "config" : configh_head + "\n#define CONTROLLER_IS_WCASS_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid_restricted + "\n" + wcass_and_xwhatsit_old_style_locklights_configuration,
    },
    "xwhatsit_beamspring_full_v1" : {
        "path": "xwhatsit",
        "desc": xwhatsit_desc + "\n  " + "The locklight leds are soldered to the extension header of the xwhatsit controller." + "\n",
        "config" : configh_head + "\n#define CONTROLLER_IS_XWHATSIT_MODEL_F\n\n%OVERRIDE_TYPE%" + wcass_and_xwhatsit_solenoid_restricted + "\n" + wcass_and_xwhatsit_old_style_locklights_configuration,
    },
}

# The follwing warning is added to universal, and xwhatsit controller variants:
ellipse_warning = \
"""WARNING: None of the keyboards that ship from modelfkeyboards.com come with a controller compatible with this firmware!
This firmware is only useful if you decide to modify your keyboard, and replace the controller PCB with a non-default one.
Otherwise please consult which controller you have in your keyboard and choose the correct one. Early keyboards shipped with the "wcass" controller,
and there are plans that in the future keyboards will be shipped with the "leyden_jar" controller."""

ellipse_boards = [
    ['beamspring_full',         ["wcass_beamspring_full_v1", 'xwhatsit_beamspring_full_v1', 'universal'], "https://www.modelfkeyboards.com/wp-content/uploads/2022/12/2022-12-10_00-51-55-scaled.jpg", "Beamspring full-size V1 by Model F Labs", '', '', 'force_beamspring'],
    ['beamspring_full_v2',      ["wcass_beamspring_full_v2", 'xwhatsit_beamspring_full_v1', 'universal'], "https://www.modelfkeyboards.com/wp-content/uploads/2022/12/2022-12-10_00-51-55-scaled.jpg", "Beamspring full-size V2 by Model F Labs", '', '', 'force_beamspring'],
    ['beamspring_ssk',          ["wcass_beamspring_full_v2", 'xwhatsit', 'universal'], "https://www.modelfkeyboards.com/wp-content/uploads/2022/12/2021-08-06_23-42-10-scaled.jpg", "Beamspring SSK by Model F Labs", '', '', 'force_beamspring'],
    ['f104_round_1_nonshrunk',  ["wcass_f104_nonshrunk", "xwhatsit_f104_nonshrunk", 'universal'], "https://www.modelfkeyboards.com/wp-content/uploads/2023/03/2022-11-28_18-18-03-scaled.jpg", "F104 round 1 non-shrunk, by Model F Labs"],
    ['f104_round_1_shrunk',     ["wcass_f104_shrunk", "xwhatsit_f104_shrunk", 'universal'], "https://www.modelfkeyboards.com/wp-content/uploads/2023/03/2022-11-28_18-18-03-scaled.jpg", "F104 round 1 shrunk, by Model F Labs"],
    ['f62',                     ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/uwqPTyth.jpeg', 'F62 reproduction by Model F Labs'],
    ['f62_scumyc',              ['wcass', 'universal', 'xwhatsit'], 'https://geekhack.org/index.php?action=dlattach;topic=79141.0;attach=271408;image', 'F62 reproduction, with "scumyc" layout, by Model F Labs'],
    ['f77',                     ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/f8Z0mwHh.jpeg', 'F77 reproduction by Model F Labs'],
    ['fssk_round_1',            ['wcass', 'universal', 'xwhatsit'], 'https://www.modelfkeyboards.com/wp-content/uploads/2023/03/2022-11-28_18-30-43.jpg', 'FSSK round 1 by Model F Labs'],
]

ellipse_credit = "Model F Labs"
ibm_credit = "IBM"

keyboards = [
    [[ibm_credit], 'ibm/3101_3727_3278_87key',           ['universal_b', 'xwhatsit_rev4'], 'https://i.imgur.com/2vv6Cunh.jpeg', 'IBM Beamspring 3101/3727/3728 (87-key)'],
    [[ibm_credit], 'ibm/3276_3278_75key',                ['universal_b', 'xwhatsit_rev4'], 'https://i.imgur.com/juemGB1h.jpg', 'IBM Beamspring 3276/3278 (75-key)'],
    [[ibm_credit], 'ibm/3277_66key',                     ['universal_b', 'xwhatsit_rev4'], 'https://i.imgur.com/qxjrCJ6h.jpeg', 'IBM Beamspring 3277 (66-key)', "\nThis keyboard uses [emdude's sense PCB](https://github.com/emdude/XWhatsit-CommonSense-Compatible-IBM-3277-PCB)"],
    [[ibm_credit], 'ibm/3277_78key',                     ['universal_b', 'xwhatsit_rev4'], 'https://i.imgur.com/GNJhCxeh.jpg', 'IBM Beamspring 3277 (78-key)', "\nThis keyboard uses [emdude's sense PCB](https://github.com/emdude/XWhatsit-CommonSense-Compatible-IBM-3277-PCB)"],
    [[ibm_credit], 'ibm/3277_split_66key',               ['universal_b', 'xwhatsit_rev4'], 'https://i.imgur.com/CzZI5Inh.jpg', 'IBM Beamspring 3277 (split 66-key)', "\nThis keyboard uses [emdude's sense PCB](https://github.com/emdude/XWhatsit-CommonSense-Compatible-IBM-3277-PCB)"],
    [[ibm_credit], 'ibm/5251',                           ['universal_b', 'xwhatsit_rev4'], 'https://i.imgur.com/kncrpQBh.jpeg', 'IBM Beamspring 5251'],
    [[ibm_credit], 'ibm/5251_hebrew',                    ['universal_b', 'xwhatsit_rev4'], 'https://deskthority.net/download/file.php?id=76243', 'IBM Beamspring 5251 (Hebrew variant)'],
    [[ibm_credit], 'ibm/displaywriter',                  ['universal_b_th_only', 'xwhatsit_displaywriter'], 'https://i.imgur.com/OY39Zjmh.jpeg', 'IBM Displaywriter Beamspring'],
    [[ibm_credit], 'ibm/bigfoot_fxt_type_1',             ['universal_b'], 'https://i.imgur.com/N7tnovWh.jpeg', 'IBM Model F Bigfoot / FXT type 1', """
These keyboards are supported by using an the TH xwhatsit, or using the Compact Beamspring controllers,
and handwiring it into the original sense PCB which must be cut up to remove the original controller.
Wires are connected so that no two row/column wires cross.
If you are using the Compact Beamspring controllers, or the TH xwhatsit with a daughtercard, please be aware that one of pins between the beamspring pinout column pins is a not connected pin. This must be skipped. This is not the case when wiring directly to the TH xwhatsit daughterboard.
Please be aware that two of the pads in the row of column pads on the sense PCB don't actually go to any columns, these must be skipped.
There are 23 columns in total, when cutting the PCB please make sure to allow access to the final 3 columns too. The pads for the final 3 columns are a little misaligned""", '', 'force_modelf'],
    [[ibm_credit], 'ibm/bigfoot_fxt_type_1',             ['xwhatsit_rev4'], 'https://i.imgur.com/N7tnovWh.jpeg', 'IBM Model F Bigfoot / FXT type 1', """
These keyboards are supported by using an original Xwhatsit beamspring rev. 4 controller PCB,
and handwiring it into the original sense PCB which must be cut up to remove the original controller.
Wires are connected so that no two row/column wires cross.
Please be aware that one of pins between the beamspring pinout column pins is a not connected pin. This must be skipped.
Also please be aware that on the sense PCB two of the pads in the row of column pads don't actually go to any columns, these must also be skipped.
There are 23 columns in total, when cutting the PCB please make sure to allow access to the final 3 columns too. The pads for the final 3 columns are a little misaligned""", '', 'force_modelf'],
    [[ibm_credit], 'ibm/4978',                           ['universal_b_th_only'], 'https://i.imgur.com/AU17ntvh.jpg', 'IBM Beamspring 4978 "Beamship"'],
    [[ibm_credit], 'ibm/3278_3279_led_78key',            ['universal_b_exp'], 'https://i.imgur.com/xqc1oBAh.jpg', 'IBM Beamspring 3278/3279 (78-key)', """
It is recommended to use the Compact Beamspring with Addition Expansion controller:
https://github.com/purdeaandrei/CompactBeamSpringAdditionalExpansion
Please read this document for details on how to perform the necessary connections:
https://github.com/purdeaandrei/CompactBeamSpringAdditionalExpansion/blob/master/top_panel_modifications.md

Alternatively, in the absence of a Compact Beamspring with Addition Expansion controller,
it may also be possible to solder the connections directly to the pro micro of a TH controller or a normal Compact Beamspring
controller, however this is not recommended."""],
    [['Alectardy98'], 'ibm/beamal',                         ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/XD9zxDkh.png', 'BEAMal', """
PCB image:
https://i.imgur.com/RT8Gwhhh.png
Project URL:
https://github.com/Alectardy98/pcb_BEAMal_Rev1
""", '', 'force_beamspring'],
    [[ibm_credit], 'ibm/3178',                           ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/VvDPHQQh.jpeg', 'IBM Model F 3178 "Blue Switch"', """
WARNING: the 3178 "blue switch" keyboard has an unusual pinout with many pins shifted, so you will need to:
 * If you're using an original Xwhatsit Model F controller, you will also need the thin adaptor board designed for 3178 keyboards, or you will need to connect it with individual wires, keeping in mind those shifted pins.
 * If you're using and SMD Model F controller, or a TH controller with daughterboard, then simply choose the alternate row of pins that are marked to be used with 3178 keyboards.
 * If you're using a wcass controller, or just the motherboard of the TH controller, then you will need to keep in mind the shifted pins when connecting the keyboard using individual wires."""],
    [[ibm_credit], 'ibm/f104',                           ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/d4qxnCB.jpg', 'IBM Model F F104 "Unsaver"'],
    [[ibm_credit], 'ibm/f107',                           ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/cKKBK9uh.jpeg', 'IBM Model F 4704 F107'],
    [[ibm_credit], 'ibm/f122',                           ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/Tha5SqIh.jpg', 'IBM Model F F122'],
    [[ibm_credit], 'ibm/f50',                            ['wcass', 'universal', 'xwhatsit'], 'http://kishy.ca/wp-content/uploads/2014/07/6019273_0003-1024x872.jpg', 'IBM Model F 4704 F50'],
    [[ibm_credit], 'ibm/f62',                            ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/o852pMMh.jpg', 'IBM Model F 4704 F62 "kishsaver"'],
    [[ibm_credit], 'ibm/fat',                            ['wcass', 'universal', 'xwhatsit', 'wcass_locklights', 'xwhatsit_locklights'], 'https://i.imgur.com/5YjgiXWh.jpeg', 'IBM Model F AT'],
    [[ibm_credit, 'i$'], 'ibm/fext',                           ['wcass', 'universal', 'xwhatsit'], 'https://deskthority.net/download/file.php?id=28909', 'FEXT', """
These are IBM Model M, or Unicomp Model M full-size keyboards modified with an "FEXT" sense pcb, and Model F flippers.
For Unicomp keyboards only the winkeyless and tsangan bottom rows are supported. (If the keyboard has a menu key, it won't work)

The FEXT project has been developed here: https://deskthority.net/viewtopic.php?t=10744"""],
    [[ibm_credit, 'i$'], 'ibm/fssk',                           ['wcass', 'universal', 'xwhatsit'], 'https://deskthority.net/download/file.php?id=29306', 'FSSK', """
These are IBM Model M SSK keyboards modified with a "Sun FSSK" sense pcb, and Model F flippers.
The FSSK project has been developed here: https://deskthority.net/viewtopic.php?t=10744"""],
    [[ibm_credit, 'Sun'], 'ibm/sun_fssk',                       ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/D0XW67Yh.jpeg', 'Sun FSSK', """
These are IBM Model M SSK keyboards modified with a "Sun FSSK" sense pcb, and Model F flippers."""],
    [[ibm_credit, 'i$'], 'ibm/fssk_v1_0b',                     ['wcass', 'universal', 'xwhatsit'], 'https://deskthority.net/download/file.php?id=29306', 'FSSK v1.0b', """
These are IBM Model M SSK keyboards modified with an "FSSK" sense pcb, and Model F flippers.
The FSSK project has been developed here: https://deskthority.net/viewtopic.php?t=10744

Note: FSSK v1.0b was never officially released by i$, however the FEXT 1.0b board has been designed such that
if chopping it shorter no additional path cables would be required. This firmware supports such chopped boards.
Also tamsin has released a nicely modified FSSK v1.0b diptrace file too, which can be found over here:
https://deskthority.net/viewtopic.php?p=512949#p512949""", '\n\nNOTE: The above image is not accurate (it\'s of the v1.0 version)'],
    [[ibm_credit, 'Alectardy98'], 'ibm/fxtal',                          ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/KJd0ymjh.jpg', "FXTal", """
These are IBM Model F XT/Bigfoot keyboards modified with the FXTal sense pcb, and by drilling some additional holes into the barrel plate.
This firmware supports both the FXTal rev1 and FXTal rev2 keyboards.
This firmware doesn't support FXTal rev0.
FXTal rev1 is published here: https://github.com/Alectardy98/pcb_FXTal_Rev1"""],
    [[ibm_credit], 'ibm/fxt_type_2',                     ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/AD8fc8Th.jpeg', 'IBM Model F XT Type 2', """
Most Model F XT keyboards are type 2, See the Types section of this wiki: https://deskthority.net/wiki/IBM_Personal_Computer_keyboard#Types

This firmware is designed for a keyboard that has been converted in a similar way to the following post: https://deskthority.net/viewtopic.php?t=19522
The post shows an original xwhatsit controller, however please keep the same general intent with any other controllers too:
namely wires are connected so that no two row/column wires cross, and the column wires in use are those 12 that are closest to the row-side of the controller.
This applies if using one of the SMD Model F controller types, if using the TH controller with a daughtercard, or if using the 'wcass' controller.
If wiring in the TH controller directly, make sure that you skip the 7 columns coming off of the third (optional) shift register, like the daughterboard would do."""],
    [[ibm_credit, 'wcass'], 'ibm/xtant',                          ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/UbgPFWmh.jpg', 'Xtant', """
The Xtant is a Model F XT converted to a modern layout, project by wcass:
  https://deskthority.net/viewtopic.php?f=7&t=3047"""],
    [[ibm_credit, 'tamsin'], hand + 'tamsin/6770_wheelwriter',     ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/c7o0aIDh.jpg', "Tamsin 6770 wheelwriter"],
    [['tamsin'], hand + 'tamsin/alice',                ['wcass', 'universal', 'xwhatsit'], 'https://i.imgur.com/hxuaAb6h.png', "Tamsin Alice"],
    [['sneakyrobb'], hand + 'sneakyrobb/beam104',          ['universal'], 'https://deskthority.net/download/file.php?id=60486', 'Sneakyrobb Beam104', '', '', 'force_beamspring', lambda x: x + "\n#define CAPSENSE_CAL_THRESHOLD_OFFSET 210\n"],
]

for board in ellipse_boards:
    for ctl in board[1]:
        if ctl.startswith('universal') or ctl.startswith('xwhatsit'):
            warnedline = [[ellipse_credit], ellipse + "/" + board[0], [ctl]] + board[2:]
            if len(warnedline) >= 6:
                warnedline[5] += "\n\n" + ellipse_warning
            elif len(warnedline) == 5:
                warnedline.append("\n" + ellipse_warning)
            keyboards.append(warnedline)
        else:
            keyboards.append([[ellipse_credit], ellipse + "/" + board[0], [ctl]] + board[2:])

readme_template = r'''# %KEYBOARD%

![%KEYBOARD%](%IMAGELINK%)%PICTURENOTE%

A short description of the keyboard/project

* Keyboard Maintainer: [Purdea Andrei](https://github.com/purdeaandrei)
* Hardware Supported: Supports the %KEYBOARDLONGNAME% keyboards, using %USING%
* Hardware Availability: Rare collector's item
%KEYBOARDNOTE%

Make example for this keyboard (after setting up your build environment):

    make %KEYBOARD%:default

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).
'''


for k in keyboards:
    for cname in k[2]:
        cpath = cname
        if 'path' in controllers[cname]:
            cpath = controllers[cname]['path']
        k_path = "xwhatsit/" + k[1] + "/" + cpath
        full_path = "keyboards/" + k_path
        data = readme_template.replace('%KEYBOARD%', k_path).replace('%IMAGELINK%', k[3]).replace('%KEYBOARDLONGNAME%', k[4]).replace("%USING%", controllers[cname]['desc'])
        if len(k) >= 6 and k[5]:
            data = data.replace('%KEYBOARDNOTE%', k[5])
        else:
            data = data.replace('%KEYBOARDNOTE%\n', '')
        if len(k) >= 7 and k[6]:
            data = data.replace('%PICTURENOTE%', k[6])
        else:
            data = data.replace('%PICTURENOTE%', '')
        override_type = ''
        if len(k) >= 8 and k[7]:
            if k[7] == "force_beamspring":
                override_type="// We're using a controller PCB that is normally designed for Model F keyboards, on a beamspring keyboard, so we must define this:\n#define CAPSENSE_CONDUCTIVE_PLASTIC_IS_PULLED_UP_ON_KEYPRESS\n\n"
            if k[7] == "force_modelf":
                override_type="// We're using a beamspring controller to drive a Model F keyboard:\n#define CAPSENSE_CONDUCTIVE_PLASTIC_IS_PUSHED_DOWN_ON_KEYPRESS\n\n"
        cdata = controllers[cname]['config'].replace("%OVERRIDE_TYPE%", override_type)
        if len(k) >= 9 and k[8]:
            cdata = k[8](cdata)
        f = open(full_path + "/readme.md", "w")
        f.write(data)
        f.close()
        f = open(full_path + "/config.h", "w")
        f.write(cdata)
        f.close()
        f = open(full_path + "/info.json", "r")
        json = f.read()
        f.close()
        json = re.sub('    "keyboard_name":.*\n', '    "keyboard_name": "' + k[4].replace('"', '\\"') + '",\n', json)
        credits = k[0] + ['Tom Wong-Cornall']
        if 'wcass' in cname and 'wcass' not in credits:
            credits.append('wcass')
        if 'leyden' in cname:
            credits.append('Rico')
        if 'universal' in cname:
            credits.extend(['listofoptions', 'kmnov2017'])
        credits.append('Purdea Andrei')
        credits_str = "/".join(credits)
        json = re.sub('    "manufacturer":.*\n', '    "manufacturer": "' + credits_str.replace('"', '\"') + '",\n', json)
        f = open(full_path + "/info.json", "w")
        f.write(json)
        f.close()
