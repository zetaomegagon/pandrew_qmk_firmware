# xwhatsit/ibm/bigfoot_fxt_type_1/universal

![xwhatsit/ibm/bigfoot_fxt_type_1/universal](https://i.imgur.com/N7tnovWh.jpeg)

A short description of the keyboard/project

* Keyboard Maintainer: [Purdea Andrei](https://github.com/purdeaandrei)
* Hardware Supported: Supports the IBM Model F Bigfoot / FXT type 1 keyboards, using one of the xwhatsit controller PCBs supported by the 'universal' driver: the TH_XWhatsIt controller, or the Compact Beamspring controller.

  The open hardware controllers supported by this firmware are published here:
    https://github.com/listofoptions/TH-XWhatsIt
    https://github.com/purdeaandrei/CompactBeamSpring
    https://github.com/purdeaandrei/CompactBeamSpringAdditionalExpansion
  And they have been discussed in the following threads:
    https://deskthority.net/viewtopic.php?f=7&t=23406
    https://deskthority.net/viewtopic.php?f=50&t=24512

* Hardware Availability: Rare collector's item

These keyboards are supported by using an the TH xwhatsit, or using the Compact Beamspring controllers,
and handwiring it into the original sense PCB which must be cut up to remove the original controller.
Wires are connected so that no two row/column wires cross.
If you are using the Compact Beamspring controllers, or the TH xwhatsit with a daughtercard, please be aware that one of pins between the beamspring pinout column pins is a not connected pin. This must be skipped. This is not the case when wiring directly to the TH xwhatsit daughterboard.
Please be aware that two of the pads in the row of column pads on the sense PCB don't actually go to any columns, these must be skipped.
There are 23 columns in total, when cutting the PCB please make sure to allow access to the final 3 columns too. The pads for the final 3 columns are a little misaligned

Make example for this keyboard (after setting up your build environment):

    make xwhatsit/ibm/bigfoot_fxt_type_1/universal:default

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).
