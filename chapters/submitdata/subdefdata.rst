.. _sub_dat_def_data:

Submission of Definitive Data
=============================

.. include:: ../../shared/variables.rst
.. include:: ../../shared/targets.rst
.. include:: ../../appendices/appendices.rst

An observatory sends definitive 1-minute to INTERMAGNET annually.
A "call for data" is made by INTERMAGNET early in the calendar
year for definitive data from the previous year. Insitutes
are requested to provide their data as soon as possible in
the new year and may send it before the call for data is made.

Since 2014 INTERMAGNET has also requested observatories to provide
1-second definitive data, if they are able to do so. It is not a  
requirement of INTERMAGNET membership that an observatory is able to 
provide 1-second data. Where possible, observatories should produce
data that complies with the INTERMAGNET 1-second data standard
(see :numref:`Chapter %s <1sec_imo>`). At present observatories
are requested to provide baseline corrected 1-second definitive
data whether or not it conforms to the standard, though
this is likely to change in the future as more observatories
become able to meet the standard. INTERMAGNET is currently developing 
recommendations on how to produce 1-second definitive data that will 
conform to the standard.


Submitting data
---------------

When to submit data
```````````````````

Definitive data for an IMO are to be provided to
INTERMAGNET shortly after the end of each calendar year, for
inclusion in the annual data publication. INTERMAGNET will send
out a "call for data" by email to each observatory. The distribution
list |imag_imo_email| is used to send the email. The subject of this email
traditionally starts with the words "Call for Data". The
request includes a submission date for both 1-minute and 1-second
data, by which time data must be
received at the Paris GIN ftp server (usually this deadline is
six months after the end of the year in which the data were
recorded). If an IMO misses the deadline:

- Only definitive data accepted before the publication
  deadline (specified by the Operations committee) will be
  included in the annual data publication.
- Definitive data delivered after this publication deadline
  will be published on the INTERMAGNET web site and in subsequent
  data publications.
- Any corrections to definitive data will also be published on
  the INTERMAGNET web site and in subsequent data publications.


How to submit data
``````````````````

The institute responsible for an IMO must deliver a complete set of
one-minute definitive data (this includes de-spiking, filling gaps where
possible, correcting baselines, and applying other processing
procedures). The baselines for one-minute definitive data must
also be included in the annual definitive data submissions, as 
should a file containing annual mean values for the currect and
previous years. Where possible institutes 
are also encouraged to submit one-second definitive data.

The following files should be put on the Paris ftp server:

.. tabularcolumns:: |p{4cm}|p{6cm}|p{5cm}|

.. table::
    :widths: auto
    :align: center

    +------------+--------------------------------------------------------------+--------------------------------------+
    | Required   | Type of data                                                 | Format                               |
    | number     |                                                              |                                      |
    | of         |                                                              |                                      |
    | files      |                                                              |                                      |
    +============+==============================================================+======================================+
    | 12         | Definitive one minute data, oriented XYZG, 1 per month       | Intermagnet Archive Format -         |
    |            |                                                              | see |app_iaf|                        |
    +------------+--------------------------------------------------------------+--------------------------------------+
    | 1          | Baseline values file                                         | Intermagnet Baseline Values Format - |
    |            |                                                              | see |app_imag_ibf|                   |
    +------------+--------------------------------------------------------------+--------------------------------------+
    | 1          | Yearmean file listing annual mean values for the observatory | Intermagnet Year-Mean File Format -  |
    |            |                                                              | see |app_iyf|                        |
    +------------+--------------------------------------------------------------+--------------------------------------+
    | 1          | "Readme" file describing the observatory                     | ASCII/Unicode text file              |
    +------------+--------------------------------------------------------------+--------------------------------------+
    | 1 [#a]_    | "Readme" file describing the institute/country               | ASCII/Unicode text file              |
    +------------+--------------------------------------------------------------+--------------------------------------+
    | 1 [#a]_    | "About" image describing the institute/country               | PNG image file                       |
    |            | (the country's "About" screen)                               |                                      |
    +------------+--------------------------------------------------------------+--------------------------------------+
    | 1 [#a]_    | Map image showing a map of the institute's/country's         | PNG image file                       |
    |            | observatories.                                               |                                      |
    +------------+--------------------------------------------------------------+--------------------------------------+
    | 12 [#b]_   | Definitive one second data (if one second data is            | Intermagnet CDF Format -             |
    |            | being contributed for the observatory), 1 per month          | see |app_cdf|                        |
    +------------+--------------------------------------------------------------+--------------------------------------+

.. [#a] For each of these items please state whether you want:

#. To use the same file as the previous year.
#. To make changes to the previous year's file (in which case
   please describe the changes).
#. To use a new file (in which case please put the new file on
   the server).

.. [#b] One second data is encouraged, but not required.

TODO: Jan/Roman - please check this is accurate and correct?

TODO: Are the "about" and map images needed/accepted any more?

Observatories should provide 1-minute definitive data
in the INTERMAGNET Archive Format (IAF) which is described in
|app_iaf|. Data can be converted to IAF using INTERMAGNET’s
"imcdview" data visualisation software, "gm_convert" data
conversion software or "MagPy" analysis and display software.
Institutes chosing to contribute 1-second
data should provide the data in Intermagnet CDF Format (ImagCDF) 
which is described in |app_cdf|. Data can be converted to ImagCDF 
using the "gm_convert" or MagPy software. These software products can be
obtained from  |imag_software|.

Please note the following:

- The total field element Fs included in the binary files, used
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
- Images must be in PNG format. Other formats are not accepted.

One of the main objectives of INTERMAGNET is to process
definitive data as fast as possible and to make these data
available to users. To facilitate this, institutes should send
their definitive data in the INTERMAGNET binary data formats as
well as accompanying files by ftp to the
Paris GIN’s ftp server as soon as possible and before the data
submission deadline which is set by the INTERMAGNET operations
committee:

-  Host name: |gin_paris|
-  User name: userint
-  Password can obtained from the Paris GIN manager (|contact_par_gin_manager|)
   or the chair of the Definitive Data Subcommittee (|contact_subcom_defdat|).

Once the data have been put on this server, INTERMAGNET then:

-  Checks the data for problems.
-  Ingests the minute data into the INTERMAGNET Web site.
-  Copies the data to the World Data Centre Edinburgh
-  Publishes the data under a DOI. The data is hosted at `GFZ data services`_.
   Entering "Intermagnet" in the search box on this page will show all
   INTERMAGNET definitive data DOIs.


.. _sub_dat_def_data_check:

Checking Procedure
------------------

Institutes must prepare definitive data with extreme care. The
data are distributed widely. Publishing corrections to this
data set is a very difficult task.

The data checking method is left to individual institutes.
However software tools are available which can help in the
preparation and checking of data. These tools are available
from the Internet (see :numref:`sub_dat_def_data_soft` for details).
The descriptions in this part of the Technical Manual mainly refer to
the imcdview program (imcdview is visualisation software for 
INTERMANGET definitive data), but other tools, such as MagPy, can also
be used. Links to all the software used in Intermagnet are
available from INTERMAGNET web site's software page: |imag_software|

When an observatory wants to check data before submission,
it is necessary to create a directory structure on disk similar 
to the structure of the INTERMAGNET Reference Data Set (IRDS).
This will allow the user to use the
imcdview software to view the data. A complete annual INTERMAGNET 
data structure includes the following folders and files:

#. ``DDD\\magYYYY\\SSS\\SSSYYMMM.bin`` (12 binary files in IAF format)
#. ``DDD\\magYYYY\\SSS\\SSSYYYY.blv`` (1 baseline file)
#. ``DDD\\magYYYY\\SSS\\yearmean.SSS`` (1 annual means file)
#. ``DDD\\magYYYY\\SSS\\readme.SSS`` (1 readme file for the observatory)
#. ``DDD\\magYYYY\\ctry_inf\\readme.CCC`` (1 readme-file for each country)
#. ``DDD\\magYYYY\\ctry_inf\\CCCsrn.png`` (1 about-screen image for each country)
#. ``DDD\\magYYYY\\YYYYmaps\\CCC.png`` (1 map image for each country)
#. ``DDD\\magYYYY\\SSS\\SSS_YYYYMM_pt1s_4.cdf`` (12 binary files in ImagCDF format,
   if one second data is being contributed for the observatory)

Where:

  - ``DDD`` is the base folder for the data, which can be any folder in the filesystem
  - ``YYYY`` is the 4 digit year and century
  - ``YY`` is the 2 digit year
  - ``SSS`` is the 3-letter observatory code
  - ``MMM`` is the 3 character month name ('jan', 'feb', 'mar', 'apr', may',
    'jun', 'jul', 'aug', 'sep', 'oct', 'nov' or 'dec')
  - ``MM`` is the 2 digit month number ('01' to '12')
  - ``CCC`` is the country code

In order for imcdview to recognize that a directory contains
INTERMAGNET data, the subdirectories ctry_inf and YYYYmaps are
needed even if they are empty. For more information see
|app_imag_dir|.

The same structure is also required 
by most of the other programs used to check data.

Before putting INTERMAGNET files on the Paris GIN ftp server,
institutes must perform the following as a minimum set of
tests:

#. Review the whole year of binary data. Software for this
   action:

   #. **imcdview, imagplot.exe**

      The imcdview software allows users
      to display data in both graphics (plots) and text modes.

   #. **imagplot.exe**

      The imagplot.exe works under Windows and allows users to
      create PostScript plots.

#. Check for any discrepancies between Fvector (Fv total field
   calculated on the basis of XYZ elements) and Fscalar (Fs
   recorded by means of proton magnetometer) for minute values.
   The resource that can be used to make this check is imcdview
   Java browser.

#. If submitting one second data, check for discrepancies between
   the one minute and one second data. The imcdview Java browser
   provides a way of making this comparison.

#. Check the binary data headers and the consistency of the
   binary data with the yearmean baseline, and readme files.
   Software for this action: check1min.exe

   The program check1min.exe checks the headers of the binary
   one minute data. It also checks whether recent yearly mean values
   included in the yearmean.sss file are consistent with the 12
   binary files, i.e. whether annual means included in the
   yearmean file agree with annual means calculated from the
   binary data. Please remember that for XYZG orientation the
   D-conversion factor should be set to exactly 10000.

   The program also checks for discrepancies between elements
   XYZFIDH, and also detects format errors.

#. K-indices
   Software: The imcdview software includes, among
   other things, a "K index Viewer".

   .. note::

     Program Kasm.exe, available on the INTERMAGNET web site,
     allows users to insert K-index data into IAF binary files.
     The program uses the "Adaptive Smoothing" method to create
     the indices.

#. Inspection of the BLV file

   Software for this action is also imcdview. The program 
   allows viewing of baseline data and creation of PNG or PDF
   plots from the baseline values in the SSSYYYY.BLV files

#. Inspection of readme files

   Readme files can be checked using any text editor, though an
   editor which can display non-printing characters (except Cr
   Lf), which should not be in readme and other text files, and
   gives easy control of line length is preferred. The contents
   of readme files can also be seen using imcdview.

#. Inspection of CDF binary files

   The CDF software (available from NASA at |cdf_format| )
   includes the programs "cdfdump" and "cdfedit" which can be used to
   inspect and update CDF data files.

   The Autoplot program (|autoplot|) can be used to create
   plots of the data in CDF data files.

.. _sub_dat_def_data_soft:

Obtaining the Checking Software
```````````````````````````````

See the following web page to download the checking software:
|imag_software|

