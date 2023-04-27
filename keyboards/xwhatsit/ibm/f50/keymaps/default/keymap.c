/* Copyright 2020 Purdea Andrei
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include QMK_KEYBOARD_H

// Defines names for use in layer keycodes and the keymap
enum layer_names {
    _BASE,
    _FN,
    _FN2
};


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /* Base */
    [_BASE] = LAYOUT(
        KC_ESC,   KC_PSLS, KC_PAST,    KC_MINS, KC_EQL,   KC_DEL,     KC_PSCR, KC_COMM, KC_DOT,  KC_BSPC,
        KC_Q,     KC_W,    KC_E,       KC_R,    KC_T,     KC_Y,       KC_U,    KC_I,    KC_O,    KC_P,
        KC_A,     KC_S,    KC_D,       KC_F,    KC_G,     KC_H,       KC_J,    KC_K,    KC_L,    KC_ENT,
        KC_LSFT,  KC_Z,    KC_X,       KC_C,    KC_V,     KC_B,       KC_N,    KC_M,    KC_SCLN, KC_NUHS,
        KC_LCTL,  MO(_FN), KC_LALT,    KC_TAB,  KC_QUOT,  KC_SPC,     KC_BSLS, KC_COMM, KC_DOT,  KC_SLSH
    ),
    [_FN] = LAYOUT(
        _______,  _______, _______,    _______, _______,  _______,    _______, _______, _______, _______,
        _______,  _______, _______,    _______, _______,  _______,    _______, _______, _______, _______,
        _______,  _______, _______,    _______, _______,  _______,    _______, _______, _______, _______,
        _______,  _______, _______,    _______, _______,  _______,    _______, _______, _______, _______,
        _______,  _______, _______,    _______, _______,  MO(_FN2),   _______, _______, _______, _______
    ),
    [_FN2] = LAYOUT(
        _______,  _______, _______,    _______, _______,  _______,    _______, _______, _______, _______,
        _______,  _______, EE_CLR,     QK_BOOT, _______,  _______,    _______, _______, _______, _______,
        _______,  _______, DB_TOGG,    _______, _______,  _______,    _______, _______, _______, _______,
        _______,  _______, _______,    _______, _______,  _______,    _______, _______, _______, _______,
        _______,  _______, _______,    _______, _______,  _______,    _______, _______, _______, _______
    )
};

