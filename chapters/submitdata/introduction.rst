.. _sub_dat_intro:

Introduction
============

.. include:: ../../appendices/appendices.rst
.. include:: ../../shared/variables.rst


Observatories send their data to INTERMAGNET via two different
routes. For preliminary data products (all types of
non-definitive data including quasi-definitive), each
observatory is assigned to a Geomagnetic Information Node
(GIN). Observatories send their preliminary data to their
assigned GIN in ‘near real-time’, i.e. as soon as possible
after recording. The process is designed to be automated, so
that observatories can upload data to INTERMAGNET as part of
their automatic data recording or processing systems. Multiple
transmissions of preliminary data are possible, where an
observatory is refining the quality of the data shortly after
recording. The GIN is responsible for forwarding this data to
the INTERMAGNET web site for onward distribution to users. The
INTERMAGNET web site is the only place where users have access
to data from INTERMAGNET observatories. Observatories send
their definitive data to the ftp site of the Paris GIN. This
process is expected to be manual and only done once a year
(unless there are problems with the data that require
resubmission).

.. _sub_dat_intro_df:

Data Formats
------------

A number of data formats are in use in INTERMAGNET. In some
cases this diversity exists to support handling of different
types of data, in other cases a new format has superseded (or
partially superseded) an older one.


IMFV1.23 GIN Dissemination Format
`````````````````````````````````

.. tabularcolumns:: |p{3.5cm}|p{9cm}|

.. table::
    :widths: auto
    :align: center

    +---------------------+-----------------------------------------------+
    | Data type supported | Notes                                         |
    +=====================+===============================================+
    | Minute mean values  | GINs continue to support this format, but     |
    |                     | INTERMAGNET no longer distributes data in     |
    |                     | IMFV1.23.                                     |
    |                     |                                               |
    |                     | Observatories are encouraged to use           |
    |                     | the IAGA-2002 format instead.                 |
    +---------------------+-----------------------------------------------+

This format is fully defined in |app_imag_imfv_1|.

IMFV2.83 Satellite Transmission Format
``````````````````````````````````````
.. tabularcolumns:: |p{6cm}|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +---------------------+-----------------------------------------------+
    | Data type supported | Notes                                         |
    +=====================+===============================================+
    | Minute mean values  | A format designed to transport compressed     |
    |                     | data via GOES and METEOSAT satellites.        |
    +---------------------+-----------------------------------------------+

This format is fully defined in |app_imag_imfv_2|.

IAGA-2002
`````````
.. tabularcolumns:: |p{6cm}|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +----------------------------------+----------------------------------+
    | Data type supported              | Notes                            |
    +==================================+==================================+
    | Any regular time-series          | The preferred format for         |
    | geomagnetic data                 | submission of preliminary data.  |
    +----------------------------------+----------------------------------+

This format is fully defined in |app_iaga_2002|.

INTERMAGNET Archive Format
``````````````````````````
.. tabularcolumns:: |p{6cm}|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +----------------------------------+----------------------------------+
    | Data type supported              | Notes                            |
    +==================================+==================================+
    | Definitive and quasi-definitive  | The required format for          |
    | minute, hourly, daily values and | submission of definitive data.   |
    | K-indices                        | Primarily used in the annual     |
    |                                  | INTERMAGNET Reference Data       |
    |                                  | Set (IRDS).                      |
    +----------------------------------+----------------------------------+

This format is fully defined in |app_iaf|.

ImagCDF
```````

.. tabularcolumns:: |p{5cm}|p{9cm}|

.. table::
    :widths: auto
    :align: center

    +------------------------------+--------------------------------------+
    | Data type supported          | Notes                                |
    +==============================+======================================+
    | High precision 1-second data | A new (2016) format for submission   |
    |                              | of 1-second definitive data.         |
    +------------------------------+--------------------------------------+

This format is fully defined in |app_cdf|.

IYF INTERMAGNET Year-Mean File
``````````````````````````````
.. tabularcolumns:: |p{3.5cm}|p{9cm}|

.. table::
    :widths: auto
    :align: center

    =================== ================================================
    Data type supported Notes
    =================== ================================================
    Annual mean values  Primarily used in the IRDS.
    =================== ================================================

This format is fully defined in |app_iyf|.

IBF INTERMAGNET Baseline File
`````````````````````````````
.. tabularcolumns:: |p{7cm}|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +----------------------------------+----------------------------------+
    | Data type supported              | Notes                            |
    +==================================+==================================+
    | Baseline values and absolute     | Primarily used in the IRDS.      |
    | observation data                 |                                  |
    +----------------------------------+----------------------------------+

This format is fully defined in |app_imag_ibf|.


.. _sub_dat_intro_dt:

Data Types
----------

Geomagnetic data is refined over time as the various sources
from which it is composed are recorded, combined and verified.
Data type in this context describes the state that a set of
data values have reached in the process of being published,
from raw data which is read directly from one or more sensors
to definitive data which is the final product of an observatory
to which no further changes are expected. The data formats used
with time-series geomagnetic data include (or imply) a data
type field in their metadata. This data type field is explained
below.

.. tabularcolumns:: |p{3cm}|p{6cm}|p{6cm}|

.. table::
    :widths: auto
    :align: center

    +------------------+------------------------+------------------------+
    | Data type        | Formats where it can   | What it means          |
    |                  | be used                |                        |
    +==================+========================+========================+
    | Reported         | IMFV1.23               | Preliminary data from  |
    |                  | (as a metadata field)  | an observatory that    |
    |                  |                        | has not had any        |
    |                  | IMFV2.83 (implied –    | baseline corrections   |
    |                  | data in this format    | applied. It may        |
    |                  | can only be            | contain spikes and may |
    |                  | ‘Reported’).           | have missing values.   |
    |                  |                        |                        |
    +------------------+------------------------+------------------------+
    | Variation        | IAGA-2002 (as a        | The data type is not   |
    |                  | metadata field)        | defined in the format  |
    |                  |                        | definition.It is       |
    |                  |                        | assumed to contain     |
    |                  |                        | data to the same       |
    |                  |                        | definition as the      |
    |                  |                        | ‘Reported’ data type.  |
    +------------------+------------------------+------------------------+
    | Adjusted         | IMFV1.23 (as a         | Adjusted data may have |
    |                  | metadata field)        | modifications made to  |
    |                  |                        | raw data to apply      |
    |                  |                        | baselines, remove      |
    |                  |                        | spikes or fill gaps.   |
    +------------------+------------------------+------------------------+
    | Provisional      | IAGA-2002 (as a        | The data type is not   |
    |                  | metadata field)        | defined in the format  |
    |                  |                        | definition. It is      |
    |                  |                        | assumed to contain     |
    |                  |                        | data to the same       |
    |                  |                        | definition as the      |
    |                  |                        | ‘Adjusted’ data type.  |
    +------------------+------------------------+------------------------+
    | Quasi-definitive | IMFV1.23, IAGA-2002    | Quasi-definitive data  |
    |                  | and IAFV2.11           | are defined as data    |
    |                  |                        | that have been         |
    |                  |                        | corrected using        |
    |                  | (as a metadata field)  | provisional baselines. |
    |                  |                        | Produced soon after    |
    |                  |                        | data acquisition,      |
    |                  |                        | their accuracy is      |
    |                  |                        | intended to be very    |
    |                  |                        | close to that of an    |
    |                  |                        | observatory’s          |
    |                  |                        | definitive data        |
    |                  |                        | product. 98% of the    |
    |                  |                        | differences between    |
    |                  |                        | quasi- definitive and  |
    |                  |                        | definitive data        |
    |                  |                        | monthly mean values    |
    |                  |                        | should be less than    |
    |                  |                        | 5nT in (X, Y, Z)       |
    |                  |                        | orientation.           |
    +------------------+------------------------+------------------------+
    | Definitive       | IMFV1.23, IAGA-2002    | Observatory data which |
    |                  | and IAFV2.11 (as a     | have been corrected    |
    |                  | metadata field) and    | for baseline           |
    |                  | IAF version prior to   | variations, have had   |
    |                  | V2.11 (implied - data  | spikes removed and     |
    |                  | in this format can     | gaps filled where      |
    |                  | only be ‘Definitive’). | possible. No further   |
    |                  |                        | change is expected and |
    |                  |                        | the quality of the     |
    |                  |                        | data is such that they |
    |                  |                        | would be used for      |
    |                  |                        | inclusion in           |
    |                  |                        | observatory year books |
    |                  |                        | and for input to the   |
    |                  |                        | World Data Centers and |
    |                  |                        | the IRDS.              |
    +------------------+------------------------+------------------------+

Where software is used to convert between formats (e.g. at GINs):

- The Reported data type is assumed to be interchangeable with
  the Variation data type.
- The Adjusted data type is assumed to be interchangeable with
  the Provisional data type.

The use of data types to describe more than the state of data
in the publication process is prone to error. INTERMAGNET is
moving to a system of describing the standard that a data set
meets and including this description alongside the data to
which it applies.


.. _sub_dat_intro_gc:

Geomagnetic Components (or Elements)
------------------------------------
Geomagnetic data can be described in a number of different
orientations. Component codes are used to describe the
individual elements of the geomagnetic vector.

-  X = H*cos(D)
-  Y = H*sin(D)
-  Z = F*sin(I)
-  H = F*cos(I)
-  H = SQRT(X^2 + Y^2)
-  F = SQRT(X^2 + Y^2 + Z^2)
-  tan(D) = Y/X
-  tan(I) = Z/H

.. figure:: ../../img/geomagn_coordinates.png
    :align: center
    :scale: 80 %
    :alt: Geomagnetic components

    Geomagnetic components

.. tabularcolumns:: |p{1cm}|p{10cm}|

.. table::
    :widths: auto
    :align: center

    +------+--------------------------------------------------------------+
    | Code | Description                                                  |
    +======+==============================================================+
    | X    | North Component. The strength of the magnetic field vector   |
    |      | in the geographic north direction (northerly values are      |
    |      | positive).                                                   |
    +------+--------------------------------------------------------------+
    | Y    | East component. The strength of the magnetic field vector in |
    |      | the geographic east direction (easterly values are           |
    |      | positive).                                                   |
    +------+--------------------------------------------------------------+
    | Z    | Vertical intensity. The strength of the magnetic field       |
    |      | vector in the vertical direction (Z is positive down and     |
    |      | hence negative south of the geomagnetic equator).            |
    +------+--------------------------------------------------------------+
    | H    | Horizontal intensity. The strength of the magnetic field     |
    |      | vector in the horizontal plane along the magnetic meridian.  |
    +------+--------------------------------------------------------------+
    | D    | Declination or variation. The angle between the magnetic     |
    |      | vector and true north (positive east).                       |
    +------+--------------------------------------------------------------+
    | I    | Inclination. The angle between the magnetic vector and the   |
    |      | horizontal plane, in degrees of arc (positive below the      |
    |      | horizontal).                                                 |
    +------+--------------------------------------------------------------+
    | F    | Total field intensity. The geomagnetic field strength,       |
    |      | calculated from and consistent with XYZ or HDZ field         |
    |      | elements.                                                    |
    +------+--------------------------------------------------------------+


.. _sub_dat_intro_rtpd:

Near Real-Time Preliminary Data
-------------------------------

INTERMAGNET wishes to make data available to users as soon as
possible after it is recorded. Observatories who are members of
INTERMAGNET are required to submit their preliminary data
within 72 hours of recording. This requirement has been in
place since INTERMAGNET was created and was a challenging
target in the days before the INTERNET. It is now a minimum
requirement. INTERMAGNET wishes to improve its near real-time
performance and has set these goals for near real-time performance:

-  1-second data: Available to users within 30 seconds.
-  1-minute data: Available to users within 2 minutes.

These are challenging targets and at present (2018) the
INTERMAGNET infrastructure is not able to support these
targets; the best possible performance is around 15-20 minutes.
However observatories are encouraged to submit preliminary data
to their assigned GIN as near to real-time as possible. The
best way to achieve this is using the web interface to submit
data in IAGA-2002 format.

.. _sub_dat_intro_gin:

Geomagnetic Information Nodes
-----------------------------

INTERMAGNET has a two stage approach to collection and
dissemination of non-definitive data. Observatories send their
data to one of 5 Geomagnetic Information Nodes (GINs). The GINs
then forward data to the INTERMAGNET web site for distribution
to users, where it is made available via a web service, a data
download application on the web and an FTP site. GINs may make
provision for observatories to access their own data once it
has been sent to the GIN, but there is no public access to data
at the GINs – all public access to data is via the INTERMAGNET
web site. Both GINs and the web site keep a permanent copy of
all data sent to them – no data is deleted (though it may be
overwritten if an observatory sends an update).

INTERMAGNET will not edit any data that an observatory has
sent, though it may contact an observatory if problems are
detected and may also remove spikes for the purposes of
plotting the data. GINs will send monthly reports of the
‘completeness’ of the data received from observatories. The
INTERMAGNET web site will send monthly reports to observatories
on the requests users have made for their data. The manager at
each GIN acts as a point of contact for IMOs to resolve any
data transmission and formatting problems.

.. _sub_dat_intro_gin_addr:

GIN Manager Addresses
`````````````````````

Any enquiries to individual GINs should be made to the
INTERMAGNET GIN Manager at the following addresses:

| **USGS - USA:**
| Abram Claycomb
| U.S. Geological Survey
| Box 25046 MS 966
| Denver Federal Center
| Denver, Colorado 80225-0046
| USA
| Telephone: 1-303-273-8485
| Fax: 1-303-273-8506
| Internet: aclaycomb@usgs.gov

| **GSC - Canada:**
| Charles Blais
| Canadian Hazards Information Service
| Natural Resources Canada
| 7 Observatory Cr.
| Ottawa, Ontario
| CANADA
| K1A 0Y3
| Telephone: 1-613-298-1292
| Fax: 1-613-992-8836
| Internet: charles.blais@canada.ca

| **BGS - Scotland:**
| Simon M. Flower
| Geomagnetism Team
| British Geological Survey
| The Lyell Centre
| Research Avenue South
| Edinburgh EH14 4AP
| UK
| Telephone: 44-131-667-1000
| Fax: 44-131-667-1877
| Internet: e_ginman@mail.nmh.ac.uk

| **IPG - France:**
| Virginie Maury
| Institut de Physique du Globe de Paris
| Observatoires magnétiques - Bureau 110
| 1, rue Jussieu
| 75238 Paris Cedex 05
| France
| Telephone: +33 (0)1 83 95 77 80
| Fax: 33 (0) 1-71-93-77-09
| Internet: p_ginman@ipgp.fr

| **Kyoto University - Japan:**
| Hiroaki Toh
| Data Analysis Center for Geomagnetism and
| Space Magnetism
| Graduate School of Science, Bldg #4
| Kyoto University
| Oiwake-cho, Kitashirakawa, Sakyo-ku
| Kyoto 606-8502
| JAPAN
| Telephone: 81-75-753-3959
| Fax: 81-75-722-7884
| Internet: imagmanager@swdcdb.kugi.kyoto-u.ac.jp

.. _sub_dat_intro_gin_email:

GIN Email Addresses
```````````````````

-  Ottawa: |contact_gin_ottawa|
-  Paris: |contact_gin_paris|
-  Golden: |contact_gin_golden|
-  Edinburgh:|contact_gin_edin|
-  Kyoto: |contact_gin_kyoto|



INTERMAGNET GIN Types
`````````````````````

The five INTERMAGNET GINs can be classified into two types,
depending on the observatories they handle and the services
they offer.

.. tabularcolumns:: |p{2cm}|p{8cm}|p{4cm}|

.. table::
    :widths: auto
    :align: center

    +-----------------------+-----------------------+-----------------------+
    | Type                  | Description           | GIN                   |
    +=======================+=======================+=======================+
    | 1                     | -  Handles data from  | Golden, Ottawa        |
    |                       |    observatories run  |                       |
    |                       |    by its own         |                       |
    |                       |    institute (and     |                       |
    |                       |    maybe a few others |                       |
    |                       |    with which it has  |                       |
    |                       |    close              |                       |
    |                       |    relationship).     |                       |
    |                       | -  Uses its own       |                       |
    |                       |    mechanisms to      |                       |
    |                       |    collect data from  |                       |
    |                       |    observatories      |                       |
    +-----------------------+-----------------------+-----------------------+
    | 2                     | -  Handles data from  | Edinburgh, Kyoto,     |
    |                       |    many IMOs not      | Paris                 |
    |                       |    associated with    |                       |
    |                       |    its own institute. |                       |
    |                       | -  Uses INTERMAGNET   |                       |
    |                       |    defined mechanisms |                       |
    |                       |    to collect data    |                       |
    |                       |    from               |                       |
    |                       |    observatories.     |                       |
    +-----------------------+-----------------------+-----------------------+

New observatories not run by USGS or GSC would normally be
assigned to one of the Type 2 GINs.

