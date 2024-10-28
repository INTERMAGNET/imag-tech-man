.. _app_imag_dir:

INTERMAGNET Physical Media Directory Structure
----------------------------------------------

The structure of files and folders on the INTERMAGNET
Physical Media (IPM) has remained broadly the same since its
inception in 1991, however there have been some differences.
This appendix documents the structure for the USB
(2014), then describes the structure of the DVD (2011) and the
first CD-ROM (1991) and lists year by year differences in the
files and folders on the INTERMAGNET Physical Media (IPM).

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



INTERMAGNET Physical Media Directory Structure
``````````````````````````````````````````````

The files on the INTERMAGNET Physical Media are set up in a
particular directory structure. The root directory contains a
"README.TXT" file, which is an ASCII file describing the
INTERMAGNET Physical Media and where to obtain information about it, the
software, and documentation; CD-ROMs from 1991-2004 also hold a
"README.EXE" file, which is an executable version of the
README.TXT file that allows the user to scroll back and forth
through the information. DVDs and USBs do not contain
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

List of Changes to the Structure since the first (1991) CD-ROM
``````````````````````````````````````````````````````````````

.. tabularcolumns:: |>{\centering\arraybackslash}p{1cm}|p{12cm}|

.. table::
    :class: longtable
    :widths: auto
    :align: center

    +-----------------------------------+-----------------------------------+
    | Year                              | Change                            |
    +===================================+===================================+
    | 1992                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 1993                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 1994                              | First CD-ROM with an ERRATA       |
    |                                   | folder in the root of the disk    |
    |                                   | IMAG21.EXE and INSTALL.EXE added  |
    |                                   | to the root of the CD-ROM         |
    +-----------------------------------+-----------------------------------+
    | 1995                              | Annual means included in a        |
    |                                   | YEARMEAN.obs file in each         |
    |                                   | observatory folder                |
    +-----------------------------------+-----------------------------------+
    | 1996                              | IMAG22.EXE replaces IMAG21.EXE    |
    |                                   |                                   |
    |                                   | PLOTUTIL folder added to the root |
    |                                   | of the CD-ROM containing plotting |
    |                                   | source code and executables (for  |
    |                                   | DOS)                              |
    +-----------------------------------+-----------------------------------+
    | 1997                              | No change                         |
    +-----------------------------------+-----------------------------------+
    | 1998                              | Republication of some data        |
    |                                   | (folders in root of CD-ROM):      |
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
    |                                   | include in CTRY_INF folder –      |
    |                                   | these are splash screens for      |
    |                                   | individual disks                  |
    +-----------------------------------+-----------------------------------+
    | 2001                              | Republication of some data        |
    |                                   | (folders in root of 1st CD-ROM    |
    |                                   | only):                            |
    |                                   |                                   |
    |                                   | - ABG 2000                        |
    |                                   |                                   |
    |                                   | Removed INTRO00A.PCX and          |
    |                                   | INTRO00B.PCX from CTRY_INF        |
    +-----------------------------------+-----------------------------------+
    | 2002                              | IMAG24.EXE replaces IMAG23.EXE    |
    |                                   |                                   |
    |                                   | Republication of some data        |
    |                                   | (folders in root of both          |
    |                                   | CD-ROMs):                         |
    |                                   |                                   |
    |                                   | - TAN 2001                        |
    |                                   |                                   |
    |                                   | INTRO1.PCX and INTRO2.PCX are     |
    |                                   | included in CTRY_INF folder       |
    +-----------------------------------+-----------------------------------+
    | 2003                              | Republication of some data        |
    |                                   | (folders in root of both          |
    |                                   | CD-ROMs):                         |
    |                                   |                                   |
    |                                   |                                   |
    |                                   | - FRN, HON 1993                   |
    |                                   | - HON 2001, 2002                  |
    |                                   | - PPT 2002                        |
    |                                   |                                   |
    +-----------------------------------+-----------------------------------+
    | 2004                              | Republication of some data        |
    |                                   | (folders in root of both          |
    |                                   | CD-ROMs):                         |
    |                                   |                                   |
    |                                   | - 2003 ABG, IQA, SJG              |
    |                                   |                                   |
    |                                   | A new UTILITY folder is put into  |
    |                                   | the root of the CD-ROM. It holds  |
    |                                   | software for working with the     |
    |                                   | data, including the first         |
    |                                   | distributed version (V1.1) of the |
    |                                   | imcdview viewing software in      |
    |                                   | CDVIEWER/CDVIEWER.JAR V1.1        |
    |                                   |                                   |
    |                                   | The OBSY_INF folder includes a    |
    |                                   | file OBS_V101.CSV – a list of     |
    |                                   | observatories used by imcdview    |
    +-----------------------------------+-----------------------------------+
    | 2005                              | Republication of some data        |
    |                                   | (folders in root of both CDs):    |
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
    |                                   | The UTILITY folder is removed     |
    |                                   | A SOFTWARE folder is added to the |
    |                                   | root of the CD-ROM. It contains   |
    |                                   | the CD viewer software,           |
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
    |                                   | from the CTRY_INF folder:         |
    |                                   | INTRO.PCX, INTRO1.PCX,            |
    |                                   | INTRO2.PCX, CTRYLIST.IDX          |
    |                                   | The OBSY_INFO folder is retained, |
    |                                   | but is empty                      |
    |                                   |                                   |
    |                                   | The IMAG24.EXE viewing software   |
    |                                   | and its associated files are      |
    |                                   | removed from the root of the disk |
    |                                   |                                   |
    |                                   | The XTRAS folder is removed       |
    +-----------------------------------+-----------------------------------+
    | 2006                              | Publication moves from two        |
    |                                   | CD-ROMs to a single DVD           |
    |                                   |                                   |
    |                                   | All graphics files are in PNG     |
    |                                   | format                            |
    |                                   |                                   |
    |                                   | The root of the DVD contains the  |
    |                                   | following folders and files:      |
    |                                   |                                   |
    |                                   | - AUTORUN.INF                     |
    |                                   | - ERRATA                          |
    |                                   | - MAG2006                         |
    |                                   | - README.TXT                      |
    |                                   | - SOFTWARE                        |
    |                                   |                                   |
    |                                   | The software folder contains the  |
    |                                   | imcdview visualisation software   |
    |                                   | along with a simple installer     |
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

.. note::

    Unless otherwise noted, where a change is shown in the structure,
    the change affects all years subsequent to the year where the
    change is described. The exception to this is republished data.

Republished data is put into a folder at the root of the
INTERMAGNET Physical Media. It is only put on for one year – the republished data
is not repeated on subsequent INTERMAGNET Physical Medias. Because the data is not
under the MAGyyyy folder, it will not be recognised by the
imcdview viewing software (where a number of years where
republished in a form that the software can access).

The OBSY_INF folder is present on all INTERMAGNET Physical Medias, though it
may be empty. It is used by software (along with the CTRY_INF and
yyyyMAPS folders) to indicate the presence of an INTERMAGNET Physical Media
folder structure.

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
