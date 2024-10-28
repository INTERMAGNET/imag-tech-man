.. _sub_dat_1min_data:

Definitive 1-Minute Data
========================

.. include:: ../../shared/variables.rst

.. include:: ../../appendices/appendices.rst

In January 1992 the Executive Council and Operations Committee
decided to produce a CD-ROM of definitive minute data values
from observatories of participating institutions, beginning
with 1991 data and continuing annually thereafter. Users thus
have access to global magnetic observatory data near real-time
values and also the final, definitive data. The institution
responsible for an IMO must deliver a complete set of
definitive data (this includes de-spiking, filling gaps where
possible, correcting baselines, and applying other processing
procedures). The baselines for one-minute definitive data must
also be included in the annual definitive data submissions to
INTERMAGNET.

The definitive data volume only contains data from
participating observatories. Participating observatories are
those that meet the INTERMAGNET standards, have been accepted
by the INTERMAGNET operations committee and also report their
data to a GIN within 72 hours of recording. The data from all
contributing observatories are provided by the institutions
responsible for those observatories.

One of the main objectives of INTERMAGNET is to process
definitive data as fast as possible and to make these data
available to users. To facilitate this, institutes should send
their definitive data in the INTERMAGNET binary data format as
well as accompanying files (e.g. baseline files) by ftp to the
Paris GIN’s ftp server as soon as possible and before the data
submission deadline which is set by INTERMAGNET operations
committee:

-  Host name: |gin_paris|
-  User name: userint
-  Password can obtained from Virginie Maury (vmaury@ipgp.fr)
   or Jan Reda (jreda@igf.edu.pl)


Once the data have been put on this server, INTERMAGNET then:

-  Checks the data for problems.
-  Transfers the data to the INTERMAGNET Web server.
-  Transfers the data to the World Data Centre Edinburgh
-  Publishes the data (CD-ROM up to 2005, DVD to 2013, USB
   memory to 2015, on-line publication after 2015). The annual
   data volume includes definitive data from all IMOs.

Institutes must prepare definitive data with extreme care. The
data are distributed widely. Publishing corrections to this
data set is a very difficult task.

Inspection of definitive data should be done carefully. The
method of inspection is left to each individual institute.
However software tools are available which can help in the
preparation and checking of data. These tools are available
from the Internet (see :numref:`sub_dat_1min_data_soft` for details).
The most important program to control the data is the imagcdview
Java browser which is also available on the annual data media
and on the INTERMAGNET web site: |imag_software|

Usually, after the end of the calendar year, INTERMAGNET
officers send an email to IMOs titled "Call For Data". This
email informs, among other things, about the delivery deadline
of definitive data. For this, the email list
|imag_imo_email| is used. The subject of this email
starts traditionally with the words "Call for Data". The
request always includes a submission date by which data must be
received at the Paris GIN ftp server (usually this deadline is
six months after the end of the year in which the data were
recorded). If an IMO misses the deadline:

- Only definitive data accepted before the publication
  deadline (specified by the Operations committee) will be
  included in the annual data publication.
- Definitive data delivered after this publication deadline
  will be published on the INTERMAGNET web site and subsequent
  data publications.
- Any corrections to definitive data will also be published on
  the INTERMAGNET web site and subsequent data publications.

Each INTERMAGNET observatory should put the following data and
information on the Paris ftp server:

A. Twelve files of definitive binary data, oriented XYZG.
B. One baseline file.
C. One readme file for the observatory.
D. One yearmean file listing annual mean values for the
   observatory.
E. Information about the readme-country file.
F. Information concerning the About-screen for the country.
G. Information concerning the Map of the institutes country.

For each of options E, F, and G, please state whether you want:

#. To use the same file as the previous year.
#. To make changes to the previous year's file (in which case
   please describe the changes).
#. To use a new file (in which case please put the new file on
   the server).

Please note the following:

- The total field element Fs included in the binary file, used
  to calculate G=Fv-Fs, should come from an absolute scalar
  magnetometer. INTERMAGNET is not accepting total field data
  calculated from a vector magnetometer.
- K-indices should be included in the binary files only. DKA
  files are created by INTERMAGNET from
  the binary data. Any DKA file provided by an institute will
  be ignored.
- INTERMAGNET needs information about changes (or lack of
  changes) to country files. The publication of data cannot be
  finished before receiving all country information (points
  E,F,G above). So delivery of country information before the
  deadline is very important.
- In cases when a country has several IMOs, the country
  information should be delivered by a single representative
  of the given country.


.. _sub_dat_1min_data_check:

Checking Procedure
------------------

In order to check the data for publication, it is necessary to
create a directory structure on disk similar to the structure
of the IRDS - this will allow the user to use the
imcdview software to view the data (imcdview is the Java
software). In order for imcdview to recognize that a directory contains
INTERMAGNET data, the subdirectories ctry_inf and yyyymaps are
needed even if they are empty.

A complete annual INTERMAGNET data structure includes the
following files (the following example is for the year 2010):

#. x:\\mag2010\\sss\\sss10mmm.bin (12 binary files in format IAF)
#. x:\\mag2010\\sss\\readme.sss (1 readme file)
#. x:\\mag2010\\sss\\sss2010.blv (1 baseline file)
#. x:\\mag2010\\sss\\yearmean.sss (1 annual means file)
#. x:\\mag2010\\2010maps\\country_id.xxx (1 map for each country (xxx = png or pcx))
#. x:\\mag2010\\ctry_inf\\readme.country_id (1 readme-file for each country)
#. x:\\mag2010\\ctry_inf\\country_id+srn.xxx (1 about-screen for each country
   (xxx = png or pcx))

sss is 3-letter observatory code, mmm is the month, country_id
is the country code. The same structure is also required by
most of the other programs used to check data.

Before putting INTERMAGNET files on the Paris GIN ftp server,
institutes must perform the following as a minimum set of
tests:

#. Review the whole year of binary data. Software for this
   action:

   #. **imcdview, imagplot.exe**

      The imcdview browser is written in Java and allows users
      to display data in both graphics (plots) and text modes.

   #. **imagplot.exe**

      The imagplot.exe works under Windows and allows users to
      create PostScript plots.

#. Check for any discrepancies between Fvector (Fv total field
   calculated on the basis of XYZ elements) and Fscalar (Fs
   recorded by means of proton magnetometer) for minute values.
   The resource that can be used to make this check is imcdview
   Java browser.

#. Check the binary data headers and the consistency of the
   binary data with the yearmean baseline, and readme files.

Software for this action: check1min.exe

The program check1min.exe checks the headers of the binary
data. It also checks whether recent yearly mean values
included in the yearmean.sss file are consistent with the 12
binary files, i.e. whether annual means included in the
yearmean file agree with annual means calculated from the
binary data. Please remember that for XYZG orientation the
D-conversion factor should be set to exactly 10000.

This program checks for discrepancies between elements
XYZFIDH, and also detects format errors.

#. K-numbers
   Software: Java browser IMCDVIEW, which is equipped, among
   other things, with a "K index Viewer".

   .. note::

     Program Kasm.exe available on INTERMAGNET web
     enables to include K-numbers to binary files generated
     according to the Adaptive Smoothing method.

#. Inspection of the BLV file

   Software for this action is also imcdview Java browser.

   The program imcdview makes it possible to produce PNG or PDF
   plots of baseline values. The plots are created from the
   SSSYYYY.BLV files

#. Inspection of readme files

   Readme files can be checked using any text editor, though an
   editor which can display non-printing characters (except Cr
   Lf), which should not be in readme and other text files, and
   gives easy control of line length is preferred. The contents
   of readme files can also be seen using imcdview.

.. _sub_dat_1min_data_soft:

Obtaining the Checking Software
-------------------------------

See the following web page to download the checking software:
|imag_software|


.. _sub_dat_1min_data_enc:

Data Encoding for Publication
-----------------------------

1-minute definitive data for an IMO are to be provided to
INTERMAGNET shortly after the end of each calendar year for
inclusion in the annual data publication. INTERMAGNET will send
out a "call for data" to each observatory, specifying the
deadline for providing data. Observatories should provide data
in the INTERMAGNET Archive Format (IAF) which is described in
|app_iaf|. Data can be converted to IAF using INTERMAGNET’s
"imcdview" viewing software, which can be obtained
from |imag_software|
Baseline data will accompany the definitive data, and will be
provided in format IBFV2.00 as described in |app_imag_ibf|.

.. _sub_dat_1min_data_enc_gen:

General Features
````````````````

The first INTERMAGNET CD-ROM contains data from 41
observatories provided by 11 countries for the year 1991. The
1992 and subsequent IPMs also contain baseline data for
the year for each observatory in the form of text and plots.
|app_obs| of this manual provides a list of observatories
currently contributing to the data publication.

.. _sub_dat_1min_data_enc_iaf:

IAF INTERMAGNET Archive Format
``````````````````````````````


The INTERMAGNET IRDS and IPM contain a variety of
metadata, including contact information and quality control
records. The geomagnetic data is held in INTERMAGNET Archive
Format. This format holds minute, hourly and daily mean values
as well as K indices.

The data are coded as 32-bit (long integer) binary words, with
5888 words comprising a day-long record. Each file contains one
month of day-records (so files are variable length, from 28 to
31 records). Each day of data has a header and data section,
the data being subdivided into minute means, hourly means,
daily means and a set of K-indices. To date, five versions of
this format have been used: IAFV1.00 being the original
description of the format. It was only designated as version
1.00 in 2007. Minor undocumented changes were made to how the
header was used over the lifetime of this version. IAFV1.10 was
defined in 2008 to add the publication date, encoding of the
format version number and to reserve word 16 in the header,
affecting words 14, 15 and 16. In 2009, delta-F was introduced
in IAFV2.00 affecting words 6,8 and 15 in the header, and words
4337 to 5776, words 5849 to 5872 and word 5876 in the data
section. Also in IAFV2.00, space padding was specified to be at
the left most position affecting word 13 in the header and
words 5885 to 5888 in the data section were made available for
each contributing institution. In 2010, IAFV2.10 was defined to
allow for a missing instrument designator affecting words 6 and
15 in the header, and words 4337 to 5776 in the data section.
In 2014, IAFV2.11 was introduced to add a data type flag in
word 15 to indicate whether the data is definitive or
quasi-definitive. |app_iaf| provides a schematic
representation of the record structure.

Each 1-day record requires 23,552 bytes, so a month-file for
January would require 730,112 bytes of storage. A year of
observatory data requires almost 8.6 Megabytes (Mb) of storage.
The storage capacity of a CD-ROM is about 640 Mb. A single
sided, single layer DVD holds about 4.7 Gb, a single sided,
double layer DVD about 8.5Gb. Following the increase of
observatories within INTERMAGNET and the evolution of the
physical media, definitive data were publised on one CD from
1991 to 1999, two CDs from 2000 to 2005, one DVD from 2006 to
2013 and on one USB drive thereafter.

Observatories should provide new definitive data to INTERMAGNET
in IAF V2.11, which is described here. In order to allow users
of historic CD-ROM/DVD/USB data to understand the format of the
data for each year of production, previous versions (and the
years they are associated with) are fully described in |app_iaf|.


.. _sub_dat_1min_data_enc_iaf_211:

IAFV2.11 (2014 and after)
"""""""""""""""""""""""""

Words 1 to 16 comprise the header section containing a mixture
of text and numeric fields, including a 3-letter observatory
identification preceded with a space [hex20] (ID) code, the
year concatenated with the day of the year, co-latitude,
longitude, elevation, reported orientation, originating
organization, a D-conversion factor, data quality,
instrumentation, K-9, sampling rate, sensor orientation,
publication date and format version/data type. Latitude,
longitude/colatitude and elevation must be given using the
WGS-84 datum. From 2014 onward, a field was been added to
indicate whether the data is definitive or quasi-definitive.
This field is a single bit flag in the second byte of word 15.
It will be encoded as 0x00 to indicate definitive data, 0x01 to
indicate quasi-definitive data. From 2010 onward, the
orientation codes "XYZ" and "HDZ" have been added to "XYZG" and
"HDZG" where "G" represents ΔF (see description below). These
new codes indicate that the observatory is recording 3 elements
only (no scalar instrument). The D-conversion factor is a fixed
value used only in the graphics portion of the access software
to allow Declination to be plotted in minutes of arc and
equivalent nanoteslas (nT). It is given as H/3438*10000, where
H is the annual mean value of the horizontal intensity.
Example: If H is 16500 D will be 47993(Integer). When XYZG or
XYZ is used, the D-conversion factor should be set to 10000.

ASCII values, such as the observatory ID and orientation, are
also stored as 32-bit words, but are coded as the hexadecimal
byte-string corresponding to the ASCII string. For example, the
string "HDZF" is coded as the sequence "48 44 5A 46". Where a
string is shorter than four bytes, it is padded to the left
with spaces. For example, the string "ESK" is coded as the
sequence "20 45 53 4B".

Word 11 is the K-9 value for the observatory in nT, word 12 is
the digital sampling rate in msec, and word 13 is the sensor
orientation. Sensor orientation could be XYZF, DIF, UVZ, HDZ,
HDZF etc. and should indicates which components are actually
measured. If a three component sensor orientation is used, a
space must be added to the left. Word 14 is the publication
date encoded as 4 ASCII bytes "YYMM" provided by INTERMAGNET.
The high byte (left most) of word 15 is the INTERMAGNET Archive
Format version number code provided by the IMO. It takes the
form of a binary single byte number ranging from 0 to 255. Zero
(0x00) represents version 1.00, one (0x01) represents version
1.10, two (0x02) represents version 2.00, three (0x03)
represents version 2.10 and four (0x04) represents version
2.11. The second byte in word 15 will be encoded as 0x00 to
indicate definitive data, 0x01 to indicate quasi-definitive
data. The other two bytes of word 15 are reserved for future
use and padded with zeros. Word 16 is reserved for future use.

Words 17-5776 contain the minute values of the 4 geomagnetic
elements (successively X,Y,Z,G or H,D,Z,G or X,Y,Z, or H,D,Z )
for the day. From 2009 onward, the 4th element contains the
difference between the square root of the sum of the squares of
the variometer components, F(v), and the total field from an
independent scalar recording, F(s). This difference, ΔF, is
defined as F(v) - F(s). Both F(v) and F(s) must be corrected to
the location in the observatory where absolute geomagnetic
observations are made. When F(s) is missing or both F(s) and
F(v) are missing, ΔF must be set to 999999. When F(v) only is
missing, ΔF must be set to -F(s). The values of the 4 elements
are stored in tenth-units with an implied decimal point. Thus,
an H value of 21305.6 is stored (in tenth-nT) as 213056 with a
decimal point implied between the last and next-to-last digits.
Words 5777-5872 are used for the hourly mean values of the
successive 4 elements. From 2009 onward, words 5849-5872 always
record 999999 (missing value), this is done because the 4th
element in the data is a quality check for minute mean data and
this quality check is meaningless for hourly means. Words
5873-5876 store the 4 daily mean values. From 2009 onward, word
5876 always record 999999 (missing value) because the quality
check for daily means is also meaningless. From 2009 onward,
the last 4 words (5885-5888) are available for each
contributing institution. Missing data for minute, hour, and
day values are stored as "999999". From 2010 onward, if a
scalar instrument is not used (so no data is recorded in the
fourth element) the value "888888" should be used instead of
"999999". Missing K-Index values are stored as "999".


.. _sub_dat_1min_data_enc_dir:

INTERMAGNET Reference Data Set and Physical Media Directory Structure
`````````````````````````````````````````````````````````````````````

This section describes the structure of the DVD (2011). The
structure of the INTERMAGNET Reference Data Set (IRDS), which is also the 
strucutre of the data on the INTERMAGNET Physical Media (IPM) at the example
is described in |app_imag_dir|.

The files are set up in a particular
directory structure. The root directory contains a "README.TXT"
file, which is an ASCII file describing the DVD and where to
obtain information about it, the software, and documentation;

On the 2011 DVD there are also three directories and a further
file. The directory called "ERRATA" contains a file
"ERRATA.TXT". This file lists errors on previous IPMs. A
second folder, called "SOFTWARE", holds the "imcdview"
programme, software, for visualizing and working with the data.
This software is described in :numref:`sub_dat_1min_data_enc_soft`
The file "imcdview_install.txt" describes how to install the imcdview software.

The final directory, MAG2011, contains a sub-directory for each
observatory identified by its 3-letter ID code. In addition,
there are sub-directories labeled "2011MAPS", "CTRY_INF", and
"OBSY_INF". The 2011MAPS directory contains the \*.PNG files
that are the map images of each country for use in the access
software. These are labeled by a 3-letter country ID with the
PNG extension, and one labeled "ALL.PNG" for all countries. The
CTRY_INF directory contains a \*.PNG file for each country (and
one for ALL) that are the images used to show the flag and
organizational Logo for the different countries, and the README
files that pertain to each country's geomagnetism program
(including a README for the ALL option). The OBSY_INF
subdirectory is empty, but is required to identify to software
that the this folder holds data in the IRDS
structure.

The individual sub-directories (e.g. BFE for Brorfelde, TUC for
Tucson, etc.) contain the 12 months of data labeled with the
3-letter ID, 2-character year, 3-letter month abbreviation, and
a "BIN" extension indicating they are binary files in the IAF
format (see  :numref:`sub_dat_1min_data_enc_iaf_211`).
For example, "BFE91AUG.BIN" is a file of 31 sequential day-records
for Brorfelde, for 1991, for August. In addition,
there are "README.XXX" files for the individual observatory,
a YEARMEAN.XXX containing annual mean data in plain text format f
or all years that the observatory has operated
(see |app_iyf| for details of the format)
and an XXX2011.BLV file that contains absolute observation and
baseline data in the INTERMAGNET baseline format (see |app_imag_ibf|)
where XXX indicates the 3-letter observatory ID.

This sub-directory may also contain a file labeled XXXYRK.DKA,
where XXX is the 3-letter observatory ID, YR is the 2-character
year value and K indicates a K-Index file. Originally the DKA
extension was used to indicate that the data were generated
from a digital algorithm in an ASCII format, however
subsequently these files have been used to hold both digitally
derived and hand-scaled K indices. Since the 2005 CD-ROM the
DKA files have been created by INTERMAGNET using data from the
binary IAF file (before 2005 these files were provided by the
observatories). These ASCII K-Index files are used, even though
the data are in the binary records, because they are much
faster to access than paging through the binary records.

.. _sub_dat_1min_data_enc_soft:

INTERMAGNET Reference Data Set and Physical Media Software
``````````````````````````````````````````````````````````

INTERMAGNET provides software to work with the data.
This software can be installed from the
IPM, or downloaded from |imag_software| .
The software is designed to be simple and easy to use. When the
software starts for the first time on a new computer, a dialog
is displayed describing how to tell the software where to find
data. This same information, on how to find data, is available
from the "Help" menu under "Help for New Users".

The program has 3 main windows. The window that you see when
the program starts shows a view of the World. The observatories
that the program has discovered in its database(s) are shown as
red dots on the world map. If you move your mouse over an
observatory its name will be displayed. If you click on an
observatory using the left mouse button then a popup-menu will
appear with a list of data that you can view. If you use the
right mouse button you will get the same menu, but in a
permanent window that will not close when you select an item
from the menu. The World Map window also holds the program’s
menu bar. The World Map window is always present while the
software is running. If you close this window, the program will
exit.

There is also an Explorer window, available from the "View"
menu. This window gives you an alternative view of data.
The view of the data that the window presents is
similar in structure to the directory structure used to hold
the data on the IPM. To view an object in the Explorer
window, double click the object. For example, to plot data from
an observatory using the Explorer window, expand the tree until
the observatory is listed, expand the observatory, select and
expand the data file that you want to view then double click
the "Data Plot" icon. The Explorer window also shows you which
databases the program is using. For more information about
databases see the online help system.

The third main window, also available from the "View" menu, is
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
between data formats (e.g. to convert INTERMAGNET minute mean
format to IAGA-2002), but please note that between import and
export the data will always be stored in IAF format and so the
precision of the data will be that provided by the IAF format
(1/10th nT and 1/10th minute of arc). For most modern data this
precision is unacceptably low, particularly for angular
measurements.

Prior to the current software, INTERMAGNET distributed a
DOS-based program for working with the IPM data. For
historical purposes this software is documented in |app_imag_cd|.

Copies of INTERMAGNET Physical Media may be obtained from:

| INTERMAGNET Physical Media (IPM) distribution office
| Observatoire Magnétique National
| Carrefour des 8 routes
| 45340 Chambon la Forêt
| FRANCE
| Tel: 33 (0) 2-38-33-95-01
| Internet: |contact_ipgp|

From 2015 onward, INTERMAGNET stopped the production of physical medias.
Definitive data is now published yearly with a Digital Object Identifier (DOI) see
:numref:`use_dat_imag_web_down_data_doi`.
Individual (monthly) IAF data files are available from the INTERMAGNET web site.
