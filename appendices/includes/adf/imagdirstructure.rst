.. _app_imag_dir:

INTERMAGNET Definitive Data Media Directory Structure
-----------------------------------------------------

The structure of files and directories on the INTERMAGNET
Physical Media (IPM) and the INTERMAGNET Reference Data Set
(IRDS) has remained broadly the same since the first IPM
release for data in 1991, however some changes have been made.
This appendix gives pictorial representations of the structure for the 
IRDS (2020), the USB (2014), DVD (2011) and the
first CD-ROM (1991). A general description of the structure as it
applies to all years is followed by detailed descriptions of
the individual years in the pictorial representations and 
finaly a list of the year by year differences in the
files and directories on the IPM and the IRDS.


Structure of the IRDS (2020)
````````````````````````````

::

    .
    ├── mag1991_def2015.zip
    │   └── mag1991
    │       ├── 1991maps
    │       │   ├── all.png
    │       │   ├── aus.png
    │       │   ├── can.png
    │       │   ├── ...
    │       │
    │       ├── ctry_inf
    │       │   ├── ctrylist.idx
    │       │   ├── allsrn.pcx
    │       │   ├── aussrn.pcx
    │       │   ├── readme.all
    │       │   ├── readme.aus
    │       │   ├── ...
    │       │   
    │       ├── obsy_inf
    │       │   └── 91obsdat.dbf
    │       │
    │       ├── ams
    │       │   ├── ams91jan.bin
    │       │   ├── mas91feb.bin
    │       │   ├── ...
    │       │   ├── ams91k.dka
    │       │   └── readme.ams
    │       │
    │       ├── bfe
    │       │   └── ...
    │       ├── ...
    │       ├── xtras
    │       │   ├── prnstruc.exe
    │       │   └── structur.dat
    │       ├── readme.txt
    │       └── readme.exe
    │
    ├── mag1992_def2015.zip
    │   └── ...
    │ ...
    │
    ├── mag2020_def2020.zip
    │   └── mag2020
    │       ├── 2020maps
    │       ├── ctry_inf
    │       ├── abg
    │       │   ├── abg20jan.bin
    │       │   ├── abg20feb.bin
    │       │   ├── ...
    │       │   ├── abg20k.dka
    │       │   ├── abg2020.blv
    │       │   ├── readme.abg
    │       │   └── yearmean.abg
    │       ├── ...
    │
    ├── change_log_IRDS2020.txt
    └── readme_INTERMAGNET_IRDS2020.txt
    

Structure of the USB (2014)
```````````````````````````

::

    .
    ├── errata
    │    └── errata.txt
    ├── mag2014
    │   ├── 2014maps
    │   │    ├── alg.png
    │   │    ├── all.png
    │   │    ├── aus.png
    │   │    ├── ...
    │   │
    │   ├── ctry_inf
    │   │   ├── algsrn.png
    │   │   ├── aussrn.png
    │   │   ├── ...
    │   │   ├── readme.alg
    │   │   ├── readme.arg
    │   │   ├── ...
    │   │
    │   ├── aaa
    │   │   ├── aaa14jan.bin
    │   │   ├── aaa14feb.bin
    │   │   ├── ...
    │   │   ├── aaa14k.dka
    │   │   ├── aaa2014.blv
    │   │   ├── readme.aaa
    │   │   └── yearmean.aaa
    │   ├── ...
    │   └──obsy_inf
    ├── imcdview_install.txt
    ├── readme.txt
    └── software
        └── Disk1
            └── InstData
                ├── GenericUnix
                │   └──  IMCDView.bin
                ├── Linux_32
                │   │── NoVM
                │   │   └── IMCDView.bin
                │   └── VM
                │       └── IMCDView.bin
                ├── Linux_64
                │   │── NoVM
                │   │   └── IMCDView.bin
                │   └── VM
                │       └── IMCDView.bin
                ├── MacOSX
                │   │── NoVM
                │   │   └── IMCDView.bin
                │   └── VM
                │       └── IMCDView.bin
                ├── Solaris
                │   │── NoVM
                │   │   └── IMCDView.bin
                │   └── VM
                │       └── IMCDView.bin
                ├── Unix_with_VM
                │   └── VM
                │       └── IMCDView.bin
                ├── Windows_32_or_64_bit
                │   │── NoVM
                │   │   └── IMCDView.exe
                │   └── VM
                │       └── IMCDView.exe
                ├── Windows_Pure_64_bit
                │   │── NoVM
                │   │   └── IMCDView.exe
                │   └── VM
                │       └── IMCDView.exe
                ├── MediaId.properties
                └── Resource1.zip


Structure of (2011) DVD
```````````````````````

::

    .
    ├── errata
    │     └── errata.txt
    ├── mag2011
    │ 	├── 2011maps
    │ 	│   ├── alg.png
    │ 	│   ├── all.png
    │ 	│   ├── aus.png
    │ 	│   ├── ...
    │ 	│
    │   ├── ctry_inf
    │ 	│   ├── algsrn.png
    │ 	│   ├── aussrn.png
    │ 	│   ├── ...
    │ 	│   ├── readme.alg
    │ 	│   ├── readme.all
    │ 	│   ├── ...
    │ 	├── aaa
    │ 	│   ├── aaa11jan.bin
    │ 	│   ├── aaa11feb.bin
    │ 	│   ├── ...
    │ 	│   ├── aaa2011.blv
    │ 	│   ├── aaa11k.dka
    │ 	│   ├── readme.aaa
    │ 	│   └── yearmean.aaa
    │  	├── aae
    │ 	│   ├── aae11jan.bin
    │ 	│   ├── aae11feb.bin
    │ 	│   ├── ...
    │ 	│   ├── aae2011.blv
    │ 	│   ├── aae11k.dka
    │ 	│   ├── readme.aae
    │ 	│   └── yearmean.aae
    │ 	├── ...
    │ 	│
    │ 	└── obsy_inf
    ├── imcdview_install.txt
    ├── readme.txt
    └── software
        └── Disk1
            └── InstData
                ├── Linux
                │   └── NoVM
                │       └── IMCDView.bin
                ├── Mac
                │   └── NoVM
                │       └── IMCDView.app
                ├── MediaId.properties
                ├── Resource1.zip
                ├── Solaris
                │   └── NoVM
                │       └── IMCDView.bin
                └── Windows
                    └── NoVM
                        └── IMCDView.exe



Structure of first (1991) CD-ROM
````````````````````````````````

::

    .
    ├── MAG1991
    │ 	├── 1991MAPS
    │ 	│   ├── ALL.png
    │ 	│   ├── AUS.png
    │ 	│   ├── CAN.png
    │ 	│   ├── ...
    │ 	├── CTRY_INF
    │ 	│   ├── CTRYLIST.IDX
    │ 	│   ├── ALLSRN.PCX
    │ 	│   ├── AUSSRN.PCX
    │  	│   ├── README.ALL
    │ 	│   ├── README.AUS
    │ 	│   ├── ...
    │ 	└── OBSY_INF
    │ 	    └── 91OBSDAT.DBF
    ├── AMS
    │   ├── AMS91JAN.BIN
    │   ├── MAS91FEB.BIN
    │   ├── ...
    │   ├── AMS91K.DKA
    │   └── README.AMS
    ├── XTRAS
    │   ├── PRNSTRUC.EXE
    │   └── STRUCTUR.DAT
    ├── README.TXT
    └── README.EXE


.. _app_imag_dir_struct:

The Directory Structure
```````````````````````

The basics of the structure used to hold IPM and IRDS data are the 
same for all years. The structure is as follows:

- Each year of data is in a separate directory, called magYYYY.

- The data is held in subdirectories of the magYYYY directory, one
  subdirectory per observatory. The subdirectory names are the IAGA
  codes for each observatory. The subdirectory contents are
  described below.

- Within the magYYYY directory there are two or three directories for
  metadata, called YYYYmaps, ctry_inf and obsy_inf. The first two of
  these directories must exist (even if they are empty) for some software to
  recognise the directory as an INTERMAGNET definitive data directory.

- The YYYYmaps directory is empty in recent publications 
  (but must be present). In earlier publications it contained a 
  map for each contributing institute showing the location of the 
  institute's observatories, along with an overall map for the entire 
  INTERMAGNET network. The maps were in the form of PCX or PNG images.

- The ctry_inf directory is empty in recent publications 
  (but must be present). In earlier publications it contained:

  - A README text file for each country / institute.

  - An image for each country / institute

  - A overall README for the publication

- The obsy_inf directory is present on all INTERMAGNET Physical 
  Medias, though it may be empty. The directory is not present 
  in IRDS publications. On publications where it has contents, 
  a single file contains a database with metadata details 
  of each observatory in the publication.

Where:

- ``YYYY`` is the 4 digit year

In IPM publications, where there is only a single year of data,
there is also a README file in the top level directory which describes
the publication.

The IPM publications also contained software, documentation and
republication of data from previous years where there had been
an error in the data. These additons to the structure are
described in the detailed descriptions of individual years
further on in this section, but they are generally of limited
interest to users, since the IRDS has superceeded the need for
them.

The Observatory Subdirectories
""""""""""""""""""""""""""""""

Each observatory subdirectory has the same contents, which are:

#. ``magYYYY\SSS\SSSYYMMM.bin`` (12 binary files in IAF format)
#. ``magYYYY\SSS\readme.SSS`` (1 readme file)
#. ``magYYYY\SSS\SSSYYYY.blv`` (1 baseline file)
#. ``magYYYY\SSS\yearmean.SSS`` (1 annual means file)
#. ``magYYYY\SSS\SSSYYk.dka`` (1 text file of K-indices)

Where:

- ``YYYY`` is the 4 digit year
- ``YY`` is the 2 digit year
- ``SSS`` is the 3-letter observatory IAGA code
- ``MMM`` is the month
- ``CCC`` is the three-letter country code

#. Each binary file in IAF format (described in detail in :numref:`sub_dat_def_data`
   and |app_iaf|) includes minute values as well as
   other accompanying data such as: metadata headers, K indices,
   hourly and daily mean values.
#. The text file readme.SSS contains meta-data and information 
   about the observatory such as location, parent
   institute, personnel, equipment and instrumentation etc.
#. The text file SSSyyyy.blv contains results of absolute control
   of geomagnetic observations and adopted baseline values. The format of this file is
   described in |app_imag_ibf|. Baseline data are considered by
   many experts as an indicator of data quality, especially with regard to observation of
   secular variation.
#. The text file yearmean.SSS contains a listing of annual mean
   values for the observatory. The format of this file is
   described in |app_iyf|. Most observatories publish all
   annual means, i.e. since the beginning of their activity.
   Some observatories also publish annual means for international geomagnetic quiet-days
   and disturbed-days.
#. The text file SSSyyk.dka contains K-indices. DKA files are created by
   INTERMAGNET from the K index data included in binary IAF files. if K-indices are not 
   scaled by the IMO there is no DKA file.

The Year-Map Subdirectory
"""""""""""""""""""""""""

The YYYYmaps subdirectory has the following contents:

``magYYYY\YYYYmaps\CCC.xxx`` (1 map for each country (xxx = png or pcx))

Where:

``CCC`` is the three-letter country code

The image file CCC.xxx shows the location of observatories of a
given country.

The Country Information Subdirectory
""""""""""""""""""""""""""""""""""""

The ctry_inf subdirectory has the following contents:

#. ``magYYYY\ctry_inf\readme.CCC`` (1 readme-file for each country)
#. ``magYYYY\ctry_inf\CCCsrn.xxx`` (1 about-screen for each country (xxx = png or pcx))

Where:

- ``YYYY`` is the 4 digit year
- ``CCC`` is the three-letter country code

#. The text file readme.CCC provides information about
   parent institute(s) in a given country.
#. The image file CCCsrn.xxx provides information about parent institute(s)
   managing IMOs in a given country in graphical form.
#. The ctry_inf subdirectory also holds a readme.all file with an overall description
   of the publication.


Modifications for the IRDS
``````````````````````````

This section describes how the IRDS data differs from the structure described in
the previous section. It references the IRDS 2020, as an example, which, like all 
IRDS publications, is available as a download from GFZ Data Services: 
`INTERMAGNET 2020 DOI`_.

On the download page for the DOI you will see a list of files. There are
two text files:

- change_log_IRDS2020.txt describes the changes that have been made to the
  IRDS since the previous publication

- readme_INTERMAGNET_IRDS2020.txt replaces the README.txt file described
  in the previous section and describes the publication.

Each of the remaining files is a compressed data file in ZIP format,
containing one year of data. File names are formatted in the form mag<year>_def<year>.zip.
The mag<year> section of the filename describes the year in which the data was
recorded. The def<year> section of the filename describes the most recent annual
INTERMAGNET publication in which the data was updated. Files where mag<year> = def<year>
have had no corrections since their original publication. For example, "mag2015_def2019.zip"
indicates that this file is different from the first release "mag2015_def2015.zip".

Each zip file contains a single directory mag<year>. The contents of this directory are
as described in the previous section, i.e. an empty <year>maps directory, an empty 
ctry_inf directory and a directory for each observatory that contributed data. 

After unzipping the archive, data can be accessed using INTERMAGNETs imcdview software 
available for downloaded from the web site : |imag_software|. Moving all the unzipped mag<year> 
directories into a single parent directory will allow imcdview to load them as a single
database, making it quicker to configure access to the data.
See :numref:`use_dat_data_view` for more info on the usage of this Data Viewer.


Detailed description of the 2011 DVD
````````````````````````````````````

This section describes the structure of the 2011 DVD, by way of an example,
since all other years of IPM data are structured 
in a similar way.

The files are presented in a fixed
directory structure. The root directory contains a "README.TXT"
file, which is an ASCII file describing the DVD and where to
obtain information about it, the software, and documentation;

On the 2011 DVD there are also three directories and a further
file. The directory called "ERRATA" contains a file
"ERRATA.TXT". This file lists errors on previous IPMs. A
second directory, called "SOFTWARE", holds the "imcdview"
programme, software, for visualizing and working with the data.
This software is described in :numref:`use_dat_data_view`
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
subdirectory is empty. It used to be required to identify to software
that the this directory holds data in the IRDS
structure.

The individual sub-directories (e.g. BFE for Brorfelde, TUC for
Tucson, etc.) contain the 12 months of 1-minute data labeled with the
3-letter ID, 2-character year, 3-letter month abbreviation, and
a "BIN" extension indicating they are binary files in the IAF
format (see  |app_iaf|).
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


Detailed description of the 1991 CD
```````````````````````````````````

The root directory contains a
README file ("README.TXT" on the IPM publications, 
"readme_INTERMAGNET_IRDS<year>.txt" on the IRDS publications), 
which is an ASCII file describing the data
and where to obtain information about it, the
software, and documentation. CD-ROMs from 1991-2004 also hold a
"README.EXE" file, which is an executable version of the
README.TXT file that allows the user to scroll back and forth
through the information. DVDs, USBs and the IRDS do not contain
README.EXE.

On the 1991 CD-ROM there are also two sub-directories. One is
labelled "XTRAS", and the other "MAG1991". The XTRAS directory
contains one file labeled "STRUCTUR.DAT", and another
"PRNSTRUC.EXE". The STRUCTUR.DAT file provides a schematic of
the data structure for the records on the CD-ROM and the
PRNSTRUC.EXE file enables the user to obtain a printout of that
record structure.

The MAG1991 directory contains a sub-directory for each
observatory identified by its 3-letter ID code. In addition,
there are sub-directories labeled "1991MAPS", "CTRY_INF", and
"OBSY_INF". The 1991MAPS directory contains the \*.PCX files
that are the map images of each country for use in the access
software. These are labeled by a 3-letter country ID with the
PCX extension, and one labeled "ALL.PCX" for the "All
Countries" option. The CTRY_INF directory contains a
"CTRYLIST.IDX" file that is used internally, \*.PCX files for
each country (and one for ALL) that are the images used to show
the flag and organizational Logo for the different countries,
and the README files that pertain to each country's
geomagnetism program (including a README for the ALL option).
The OBSY_INF subdirectory contains a "91OBSYDAT.DBF" file that
is used internally in the software. Since 2006 .pcx and .gif
graphic fiels have been replaced with .png files. It concerns
both maps in YYYYMAPS and About-screen images in CTRY_INF,
where YYYY is the 4-character year value.

The individual sub-directories (e.g. BFE for Brorfelde, TUC for
Tucson, etc.) contain the 12 months of data labeled with the
3-letter ID, 2-character year, 3-letter month abbreviation, and
a "BIN" extension indicating they are binary files. For
example, "BFE91AUG.BIN" is a file of 31 sequential day-records
for Brorfelde, for 1991, for August. In addition, there are the
"README.XXX" files for the individual observatory, where the
XXX indicates the 3-letter observatory ID.

This sub-directory may also contain a file labeled as
XXXYRK.DKA, where the XXX is the 3-letter observatory ID, the
YR is the 2-character year value and the K indicates a K-Index
file. Originally the DKA extension was used to indicate that
the data were generated from a digital algorithm in an ASCII
format, however subsequently these files have been used to hold
both digitally derived and hand-scaled K indices. Since 2005
the DKA files have been created by INTERMAGNET, using data from
the binary IAF file (before 2005 these files were provided by
the observatories). The consequence is that DKA ASCII files
provided by IMOs are ignored during final compilation of
INTERMAGNET Physical Media. These ASCII K-Index files are published on,
even though the data are in the binary records, because they
are much faster to access than paging through the binary
records on the INTERMAGNET Physical Media.


.. _app_imag_dir_struct_changes:

List of Changes to the Structure since the first (1991) CD-ROM
``````````````````````````````````````````````````````````````

.. tabularcolumns:: |>{\centering\arraybackslash}p{1cm}|p{12cm}|

.. table::
    :class: longtable
    :widths: auto
    :align: center

    +-----------------------------------+-----------------------------------+
    | Year                              | Initial publication               |
    +===================================+===================================+
    | 1992                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 1993                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 1994                              | First CD-ROM with an ERRATA       |
    |                                   | directory in the root of the disk |
    |                                   | IMAG21.EXE and INSTALL.EXE added  |
    |                                   | to the root of the CD-ROM         |
    +-----------------------------------+-----------------------------------+
    | 1995                              | Annual means included in a        |
    |                                   | YEARMEAN.obs file in each         |
    |                                   | observatory directory             |
    +-----------------------------------+-----------------------------------+
    | 1996                              | IMAG22.EXE replaces IMAG21.EXE    |
    |                                   |                                   |
    |                                   | PLOTUTIL directory added to the   |
    |                                   | root of the CD-ROM containing     |
    |                                   | plottingsource code and           |
    |                                   | executables (for DOS)             |
    +-----------------------------------+-----------------------------------+
    | 1997                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 1998                              | Republication of some data        |
    |                                   | (directories in root of CD-ROM):  |
    |                                   |                                   |
    |                                   | - CLF 1996                        |
    |                                   | - PPT, THY 1991                   |
    |                                   |                                   |
    +-----------------------------------+-----------------------------------+
    | 1999                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 2000                              | 1st year of distribution on 2     |
    |                                   | CD-ROMs (the number of            |
    |                                   | observatories meant that the data |
    |                                   | was too large to fit on a single  |
    |                                   | CD-ROM)                           |
    |                                   | IMAG23.EXE replaces IMAG22.EXE    |
    |                                   |                                   |
    |                                   | INTRO00A.PCX and INTRO00B.PCX are |
    |                                   | include in CTRY_INF directory –   |
    |                                   | these are splash screens for      |
    |                                   | individual disks                  |
    +-----------------------------------+-----------------------------------+
    | 2001                              | Republication of some data        |
    |                                   | (directories in root of 1st       |
    |                                   | CD-ROM only):                     |
    |                                   |                                   |
    |                                   | - ABG 2000                        |
    |                                   |                                   |
    |                                   | Removed INTRO00A.PCX and          |
    |                                   | INTRO00B.PCX from CTRY_INF        |
    +-----------------------------------+-----------------------------------+
    | 2002                              | IMAG24.EXE replaces IMAG23.EXE    |
    |                                   |                                   |
    |                                   | Republication of some data        |
    |                                   | (directories in root of both      |
    |                                   | CD-ROMs):                         |
    |                                   |                                   |
    |                                   | - TAN 2001                        |
    |                                   |                                   |
    |                                   | INTRO1.PCX and INTRO2.PCX are     |
    |                                   | included in CTRY_INF directory    |
    +-----------------------------------+-----------------------------------+
    | 2003                              | Republication of some data        |
    |                                   | (directories in root of both      |
    |                                   | CD-ROMs):                         |
    |                                   |                                   |
    |                                   |                                   |
    |                                   | - FRN, HON 1993                   |
    |                                   | - HON 2001, 2002                  |
    |                                   | - PPT 2002                        |
    |                                   |                                   |
    +-----------------------------------+-----------------------------------+
    | 2004                              | Republication of some data        |
    |                                   | (directories in root of both      |
    |                                   | CD-ROMs):                         |
    |                                   |                                   |
    |                                   | - 2003 ABG, IQA, SJG              |
    |                                   |                                   |
    |                                   | A new UTILITY directory is put    |
    |                                   | into the root of the CD-ROM. It   |
    |                                   | holds software for working with   |
    |                                   | the data, including the first     |
    |                                   | distributed version (V1.1) of the |
    |                                   | imcdview viewing software in      |
    |                                   | CDVIEWER/CDVIEWER.JAR V1.1        |
    |                                   |                                   |
    |                                   | The OBSY_INF directory includes a |
    |                                   | file OBS_V101.CSV – a list of     |
    |                                   | observatories used by imcdview    |
    +-----------------------------------+-----------------------------------+
    | 2005                              | Republication of some data        |
    |                                   | (directories in root of both      |
    |                                   | CDs):                             |
    |                                   |                                   |
    |                                   | - 2003 NVS                        |
    |                                   | - 2004 WNG                        |
    |                                   |                                   |
    |                                   | Filenames on the CD-ROMs are now  |
    |                                   | in lowercase (this documentation  |
    |                                   | will continue to show filename in |
    |                                   | uppercase for clarity)            |
    |                                   |                                   |
    |                                   | GIF files are used for some       |
    |                                   | graphics files (alongside PCX)    |
    |                                   |                                   |
    |                                   | The UTILITY directory is removed  |
    |                                   | A SOFTWARE directory is added to  |
    |                                   | the root of the CD-ROM. It        |
    |                                   | contains the CD viewer software,  |
    |                                   | imcdview.jar V1.2 and associated  |
    |                                   | installer software                |
    |                                   |                                   |
    |                                   | An AUTORUN.INF file is added to   |
    |                                   | the root of the CD-ROM to run the |
    |                                   | imcdview installer when the disk  |
    |                                   | is inserted (only works on        |
    |                                   | Windows operating systems)        |
    |                                   |                                   |
    |                                   | The following files are removed   |
    |                                   | from the CTRY_INF directory:      |
    |                                   | INTRO.PCX, INTRO1.PCX,            |
    |                                   | INTRO2.PCX, CTRYLIST.IDX          |
    |                                   | The OBSY_INFO directory is        |
    |                                   | retained, but is empty            |
    |                                   |                                   |
    |                                   | The IMAG24.EXE viewing software   |
    |                                   | and its associated files are      |
    |                                   | removed from the root of the disk |
    |                                   |                                   |
    |                                   | The XTRAS directory is removed    |
    +-----------------------------------+-----------------------------------+
    | 2006                              | Publication moves from two        |
    |                                   | CD-ROMs to a single DVD           |
    |                                   |                                   |
    |                                   | All graphics files are in PNG     |
    |                                   | format                            |
    |                                   |                                   |
    |                                   | The root of the DVD contains the  |
    |                                   | following directories and files:  |
    |                                   |                                   |
    |                                   | - AUTORUN.INF                     |
    |                                   | - ERRATA                          |
    |                                   | - MAG2006                         |
    |                                   | - README.TXT                      |
    |                                   | - SOFTWARE                        |
    |                                   |                                   |
    |                                   | The software directory contains   |
    |                                   | the imcdview visualisation        |
    |                                   | software along with a simple      |
    |                                   | installer                         |
    +-----------------------------------+-----------------------------------+
    | 2007                              | A multi-OS “Install Anywhere”     |
    |                                   | installer is included for the     |
    |                                   | imcdview visualisation software.  |
    |                                   |                                   |
    |                                   | A Java Virtual Machine is no      |
    |                                   | longer required to run the        |
    |                                   | software, as this is include on   |
    |                                   | the DVD                           |
    +-----------------------------------+-----------------------------------+
    | 2008                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 2009                              | A major republication of data     |
    |                                   | from years 2005, 2006, 2007 and   |
    |                                   | 2008                              |
    |                                   |                                   |
    |                                   | The AUTORUN.INF file is removed   |
    |                                   | from the root of the DVD          |
    |                                   |                                   |
    |                                   | The IMCDVIEW_INSTALL.TXT file is  |
    |                                   | added to the root of the DVD      |
    +-----------------------------------+-----------------------------------+
    | 2010                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 2011                              | Publication physical maps instead |
    |                                   | of political country maps         |
    +-----------------------------------+-----------------------------------+
    | 2012                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 2013                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 2014                              | Publication moves from DVD to USB |
    |                                   | drive                             |
    +-----------------------------------+-----------------------------------+
    | 2015                              | Final physical publication        |
    |                                   | including all data from 1991 to   |
    |                                   | 2015                              |
    +-----------------------------------+-----------------------------------+
    | 2015                              | First IRDS DOI                    |
    |                                   | including all data from 1991 to   |
    |                                   | 2015. New ways of republishing    |
    |                                   | data.                             |
    +-----------------------------------+-----------------------------------+
    | 2016                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 2017                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 2018                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 2019                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 2020                              | No change                         |
    +-----------------------------------+-----------------------------------+

.. note::

    Unless otherwise noted, where a change is shown in the structure,
    the change affects all years subsequent to the year where the
    change is described. The exception to this is republished data.

Republished data
""""""""""""""""

In the IPM (physical publications from 1992 to 2015)
republished data is put into a directory at the root of the
INTERMAGNET Physical Media. It is only put on for one year – the republished data
is not repeated on subsequent INTERMAGNET Physical Media publications. Because the data is not
under the magYYYY directory, it will not be recognised by the
imcdview viewing software (where a number of years were
republished in a form that the software can access).

The IRDS republishes data by overwriting the previous data in the MAGyyyy
directories, so that the new data is recognised by the imcdview software. So that
it is clear when data has been republished (and to reduce the size of the
archive), the magYYYY directories, so that the new data is recognised by the imcdview software. So that
are compressed into magYYYY_defZZZZ.zip files,
where ZZZZ represents the year in which the data was last (re)published.

Other changes
"""""""""""""

The .com and .exe files on earlier CD-ROMs are programs that were
designed to run on Microsoft DOS operating system. They will not
work on more recent versions of Microsoft Windows.

The IMAGxx.EXE files on earlier CD-ROMs contained software to view
the data on the CD-ROM. This software only ran on Microsoft DOS
operating system. This has been superseded by a
multi-operating-system program for viewing the data (imcdview, the
INTERMAGNET CD viewer).

The .PCX files, that preceded the current .GIF and .PNG files, are
graphics files. PCX stands for PiCture eXchange, a format created
by the ZSoft corporation. PCX is no longer in widespread use.
Convertors from PCX to more modern formats are available online.

The CTRYLIST.IDX file (no longer used on the DVD/USB) is a text
list of countries and their 3 letter codes.

The yyOBSDAT.DBF file (no longer used on the DVD/USB) is a
database listing the contents of the CD-ROM. This was used by the
DOS-based IMAGxx software (but is not used by the more recent
imcdview software). The database is in Dbase format.
