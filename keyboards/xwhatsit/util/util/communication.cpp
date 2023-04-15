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

#include "communication.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include "../../util_comm.h"
#include <wchar.h>

#define EXPECTED_SERIAL_NUMBER_BEGINNING L"purdea.ro:qmk_xwhatsit"

Communication::Communication()
{
    if (hid_init() != 0)
    {
        std::cerr << "Error: Unable to run hid_init()" << std::endl;
        exit(-1);
    };
}

Communication::~Communication()
{
    hid_exit();
}

std::vector<std::string> Communication::scan()
{
    QMutexLocker locker(&mutex);
    std::vector<std::string> ret;

    hid_device_info *enu = hid_enumerate(0x0481, 0x0002);
    hid_device_info *devinfo = enu;
    while (devinfo != NULL)
    {
        if ((NULL != devinfo->manufacturer_string) &&
            (NULL != devinfo->product_string) &&
            (0==wcscmp(devinfo->manufacturer_string, L"Tom Wong-Cornall")) &&
            (0==wcscmp(devinfo->product_string, L"ibm-capsense-usb")))
        {
            // Original Xwhatsit firmware
            if (devinfo->interface_number == 1)
            {
                ret.push_back(std::string(devinfo->path) + XWHATSIT_ENDING_STRING);
            }
        } else if ((NULL != devinfo->manufacturer_string) &&
                   (wcsstr(devinfo->manufacturer_string, L"Purdea Andrei"))) {
            // All "Old Firmware" QMK xwhatsit firmware will have this substring
            if (devinfo->interface_number == 1)
            {
                ret.push_back(devinfo->path);
            }
        }
        devinfo = devinfo->next;
    }
    hid_free_enumeration(enu);

    enu = hid_enumerate(0x1209, 0x4704); // Model F Labs custom VID:PID pair
    devinfo = enu;
    while (devinfo != NULL)
    {
        if ((NULL != devinfo->manufacturer_string) &&
            (wcsstr(devinfo->manufacturer_string, L"Purdea Andrei"))) {
            // All "Old Firmware" QMK xwhatsit firmware will have this substring
            if (devinfo->interface_number == 1)
            {
                ret.push_back(devinfo->path);
            }
        } else if ((NULL != devinfo->serial_number) &&
                   (0==wcsncmp(devinfo->serial_number, EXPECTED_SERIAL_NUMBER_BEGINNING, wcslen(EXPECTED_SERIAL_NUMBER_BEGINNING)))) {
            // All "New Firmware" QMK xwhatsit firmware will have its serial number start like this.
            if (devinfo->interface_number == 1)
            {
                ret.push_back(devinfo->path);
            }
        }
        devinfo = devinfo->next;
    }
    hid_free_enumeration(enu);

    enu = hid_enumerate(0x16C0, 0x27DB);
    devinfo = enu;
    while (devinfo != NULL)
    {
        if ((NULL != devinfo->serial_number) &&
                   (0==wcsncmp(devinfo->serial_number, EXPECTED_SERIAL_NUMBER_BEGINNING, wcslen(EXPECTED_SERIAL_NUMBER_BEGINNING)))) {
            // All "New Firmware" QMK xwhatsit firmware will have its serial number start like this.
            if (devinfo->interface_number == 1)
            {
                ret.push_back(devinfo->path);
            }
        }
        devinfo = devinfo->next;
    }
    hid_free_enumeration(enu);

    return ret;
}

Device *Communication::open(std::string path)
{
    return new Device(path, mutex);
}
