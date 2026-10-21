.. _use_dat_data_view:

Data Viewer
===========

.. include:: ../../shared/variables.rst

.. include:: ../../appendices/appendices.rst


INTERMAGNET provides software called "imcdview" to work with the data 
from the DOIs, web downloads and from the INTERMAGNET Physical Media 
(IPM). This software can be downloaded from |imag_software| .
The software is designed to be simple and easy to use. When the
software starts for the first time on a new computer, a dialog
is displayed describing how to configure the software to find
data. This same information, on how to find data, is available
from the "Help" menu under "Help for New Users".

The program has 3 main windows. The window that you see when
the program starts shows a view of the world. The observatories
that the program has discovered in its database(s) are shown as
red dots on the world map. If you move your mouse over an
observatory its name will be displayed. If you click on an
observatory using the left mouse button then a popup-menu will
appear with a list of data that you can view. If you use the
right mouse button you will get the same menu, but in a
permanent window that will not close when you select an item
from the menu. The World Map window also holds the program’s
toolbar. The World Map window is always present while the
software is running. If you close this window, the program will
exit.

There is also an Explorer window. 
This window gives you an alternative view of data,
similar in structure to the directory structure used to hold
the data. To view an object in the
Explorer window, double click the object. For example, to plot
data from an observatory using the Explorer window, expand the
tree until the observatory is listed, expand the observatory,
select and expand the data file that you want to view then
double click the "Data Plot" icon. The Explorer window also
shows you which databases the program is using. For more
information about databases see the online help system.

The Data Catalogue option displays a colour-coded 
graphical view of available observatories and data from the program's database. 
Data can be accessed via sub-menus by clicking within the graphic.

The third main window is
the Export Window. This window allows you to create data files
in IAGA 2002 and other data formats from the INTERMAGNET
archive data. The window has been designed so that you can
convert as much data as you want with the minimum of work.
Further details are available in the online help system.

The software also includes an import function, allowing you to
convert data from IAGA 2002 and other data formats into the
INTERMAGNET Archive Format. This function is available from the
"Database" menu. Using this software, observatories can convert
their own data into IAF for delivery to INTERMAGNET. It’s also
possible to use the import and then export functions to convert
between data formats (e.g. to convert INTERMAGNET minute value
format to IAGA-2002), but please note that between import and
export the data will always be stored in IAF format and so the
precision of the data will be that provided by the IAF format
(1/10th nT and 1/10th minute of arc). For most modern data this
precision is unacceptably low, particularly for angular measurements.
As an alternative use the "gm_convert" or "MagPy" programs, also
available from INTERMAGNET, which do not suffer from this
restriction.

Prior to the current software, INTERMAGNET distributed a
DOS-based program for working with the DVD/CD-ROM data.
