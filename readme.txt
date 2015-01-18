Statistical Operations GUI
Copyright (C) 2015  Alexander Hollaus <office@knofy.net>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

=======================================================================

Step 1: Installation

You need to have the python3 and tkinter-Module for python3 installed.

For installation on Debian systems use:
sudo apt-get install python3 python3-tk

=======================================================================

Step 2: Start

Execute start.py to run the program
Open the program-Folder in the console and start the program either by:
./start.py or python3 start.py

=======================================================================

Step 3: Usage

1. Click on the button 'Open' to select a CSV-File you want to perform
statistical operations on (in the folder 'testfiles' are already a few
files you can use). The File must have one header-line and valid values
otherwise statistical calculations are not possible by this program.

2. With 'Select Column' choose the selected column of the file you want
to use. If a column is not in the list but exists in the file, this means
that there is a conflict with one of the values and for the stability of
the program the column is excluded from statistical operations.

3. With 'Select Operation' you choose the type of statistical calculation
you want to perform on the selected column.

4. Click on 'Calculate'. The result will be shown in the field 'Result'.

=======================================================================

Step 4: Feedback

If you like this program and/or have any recommendations, questions or
complaints feel free to contact me at <office@knofy.net>