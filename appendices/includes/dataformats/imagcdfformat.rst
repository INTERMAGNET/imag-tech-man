.. _app_cdf:


IMAGCDF INTERMAGNET Exchange Format
-----------------------------------

.. include:: ../shared/variables.rst


This document describes how NASA's Common Data Format ( CDF - |cdf_format| )
is used to store geomagnetic data. This format is called ImagCDF. 

.. _app_cdf_design:

Design Details and CDF Concepts
```````````````````````````````

General Design Details
""""""""""""""""""""""


Geomagnetic data is held in CDF variables, one variable per
geomagnetic element. Additional variables hold time stamp data.
A single time stamp variable may be used if all time series data
uses the same sample rate. Alternatively
one time stamp variable may be for the vector
magnetometer data, a second variable for the scalar magnetometer
data, if data from these two instruments are recorded at
different sample rates. 

Each variable (data or time stamp) has one or more records, an
individual record holding a single sample value. The index numbers
of the records in the data variables correspond with
the index numbers in the appropriate time stamp variable's records.
A typical file might contain 6
variables: 3 geomagnetic elements (such as HDZ or XYZ); one scalar
element (F); and two timing variables, one for the vector data,
the other for the scalar. The format does not mandate that these
variables are present – there may be fewer (for example only
scalar data) or more (for example additional temperature data).

Metadata is held in CDF attributes in two ways: global attribute
entries concern all the data in a file; variable attributes have
entries that concern a single variable (e.g. the geomagnetic data 'H' variable). An
entry holds an individual item of metadata. An attribute name
(whether global or variable) must be unique, so when an attribute
needs to be used more than once (e.g. the element type for a
geomagnetic variable must be used once for each geomagnetic
element), then multiple entries are created in a single attribute.
Global attributes in ImagCDF will have only one entry (with two
exceptions). Variable attributes may have an entry for each of the
relevant variables in the file. For variable attributes, the
multiple entries are indexed using the variable's numeric
identifier, so that the metadata 'belongs' to the variable. For
example, in an ImagCDF file holding HDZF data, the attribute Units
will have four entries (in this order): "nT"; "Degrees of arc";
"nT"; "nT".

Data Types Used for Variables and Attributes
""""""""""""""""""""""""""""""""""""""""""""

Real Numbers
############


ImagCDF uses double precision CDF_DOUBLE (8-byte) floating point
numbers (to the IEEE 754 standard) for all numeric values. These
numbers provide about 14.5 (decimal) digits of precision -
|floating_point_arithmetic|.
In order to use floating point numbers successfully, the dynamic
range of the quantity being represented (ratio of smallest to
largest value) must be smaller than 14.5 digits. For geomagnetic
field strengths, assume that the ratio of smallest difference to
largest value that we need to represent in geomagnetic field data
is 0.1pT in 80,000nT. This equates to 1 part in 80,000 x 1,000 x
10, or 1 part in 800,000,000, or 9 digits of precision, so is
within the dynamic range available.

Dates / Times
#############

All date / time values in ImagCDF are held as CDF TT2000 dates,
which are based on 8-byte integers. TT2000 uses an epoch (midday
on 1st January 2000) to store dates and times, has a precision of
1 nanosecond which gives a range in excess of ±280 years from the
epoch date. The TT2000 type can correctly handle leap seconds.

Strings
#######

Text data is held using CDF_CHAR variables in ImagCDF.

Compression
"""""""""""

The CDF library allows the user to specify whether all, part or
none of a CDF file is compressed at the time it is written. Once
this choice has been made, the CDF library handles compression and
decompression of the data in the file automatically (reading and
any further writing to the file will decompress or compress as
required). Choosing whether or not to compress a file is simply a
matter of specifying which (if any) compression method to use when
the file is created. ImagCDF allows any of the compressions
provided by CDF.

Significant compression is achieved using the CDF compression
option. A day file of four element minute data can occupy under
15Kb.

.. _app_cdf_optain_soft:

Where to Obtain the CDF Software
````````````````````````````````

Before you can use any of NASA or INTERMAGNET's tools for working
with ImagCDF, you will need to download and install the CDF
software from NASA: |cdf_software| . Software that has
been written to work with CDF is likely to need the libraries that
are installed. For details of other software that may be useful
see section :ref:`app_cdf_tools`.

.. _app_cdf_data:

ImagCDF Data
````````````

All variables holding geomagnetic data have the following
features:

- Units used must be nT for geomagnetic field values, degrees for
  angles or celsius for temperatures.
- Lengths of time series are arbitrary (e.g. a file may be used
  to store an entire day of data or a small fragment of a day
  down to a single sample).

Geomagnetic data is held in variables called GeomagneticField <E>
where <E> represents the code for the geomagnetic element recorded
- see section :ref:`app_cdf_v1_20_gattr_valid_codes`
for a list of valid codes (in version 1.20). The variable has 0 dimensions,
each consecutive record holding individual consecutive data samples in CDF double data type,
starting at record 1. Missing data values are represented by a
data sample that contains the same number as is present in the
FILLVAL metadata attribute. The FILLVAL must exceed any valid
geomagnetic field strength or angle. Typically this would be
99999.0. The variable attribute FIELDNAM must be set to
"Geomagnetic Field Element <E>".

An ImagCDF file must include a set of geomagnetic field variables
that describe the vector field in a recognised orientation (such
as 'HDZ', 'XYZ' or 'DIF). All vector variables must have the same
number of records. An ImagCDF file may also include an additional
field element from an independent scalar instrument, with an
element code of 'G' or 'S'.

Temperature data is optional (unless otherwise stated in the data
standard that the data conforms to, for example, temperature is
mandatory for data that conforms to the INTERMAGNET 1-second data
standard). The first temperature variable is called Temperature1,
then Temperature2 and so on. The FIELDNAM attribute describes, in
free text, for each temperature variable, the location at which
the temperature was recorded.

Time stamps for the data are held in separate variables. Time
stamps must represent a regular time series with no missing values
in the series. If all data has the same sample rate, a single
time stamp variable called DataTimes may be used. Otherwise
time stamps for all the geomagnetic field vector
variables are held in a single variable called
GeomagneticVectorTimes and time stampes for the scalar data are
held in a variable called
GeomagneticScalarTimes. Time stamps for temperature data are held
in variables called Temperature1Times, Temperature2Times and so
on. These variables have 0 dimensions and must have the same
number of records as the data variables that they apply to. Each
record in a time stamp variable holds a CDF TT2000 epoch time.
Time stamps must always refer to the start of each sample period
(e.g. for minute data, the seconds and milliseconds will always be
set to zero).

Recommended names for time stamp variables are:

.. tabularcolumns:: |p{7.5cm}|p{7.5cm}|

.. table::
    :widths: auto
    :align: center

    +----------------------------------+----------------------------------+
    | Situation                        | Names                            |
    +==================================+==================================+
    | The same time stamps can be used |  DataTimes                       |
    | for all data in the file (i.e.   |                                  |
    | there is a single time stamp     |                                  |
    | variable in the file)            |                                  |
    +----------------------------------+----------------------------------+
    | Different time stamps for        | *GeomagneticVectorTimes,         |
    | vector, scalar and temperature   | GeomagneticScalarTimes,          |
    |                                  | Temperature1Times,               |
    |                                  | Temperature2Times, …*            |
    +----------------------------------+----------------------------------+

Additional variables and metadata may be carried in an ImagCDF
(e.g. it may be convenient to include meteorological data in the
same file). The format of these variables and metadata is left to
the user to define. The CDF system means that these variables can
be included without causing problems to software reading ImagCDF
files. Software writing ImagCDF files should preserve additional
variables and attributes read from an ImagCDF file.

.. _app_cdf_v1_20:

ImagCDF Version 1.20
````````````````````

The descriptions in this section apply to version 1.20 of ImagCDF.

.. _app_cdf_v1_20_gattr:

ImagCDF Global Attributes (V1.20)
"""""""""""""""""""""""""""""""""

The following attributes apply to all the data in an ImagCDF file.
The "Entries" column shows whether the attribute has:

- A single mandatory entry (number of entries is exactly 1)
- A single optional entry (number of entries may be 0 or 1)
- Multiple mandatory entries (number of entries is between 1 and
  N\ :sup:`1`)
- Optional mandatory entries (number of entries is between 1 and
  N\ :sup:`2`)

Superscript numbers following the attribute name show:

#. That the attribute is a recommended attribute for use with
   NASA's CDF tools
#. That the attribute is part of the ISTP/IACG guidelines -
   |istp_gattr|

.. _app_cdf_v1_20_gattr_describe_data:

Attributes that Describe the Data Format (V1.20)
################################################

These are 'constant' values that will be the same for all ImagCDF
files. They allow 'generic' CDF programs to understand and process
the data correctly.

.. tabularcolumns:: |p{3cm}|p{1.5cm}|>{\centering\arraybackslash}p{1.5cm}|p{7cm}|

.. table::
    :widths: auto
    :align: center

    ================= ====== ======= ================================================
    Attribute Name    Type   Entries Description
    ================= ====== ======= ================================================
    FormatDescription String 1       Always set to "INTERMAGNET CDF Format"
    FormatVersion     String 1       Set to the current version of the format – "1.2"
    Title             String 1       Always set to "Geomagnetic time series data"
    ================= ====== ======= ================================================


.. _app_cdf_v1_20_gattr_unique_id:

Attributes that Uniquely Identify the Data (V1.20)
##################################################

The attributes in this section are sufficient, along with the
start date and duration of the time series, to uniquely identify a
piece of geomagnetic data.

.. tabularcolumns:: |p{3cm}|p{1.5cm}|>{\centering\arraybackslash}p{1.5cm}|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +-----------------------+------------+------------+------------------------------------------------+
    | Attribute Name        | Type       | Entries    | Description                                    |
    +=======================+============+============+================================================+
    | IagaCode              | String     | 1          | The IAGA code for the observatory              |
    +-----------------------+------------+------------+------------------------------------------------+
    | ElementsRecorded      | String     | 1          | A string consisting of single character codes, |
    |                       |            |            | each describing one of the geomagnetic field   |
    |                       |            |            | elements that is recorded in this data file.   |
    |                       |            |            | This might typically be a three or four digit  |
    |                       |            |            | code such as HDZ, XYZG or DIFG. The codes in   |
    |                       |            |            | this attribute determine the names of the data |
    |                       |            |            | variables (see the section on geomagnetic      |
    |                       |            |            | data). Valid codes are defined in section      |
    |                       |            |            | :ref:`app_cdf_v1_20_gattr_valid_codes`         |
    +-----------------------+------------+------------+------------------------------------------------+
    | PublicationLevel      | String     | 1          | Choose one of the following codes to describe  |
    |                       |            |            | the level that the data has been processed to: |
    |                       |            |            |                                                |
    |                       |            |            | -  *1*: The data is unprocessed and as         |
    |                       |            |            |    recorded at the observatory with no changes |
    |                       |            |            |    made.                                       |
    |                       |            |            | -  *2*: Some edits have been made such as gap  |
    |                       |            |            |    filling and spike removal and a             |
    |                       |            |            |    preliminary baseline added.                 |
    |                       |            |            | -  *3*: The data is at the level required for  |
    |                       |            |            |    production of an initial bulletin or for    |
    |                       |            |            |    quasi-definitive publication.               |
    |                       |            |            | -  *4*: The data has been finalised and no     |
    |                       |            |            |    further changes are intended                |
    |                       |            |            |                                                |
    |                       |            |            | Only these values are allowed.                 |
    |                       |            |            |                                                |
    |                       |            |            | This field provides a quick description of the |
    |                       |            |            | point the data has reached in the publication  |
    |                       |            |            | process. For detailed information on the       |
    |                       |            |            | standards that the data conforms to see        |
    |                       |            |            | section :ref:`app_cdf_v1_20_gattr_stand_q`     |
    +-----------------------+------------+------------+------------------------------------------------+
    | PublicationDate       | Date/time  | 1          | Date and time on which the data was published. |
    |                       |            |            | This attribute is used to distinguish multiple |
    |                       |            |            | publications of the same data.                 |
    +-----------------------+------------+------------+------------------------------------------------+


.. _app_cdf_v1_20_gattr_obs:

Attributes that Describe the Observatory (V1.20)
################################################

These attributes are available from other metadata systems (given
an IAGA code), but are included for convenience of the user.

.. tabularcolumns:: |p{3cm}|p{1.5cm}|>{\centering\arraybackslash}p{1.5cm}|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +------------------+--------+-----------+-------------------------------------------------------+
    | Attribute Name   | Type   | Entries   | Description                                           |
    +==================+========+===========+=======================================================+
    | ObservatoryName  | String | 1         | The full name for the observatory                     |
    +------------------+--------+-----------+-------------------------------------------------------+
    | Latitude         | Double | 1         | The latitude of the observing position in degrees, to |
    |                  |        |           | WGS-84 datum                                          |
    +------------------+--------+-----------+-------------------------------------------------------+
    | Longitude        | Double | 1         | The longitude of the observing position in degrees,   |
    |                  |        |           | to WGS-84 datum                                       |
    +------------------+--------+-----------+-------------------------------------------------------+
    | Elevation        | Double | 1         | The height of the observing position in metres above  |
    |                  |        |           | sea level, to WGS-84 datum. Set to 99999.0 if not     |
    |                  |        |           | known.                                                |
    +------------------+--------+-----------+-------------------------------------------------------+
    | Institution      | String | 1 or more | The name of the responsible institute.                |
    +------------------+--------+-----------+-------------------------------------------------------+
    | VectorSensOrient | String | 0 - 1     | The orientation code of the sensor at the original    |
    |                  |        |           | recording of the vector data. A string consisting of  |
    |                  |        |           | single character codes, each describing one of the    |
    |                  |        |           | geomagnetic field elements that was recorded by the   |
    |                  |        |           | vector instrument. Valid codes are the same as for    |
    |                  |        |           | the ElementsRecorded attribute.                       |
    +------------------+--------+-----------+-------------------------------------------------------+


.. _app_cdf_v1_20_gattr_stand_q:

Attributes that Relate to Data Standards and Quality (V1.20)
############################################################

These attributes describe the standards, if any, that the data
meets.


.. tabularcolumns:: |p{3cm}|p{1.5cm}|>{\centering\arraybackslash}p{1.5cm}|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +-------------------------+-----------+---------+--------------------------------------------------+
    | Attribute Name          | Type      | Entries | Description                                      |
    +=========================+===========+=========+==================================================+
    | StandardLevel           | String    | 1       | Describe whether the data conforms to a          |
    |                         |           |         | standard. Choose from one of the following       |
    |                         |           |         | codes:                                           |
    |                         |           |         |                                                  |
    |                         |           |         | -  *None*: The data does not conform to any      |
    |                         |           |         |    standards. When using this, the               |
    |                         |           |         |    StandardName attribute does not need to be    |
    |                         |           |         |    set.                                          |
    |                         |           |         | -  *Partial*: The data partially conforms to     |
    |                         |           |         |    the relevant standard for this data           |
    |                         |           |         |    product.                                      |
    |                         |           |         | -  *Full*: The data fully conforms to the        |
    |                         |           |         |    relevant standard for this data product.      |
    |                         |           |         |                                                  |
    |                         |           |         | Only these values are allowed.                   |
    |                         |           |         |                                                  |
    |                         |           |         | If *StandardsLevel* is set to *Partial*, then    |
    |                         |           |         | the *PartialStandDesc* attribute must also be    |
    |                         |           |         | set.                                             |
    +-------------------------+-----------+---------+--------------------------------------------------+
    | StandardName            | String    | 0 - 1   | The name of the relevant standard. See section   |
    |                         |           |         | :ref:`app_cdf_v1_20_gattr_rel_stand`             |
    +-------------------------+-----------+---------+--------------------------------------------------+
    | StandardVersion         | String    | 0 – 1   | If the standard has a version, put its version   |
    |                         |           |         | number in this attribute.                        |
    +-------------------------+-----------+---------+--------------------------------------------------+
    | PartialStandDesc        | String    | 0 - 1   | See section :ref:`app_cdf_v1_20_gattr_rel_stand` |
    +-------------------------+-----------+---------+--------------------------------------------------+

Attributes that Relate to Publication of the Data (V1.20)
#########################################################

These attributes are needed when that data is published.

.. tabularcolumns:: |p{3cm}|p{2cm}|c|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +-------------------+------------+-----------+--------------------------------------------------+
    | Attribute Name    | Type       | Entries   | Description                                      |
    +===================+============+===========+==================================================+
    | Source            | String     | 1         | Set to one of: "institute" (if the named         |
    |                   |            |           | institution provided the data- see section       |
    |                   |            |           | :ref:`app_cdf_v1_20_gattr_obs`                   |
    |                   |            |           | for the institution); "INTERMAGNET" (if the data |
    |                   |            |           | file has been created by INTERMAGNET from        |
    |                   |            |           | another data source); "WDC" (if the World Data   |
    |                   |            |           | Centre has created the file from another data    |
    |                   |            |           | source)                                          |
    +-------------------+------------+-----------+--------------------------------------------------+
    | TermsOfUse        | String     | 0 – 1     | The terms of use for the data. This could be     |
    |                   |            |           | text describing the terms of use or a link to a  |
    |                   |            |           | web page. INTERMAGNET has a recommended wording  |
    |                   |            |           | for data provided through INTERMAGNET.           |
    +-------------------+------------+-----------+--------------------------------------------------+
    | UniqueIdentifier  | String     | 0 – 1     | A string that can be used to uniquely identify   |
    |                   |            |           | this data. This could be a Digital object        |
    |                   |            |           | identifier or could be an identifier created     |
    |                   |            |           | according to local rules. Note this is optional  |
    |                   |            |           | and will not be present if this data is not      |
    |                   |            |           | covered by an identifier.                        |
    +-------------------+------------+-----------+--------------------------------------------------+
    | ParentIdentifiers | String     | 0 or more | The unique identifiers of the parent data sets   |
    |                   |            |           | (if any), one identifier per entry. The parent   |
    |                   |            |           | data set is the data set from which this data    |
    |                   |            |           | set's values have been derived. E.g. if a one    |
    |                   |            |           | minute data set has been created from a one      |
    |                   |            |           | second data set, the one second data set is the  |
    |                   |            |           | parent. Another example is where definitive data |
    |                   |            |           | is created from provisional data.                |
    +-------------------+------------+-----------+--------------------------------------------------+
    | ReferenceLinks    | String/URL | 0 or more | URLs pointing to (e.g.) information about the    |
    |                   |            |           | data creator, information about the data         |
    |                   |            |           | repository… One URL per entry.                   |
    +-------------------+------------+-----------+--------------------------------------------------+

.. _app_cdf_v1_20_gattr_valid_codes:

Valid Codes for Elements Recorded (V1.20)
#########################################

- 'X', 'Y', or 'Z' indicate that the variable holds the strength
  of the magnetic field vector in the standard geographic
  coordinates in nT.
- 'H' indicates that the variable holds the strength of the
  magnetic field vector in the horizontal plane along the
  magnetic meridian in nT.
- 'D' indicates that the variable holds the angle between the
  magnetic vector and true north, in degrees of arc, positive
  east.
- 'E' indicates that the variable holds a field strength in the
  horizontal plane perpendicular to 'H' in nT. 'E' is only valid
  for data that is not baseline corrected.
- 'V' indicates that the variable holds the field strength along
  the direction of the inclination.
- 'I' indicates that the variable holds the angle between the
  magnetic vector and the horizontal plane, in degrees of arc,
  positive below the horizontal.
- 'F' indicates that the variable holds the geomagnetic field
  strength in nT, calculated from and consistent with XYZ or HDZ
  field elements.
- 'S' indicates that the variable holds the geomagnetic field
  strength in nT, measured by an independent scalar instrument
- 'G' indicates that the variable holds delta- F values, defined
  as F(vector) –S(scalar) in nT. When calculating values for the
  G element, if F(vector) is missing, G is set to –S (scalar)

Other codes are allowed, but may lead to data not being
understood.

.. _app_cdf_v1_20_gattr_rel_stand:

Relevant Data Standards (V1.20)
###############################

Different geomagnetic data products have different standards
associated with them. This table shows what standards are being
referred to in the StandardsLevel attribute and describes what to
put into the StandardName attribute in the case where
StandardsLevel is set to Partial or Full. The table also shows
what to put in the PartialStandDesc attribute in the case where
the StandardsLevel attribute is set to Partial.

.. tabularcolumns:: |p{4cm}|p{6cm}|p{5cm}|

.. table::
    :widths: auto
    :align: center

    +---------------------------+---------------------------------+---------------------------+
    | Data product              | Relevant Standard               | Contents of StandardName  |
    +===========================+=================================+===========================+
    | One second definitive     | INTERMAGNET Definitive          | INTERMAGNET_1-Second      |
    | data                      | One-second Data                 |                           |
    |                           | Standard [#f2]_                 |                           |
    +---------------------------+---------------------------------+---------------------------+
    | One minute definitive     | INTERMAGNET magnetic            | INTERMAGNET_1-Minute      |
    | data                      | observatory –                   |                           |
    |                           | specifications [#f3]_           |                           |
    +---------------------------+---------------------------------+---------------------------+
    | One minute                | INTERMAGNET magnetic            | INTERMAGNET_1-Minute_QD   |
    | quasi-definitive data     | observatory –                   |                           |
    |                           | specifications [#f3]_,modified  |                           |
    |                           | for baseline accuracy [#f4]_    |                           |
    +---------------------------+---------------------------------+---------------------------+
    | Hourly means              | No relevant standard            |                           |
    +---------------------------+---------------------------------+---------------------------+
    | Daily means               | No relevant standard            |                           |
    +---------------------------+---------------------------------+---------------------------+
    | Monthly means             | No relevant standard            |                           |
    +---------------------------+---------------------------------+---------------------------+
    | Annual means              | No relevant standard            |                           |
    +---------------------------+---------------------------------+---------------------------+

.. [#f2]  INTERMAGNET Technical Note 6
.. [#f3]  :numref:`1min_imo_descr`
.. [#f4]  Quasi-definitive definition on the INTERMAGNET web site: |faq_qd|

If a standard is met in full or not met at all, PartialStandDesc can be
omitted. Where a standard is partially met (e.g. the time stamp accuracy
is within tolerance, but the data is not baseline corrected), the name
of the relevant standard should be put in the *StandardName* attribute,
*StandardLevel* should be set to *Partial* and the *PartialStandDesc*
attribute should be filled in with a comma separated list of the
sub-sections from the standard that the data meets. E.g. if the data
meets the time stamp accuracy and thermal stability sections of the
1-minute data standard, enter *IMOM-01,IMOM-16* in *PartialStandDesc*.


.. tabularcolumns:: |>{\centering\arraybackslash}p{3cm}|p{12cm}|

.. table::
    :widths: auto
    :align: center

    +-------------------+--------------------------------------------------------------+
    | Value to put in   | Description                                                  |
    | PartialStandDesc  |                                                              |
    +-------------------+--------------------------------------------------------------+
    |                   | **One-minute Definitive Data: General specifications**       |
    +-------------------+--------------------------------------------------------------+
    | IMOM-01           | Time-stamp accuracy (centered on the UTC minute): 5s         |
    +-------------------+--------------------------------------------------------------+
    |                   | **One-minute Definitive Data: Vector Magnetometer            |
    |                   | specifications**                                             |
    +-------------------+--------------------------------------------------------------+
    | IMOM-11           | Absolute Accuracy: ±5nT                                      |
    +-------------------+--------------------------------------------------------------+
    | IMOM-12           | Resolution: 0.1nT                                            |
    +-------------------+--------------------------------------------------------------+
    | IMOM-13           | Dynamic Range: ≥±4000nT High Lat., ≥±3000nT Mid/Equatorial   |
    |                   | Lat.                                                         |
    +-------------------+--------------------------------------------------------------+
    | IMOM-14           | Band pass: D.C. to 0.1Hz                                     |
    +-------------------+--------------------------------------------------------------+
    | IMOM-15           | Minimum sampling rate: 1Hz                                   |
    +-------------------+--------------------------------------------------------------+
    | IMOM-16           | Thermal stability: 0.25nT/°C                                 |
    +-------------------+--------------------------------------------------------------+
    | IMOM-17           | Long term stability: 5nT/year                                |
    +-------------------+--------------------------------------------------------------+
    | IMOM-18           | Filtering to one-minute data: INTERMAGNET Gaussian           |
    +-------------------+--------------------------------------------------------------+
    |                   | **One-minute Definitive Data: Scalar Magnetometer            |
    |                   | specifications**                                             |
    +-------------------+--------------------------------------------------------------+
    | IMOM-21           | Resolution: 0.1nT                                            |
    +-------------------+--------------------------------------------------------------+
    | IMOM-22           | Absolute Accuracy: ±1nT                                      |
    +-------------------+--------------------------------------------------------------+
    | IMOM-23           | Minimum sampling rate: 0.033Hz (30 sec)                      |
    +-------------------+--------------------------------------------------------------+
    |                   | **One-second Data: General Specifications**                  |
    +-------------------+--------------------------------------------------------------+
    | IMOS-01           | Time-stamp accuracy (centered on the UTC second): 0.01s      |
    +-------------------+--------------------------------------------------------------+
    | IMOS-02           | Phase response: Maximum group delay: ±0.01s                  |
    +-------------------+--------------------------------------------------------------+
    | IMOS-03           | Maximum filter width: 25 seconds                             |
    +-------------------+--------------------------------------------------------------+
    | IMOS-04           | Instrument amplitude range: ≥±4000nT High Lat., ≥±3000nT     |
    |                   | Mid/Equatorial Lat.                                          |
    +-------------------+--------------------------------------------------------------+
    | IMOS-05           | Data resolution: 1pT                                         |
    +-------------------+--------------------------------------------------------------+
    | IMOS-06           | Pass band: DC to 0.2Hz                                       |
    +-------------------+--------------------------------------------------------------+
    |                   | **One-second Data: Specifications in the Pass Band [DC to    |
    |                   | 8mHz (120s)]**                                               |
    +-------------------+--------------------------------------------------------------+
    | IMOS-11           | Noise level: ≤100pT RMS                                      |
    +-------------------+--------------------------------------------------------------+
    |                   | Maximum offset error (cumulative error between absolute      |
    |                   | observations): ±2.5 nT                                       |
    +-------------------+--------------------------------------------------------------+
    | IMOS-13           | Maximum component scaling plus linearity error: 0.25%        |
    +-------------------+--------------------------------------------------------------+
    | IMOS-14           | Maximum component orthogonality error: 2mrad                 |
    +-------------------+--------------------------------------------------------------+
    | IMOS-15           | Maximum Z-component verticality error: 2mrad                 |
    +-------------------+--------------------------------------------------------------+
    |                   | **One-second Data: Specifications in the Pass Band [8mHz     |
    |                   | (120s) to 0.2Hz]**                                           |
    +-------------------+--------------------------------------------------------------+
    | IMOS-21           | Noise level: ≤10pT/√Hz at 0.1 Hz                             |
    +-------------------+--------------------------------------------------------------+
    | IMOS-22           | Maximum gain/attenuation: 3dB                                |
    +-------------------+--------------------------------------------------------------+
    |                   | **One-second Data: Specifications in the Stop Band [≥0.5     |
    |                   | Hz]**                                                        |
    +-------------------+--------------------------------------------------------------+
    | IMOS-31           | Minimum attenuation in the stop band (≥ 0.5Hz): 50dB         |
    +-------------------+--------------------------------------------------------------+
    |                   | **One-second Data: Auxiliary measurements:**                 |
    +-------------------+--------------------------------------------------------------+
    | IMOS-41           | Compulsory full-scale scalar magnetometer measurements with  |
    |                   | a data resolution of 0.01nT at a minimum sample period of 30 |
    |                   | seconds.                                                     |
    +-------------------+--------------------------------------------------------------+
    | IMOS-42           | Compulsory vector magnetometer temperature measurements with |
    |                   | a resolution of 0.1°C at a minimum sample period of one      |
    |                   | minute.                                                      |
    +-------------------+--------------------------------------------------------------+

.. _app_cdf_v1_20_vattr:

ImagCDF Variable Attributes (V1.20)
"""""""""""""""""""""""""""""""""""

The following attributes apply to individual variables - there is an
attribute entry for each geomagnetic field element or temperature in an
ImagCDF file and the value of that entry applies only to that field
element or temperature. The "Entries" column shows whether the attribute
is:

-  Mandatory (number of entries per variable is exactly :sup:`1`)
-  Optional (number of entries per variable may be :sup:`0` or :sup:`1`)

.. raw:: latex

    \newpage

None of these attributes are required for the time stamp variables
GeomagneticVectorTimes and GeomagneticScalarTimes.

.. tabularcolumns:: |p{3cm}|p{1.5cm}|>{\centering\arraybackslash}p{1.5cm}|p{8cm}|

.. table::
    :widths: 24,10,6,60
    :align: center

    +--------------------------+--------+---------+-----------------------------------------------------------+
    | Attribute Name           | Type   | Entries | Description                                               |
    +--------------------------+--------+---------+-----------------------------------------------------------+
    | FIELDNAM [#f5]_          | String | 1       | Set to "Geomagnetic Field Element " + the element code    |
    |                          |        |         | (e.g. H, D, Z,… - see section                             |
    |                          |        |         | :ref:`app_cdf_v1_20_gattr_valid_codes` for a list of      |
    |                          |        |         | valid codes); or set to "Temperature " + the name of the  |
    |                          |        |         | location where the temperature was recorded.              |
    +--------------------------+--------+---------+-----------------------------------------------------------+
    | UNITS [#f5]_             | String | 1       | Must be one of "nT", "Degrees of arc" or "Celsius"        |
    +--------------------------+--------+---------+-----------------------------------------------------------+
    | FILLVAL [#f5]_           | Double | 1       | The value used to show that a data sample is missing. Set |
    |                          |        |         | to 99999.0 for compatibility with other formats. The      |
    |                          |        |         | values must either less than VALIDMIN or greater than     |
    |                          |        |         | VALIDMAX.                                                 |
    +--------------------------+--------+---------+-----------------------------------------------------------+
    | VALIDMIN [#f5]_          | Double | 1       | The smallest allowed numeric value for the data in the    |
    |                          |        |         | corresponding variable.                                   |
    +--------------------------+--------+---------+-----------------------------------------------------------+
    | VALIDMAX   [#f5]_        | Double | 1       | The largest allowed numeric value for the data in the     |
    |                          |        |         | corresponding variable.                                   |
    +--------------------------+--------+---------+-----------------------------------------------------------+
    | DEPEND_0  [#f6]_         | String | 0 - 1   | For geomagnetic data, set this to the name of the         |
    |                          |        |         | variable that holds time stamps for this time series. For |
    |                          |        |         | records containing time stamps, do not set this variable. |
    +--------------------------+--------+---------+-----------------------------------------------------------+
    | DISPLAY_TYPE  [#f6]_     | String | 1       | Set to "time_series"                                      |
    +--------------------------+--------+---------+-----------------------------------------------------------+
    | LABLAXIS [#f6]_          | String | 1       | Set to the element code (as defined in section            |
    |                          |        |         | :ref:`app_cdf_v1_20_gattr_valid_codes` )                  |
    +--------------------------+--------+---------+-----------------------------------------------------------+

.. [#f5]  The attribute is a recommended attribute for use with NASA's CDF tools
.. [#f6]  The attribute is part of the ISTP/IACG guidelines - |istp_vattr|


ImagCDF File Names (V1.20)
""""""""""""""""""""""""""

ImagCDF files are named using the convention::

    [iaga-code]_[date-time]_[publication-level].cdf

- Iaga-code is the three letter IAGA code for the observatory that the data is from. This should
  match the IAGA code in section :ref:`app_cdf_v1_20_gattr_unique_id`.
- Date-time is the start date/time of the data in the file. The format for the date/time is
  described below.
- Publication-level is the PublicationLevel attribute from section :ref:`app_cdf_v1_20_gattr_unique_id`.

Filenames are in lower case. Files may contain arbitrary amounts of data, however the amount of data
is not coded into the filename.

Format of Date/Time Portion of Filename and Examples (V1.20)
############################################################

The date/time portion of the filename is formatted differently for different data with different
data intervals:

.. tabularcolumns:: |p{3cm}|p{4cm}|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +---------------+------------------+---------------------------------------------------------------+
    | Data Interval | Date/time format | Example filename                                              |
    +===============+==================+===============================================================+
    | Annual means  | YYYY             | esk_2000_4.cdf – final annual mean data from Eskdalemuir      |
    |               |                  | starting in the year 2000                                     |
    +---------------+------------------+---------------------------------------------------------------+
    | Monthly means | YYYYMM           | ott_201401_4.cdf – final monthly mean data from Ottawa        |
    |               |                  | starting in January 2014                                      |
    +---------------+------------------+---------------------------------------------------------------+
    | Daily means   | YYYYMMDD         | gua_20100101_4.cdf – final daily mean data from Guam starting |
    |               |                  | at the beginning of 2010                                      |
    +---------------+------------------+---------------------------------------------------------------+
    | Hourly means  | YYYYMMDD_HH      | naq_20020201_00_4.cdf – final hourly mean data from NAQ in    |
    |               |                  | January 2002                                                  |
    +---------------+------------------+---------------------------------------------------------------+
    | Minute means  | YYYYMMDD_HHMM    | naq_20020120_0000_3.cdf – 'bulletin' or quasi-definitive      |
    |               |                  | minute mean data from NAQ for 20th January 2002 starting at   |
    |               |                  | midnight                                                      |
    +---------------+------------------+---------------------------------------------------------------+
    | Second        | YYYYMMDD_HHMMSS  | naq_20020120_012300_1.cdf – raw 1-second data from NAQ for    |
    |               |                  | 20th January 2002 starting at 01:23:00                        |
    +---------------+------------------+---------------------------------------------------------------+

- YYYY = four digit year (i.e. 2002)
- MM = two digit month (01 for January - 12 for December)
- DD = two digit day of month (01-31)
- HH = two digit hour (0-23)
- MM = two digit minute (0-59)
- SS = two digit second (0-59)

.. _app_cdf_v1_30:

ImagCDF Version 1.30
````````````````````

The descriptions in this section apply to version 1.30 of ImagCDF.

Version 1.30 only changes the format of the ImagCDF filenames. The documentation
for version 1.20 should be used for the contents of these files:

.. _app_cdf_v1_30_gattr:

ImagCDF Global Attributes (V1.30)
"""""""""""""""""""""""""""""""""

There are no changes to the global attributes in the format since version 1.20. See the
global attributes documentation for :ref:`version 1.20<app_cdf_v1_20_gattr>`.

.. _app_cdf_v1_30_vattr:

ImagCDF Variable Attributes (V1.30)
"""""""""""""""""""""""""""""""""""

There are no changes to the variable attributes in the format since version 1.20. See the
varible attributes documentation for :ref:`version 1.20<app_cdf_v1_20_vattr>`.

ImagCDF File Names (V1.30)
""""""""""""""""""""""""""

Version 1.30 fixes some errors and omissions in the format of ImagCDF filenames.

ImagCDF files are named using the convention::

    [iaga-code]_[date-time]_[cadence]_[publication-level].cdf

- Iaga-code is the three letter IAGA code for the observatory that the data is from. This should
  match the IAGA code in section :ref:`app_cdf_v1_20_gattr_unique_id`.
- Date-time is the start date/time of the data in the file. The format for the date/time is
  described below.
- Cadence refers to the data sample period and is formatted as an ISO 8601 duration. Some sample
  ISO 8601 durations are given below.
- Publication-level is the PublicationLevel attribute from section :ref:`app_cdf_v1_20_gattr_unique_id`.

Filenames are in lower case. Files may contain any amount of data. The date/time string may
be used to indicate the amount of data in the file - more information on this is given in the
description of the date/time format.

ISO 8601 Duration Strings for Common Geomagnetic Sample Periods (V1.30)
#######################################################################

.. tabularcolumns:: |p{3cm}|c|

.. table::
    :widths: auto
    :align: center

    ============= =================
    Sample Period ISO 8601 duration
    ============= =================
    1 second      PT1S
    1 minute      PT1M
    Hourly means  PT1H
    Daily means   P1D
    Monthly means P1M
    Annual means  P1Y
    ============= =================

The table above is a set of examples. Other sample periods may be used provided that the sample
period used represents the vector data and conforms to ISO 8601.

Format of Date/Time Portion of Filename and Examples (V1.30)
############################################################

The date/time portion of the filename is formatted differently, depending on the amount of data
the file contains (the data coverage). 

.. tabularcolumns:: |p{3cm}|p{4cm}|p{8cm}|

.. table::
    :widths: auto
    :align: center

    +----------------+------------------+---------------------------------------------------------------+
    | Amount of data | Date/time format | Example filename                                              |
    | in file        |                  |                                                               |
    | (coverage)     |                  |                                                               |
    +================+==================+===============================================================+
    | One year       | YYYY             | esk_2000_pt1m_4.cdf – one year of final minute mean data from |
    |                |                  | Eskdalemuir for the year 2000                                 |
    +----------------+------------------+---------------------------------------------------------------+
    | One month      | YYYYMM           | ott_201401_pt1s_4.cdf – one month of final 1-second data from |
    |                |                  | Ottawa for January 2014                                       |
    +----------------+------------------+---------------------------------------------------------------+
    | One day        | YYYYMMDD         | gua_20100101_pt1m_3.cdf – one day of quasi-definitive minute  |
    |                |                  | mean data from Guam for 1st January 2010                      |
    +----------------+------------------+---------------------------------------------------------------+
    | One hour       | YYYYMMDD_HH      | naq_20020201_00_pt1m_2.cdf – one hour of provisional minute   |
    |                |                  | mean data from NAQ starting at midnight on 1st February 2002  |
    +----------------+------------------+---------------------------------------------------------------+
    | One minute     | YYYYMMDD_HHMM    | naq_20020120_0000_pt1s_2.cdf – one minute of provisional      |
    |                |                  | 1-second data from NAQ starting at 00:00 on 1st of February   |
    |                |                  | 2002                                                          |
    +----------------+------------------+---------------------------------------------------------------+
    | One second     | YYYYMMDD_HHMMSS  | naq_20020120_012300_pt1s_1.cdf – one second of raw 1-second   |
    |                |                  | data from NAQ at 01:23:00 on 20th January 2002                |
    +----------------+------------------+---------------------------------------------------------------+

- YYYY = four digit year (i.e. 2002)
- MM = two digit month (01 for January - 12 for December)
- DD = two digit day of month (01-31)
- HH = two digit hour (0-23)
- MM = two digit minute (0-59)
- SS = two digit second (0-59)

The start date/time of the data is expected to conform to the coverage: For a year of data the start date/time
is expected to be the start of the first day of the year. For a day of data the start date/time is expected to
be the start of the day. And so on for the other coverages listed in the table.

In the situations where the state date/time doesn't conform to this rule, or the amount of data is not
listed in the table, the data is considered to be a "fragment" (ie an incomplete part of a larger data
coverage). The filename for data fragments should use the full date/time, the same as for data with
a coverage of one second.


.. _app_cdf_tools:

Tools to Look at CDF Data
`````````````````````````

Once you have some CDF data you will want to look at it. The CDF toolset (that is installed for you
when you install CDF) provides programs to do this. The simplest way is (using a command shell or
DOS prompt): ::

    cdfdump [filename] | more

Which will display the entire contents of the file. The example file is formatted using cdfdump.
Other tools from the CDF toolset that may be useful include cdfexport and cdfedit.

Autoplot is a useful tool that can plot the time series data in ImagCDF data files. You can download
it from |autoplot|.

A number of packages provide access to CDF data. These include Matlab and IDL. A list is maintained
on the NASA CDF website: |cdf_software_list|

Octave may be able to read CDF data:|octave|. The Wolfram Language can
use CDF data via its NASACDF data format - |wolfram|.

Example Data File
`````````````````

The data in this example was extracted from a monthly file containing 1-second definitive data from
Abisko observatory for January 2019. Only the first two data records are shown for each variable.

.. highlight:: none

::

  File Info
  =========================================
  CDF File:     abk_201901_PT1S_4.cdf
  Version:      3.7.0

  Common Data Format (CDF)
  https://cdf.gsfc.nasa.gov
  Space Physics Data Facility
  NASA/Goddard Space Flight Center
  Greenbelt, Maryland 20771 USA
  (User support: gsfc-cdf-support@lists.nasa.gov)

  Format:       SINGLE
  Encoding:     IBMPC
  Majority:     ROW
  NumrVars:     0
  NumzVars:     5
  NumAttrs:     29 (21 global, 8 variable)
  Compression:  GZIP.1
  Checksum:     None
  LeapSecondLastUpdated:     20170101

  Global Attributes (21 attributes)
  =========================================
  FormatDescription (num:0) (1 entry):
          0 (CDF_CHAR/22):        "INTERMAGNET CDF format"
  FormatVersion (num:1) (1 entry):
          0 (CDF_CHAR/3):         "1.3"
  Title (num:2) (1 entry):
          0 (CDF_CHAR/28):        "Geomagnetic time series data"
  IagaCode (num:3) (1 entry):
          0 (CDF_CHAR/3):         "ABK"
  ElementsRecorded (num:4) (1 entry):
          0 (CDF_CHAR/4):         "XYZG"
  PublicationLevel (num:5) (1 entry):
          0 (CDF_CHAR/1):         "4"
  PublicationDate (1 entry):
       0 (CDF_TT2000/1):          2022-10-08T12:19:06.088000000
  ObservatoryName (num:7) (1 entry):
          0 (CDF_CHAR/6):         "Abisko"
  Latitude (num:8) (1 entry):
          0 (CDF_DOUBLE/1):       68.358
  Longitude (num:9) (1 entry):
          0 (CDF_DOUBLE/1):       18.823
  Elevation (num:10) (1 entry):
          0 (CDF_CHAR/5):         "380.0"
  Institution (num:11) (1 entry):
          0 (CDF_CHAR/27):        "Geological Survey of Sweden"
  VectorSensOrient (num:12) (1 entry):
          0 (CDF_CHAR/3):         "XYZ"
  StandardLevel (num:13) (1 entry):
          0 (CDF_CHAR/7):         "Partial"
  StandardName (num:14) (1 entry):
          0 (CDF_CHAR/20):        "INTERMAGNET_1-Second"
  PartialStandDesc (num:15) (1 entry):
          0 (CDF_CHAR/87):        "IMOS-03,IMOS-04,IMOS-05,IMOS-06,IMOS-11,IMOS-12,IMOS-14,IMOS-15,IMOS-22,IMOS-41,IMOS-42"
  Source (num:16) (1 entry):
          0 (CDF_CHAR/9):         "institute"
  TermsOfUse (num:17) (1 entry):
          0 (CDF_CHAR/62):        "http://www.intermagnet.org/data-donnee/data-eng.php#conditions"
  LeapSecondUpdated (num:18) (1 entry):
          0 (CDF_CHAR/8):         "20170101"
  ParentIdentifiers (num:19) (1 entry):
          0 (CDF_CHAR/13):        "ABKsec_4_0001"
  SamplingRate (num:20) (1 entry):
          0 (CDF_CHAR/7):         "1.0 sec"

  Variable Attributes (8 attributes)
  =========================================
  DEPEND_0 (num:21)
  DISPLAY_TYPE (num:22)
  LABLAXIS (num:23)
  FILLVAL (num:24)
  VALIDMIN (num:25)
  VALIDMAX (num:26)
  FIELDNAM (num:27)
  UNITS (num:28)

  Variable Information (0 rVariable, 5 zVariables)
  ===========================================================
  DataTimes             CDF_TT2000/1      0:[]    T/
  GeomagneticFieldX     CDF_DOUBLE/1      0:[]    T/
  GeomagneticFieldY     CDF_DOUBLE/1      0:[]    T/
  GeomagneticFieldZ     CDF_DOUBLE/1      0:[]    T/
  GeomagneticFieldG     CDF_DOUBLE/1      0:[]    T/

  Variable (5 variables)
  =========================================

  DataTimes (No: 0) (Recs: 2678400) (Compression: GZIP.6 BlockingFactor: 8192)
  ----------------------
  Data Type:           CDF_TT2000
  Dimensionality:      0:[]       (T/)
  Compression:         GZIP.6
  Pad value:           0000-01-01T00:00:00.000000000
  Written Records:     2678400/2678400(max)
  Allocated Records:   2678400/2678400(max)
  Blocking Factor:     8192 (records)
  Attribute Entries:
  Variable Data:
    Record # 1: 2019-01-01T00:00:00.000000000
    Record # 2: 2019-01-01T00:00:01.000000000
    ...

  GeomagneticFieldX (No: 1) (Recs: 2678400) (Compression: GZIP.6 BlockingFactor: 8192)
  -----------------
  Data Type:           CDF_DOUBLE
  Dimensionality:      0:[]       (T/)
  Compression:         GZIP.6
  Pad value:           -1.0e+30
  Written Records:     2678400/2678400(max)
  Allocated Records:   2678400/2678400(max)
  Blocking Factor:     8192 (records)
  Attribute Entries:
       DEPEND_0        (CDF_CHAR/22): "DataTimes"
       DISPLAY_TYPE    (CDF_CHAR/11): "time_series"
       LABLAXIS        (CDF_CHAR/1): "X"
       FILLVAL         (CDF_DOUBLE/1): nan
       VALIDMIN        (CDF_DOUBLE/1): -88880.0
       VALIDMAX        (CDF_DOUBLE/1): 88880.0
       FIELDNAM        (CDF_CHAR/27): "Geomagnetic Field Element X"
       UNITS           (CDF_CHAR/2): "nT"
  Variable Data:
    Record # 1: 11283.1
    Record # 2: 11283.0
    ...

  GeomagneticFieldY (No: 2) (Recs: 2678400) (Compression: GZIP.6 BlockingFactor: 8192)
  -----------------
  Data Type:           CDF_DOUBLE
  Dimensionality:      0:[]	(T/)  
  Compression:         GZIP.6
  Pad value:           -1.0e+30
  Written Records:     2678400/2678400(max)
  Allocated Records:   2678400/2678400(max)
  Blocking Factor:     8192 (records)
  Attribute Entries:
       DEPEND_0        (CDF_CHAR/22): "DataTimes"
       DISPLAY_TYPE    (CDF_CHAR/11): "time_series"
       LABLAXIS        (CDF_CHAR/1): "Y"
       FILLVAL         (CDF_DOUBLE/1): nan
       VALIDMIN        (CDF_DOUBLE/1): -88880.0
       VALIDMAX        (CDF_DOUBLE/1): 88880.0
       FIELDNAM        (CDF_CHAR/27): "Geomagnetic Field Element Y"
       UNITS           (CDF_CHAR/2): "nT"
  Variable Data:
    Record # 1: 1806.72
    Record # 2: 1806.67
    ...

  GeomagneticFieldZ (No: 3) (Recs: 2678400) (Compression: GZIP.6 BlockingFactor: 8192)
  -----------------
  Data Type:           CDF_DOUBLE
  Dimensionality:      0:[]	(T/)  
  Compression:         GZIP.6
  Pad value:           -1.0e+30
  Written Records:     2678400/2678400(max)
  Allocated Records:   2678400/2678400(max)
  Blocking Factor:     8192 (records)
  Attribute Entries:
       DEPEND_0        (CDF_CHAR/22): "DataTimes"
       DISPLAY_TYPE    (CDF_CHAR/11): "time_series"
       LABLAXIS        (CDF_CHAR/1): "Z"
       FILLVAL         (CDF_DOUBLE/1): nan
       VALIDMIN        (CDF_DOUBLE/1): -88880.0
       VALIDMAX        (CDF_DOUBLE/1): 88880.0
       FIELDNAM        (CDF_CHAR/27): "Geomagnetic Field Element Z"
       UNITS           (CDF_CHAR/2): "nT"
  Variable Data:
    Record # 1: 52087.4
    Record # 2: 52087.4
    ...

  GeomagneticFieldG (No: 4) (Recs: 2678400) (Compression: GZIP.6 BlockingFactor: 8192)
  -----------------
  Data Type:           CDF_DOUBLE
  Dimensionality:      0:[]	(T/)  
  Compression:         GZIP.6
  Pad value:           -1.0e+30
  Written Records:     2678400/2678400(max)
  Allocated Records:   2678400/2678400(max)
  Blocking Factor:     8192 (records)
  Attribute Entries:
       DEPEND_0        (CDF_CHAR/22): "DataTimes"
       DISPLAY_TYPE    (CDF_CHAR/11): "time_series"
       LABLAXIS        (CDF_CHAR/1): "G"
       FILLVAL         (CDF_DOUBLE/1): nan
       VALIDMIN        (CDF_DOUBLE/1): -88880.0
       VALIDMAX        (CDF_DOUBLE/1): 88880.0
       FIELDNAM        (CDF_CHAR/28): "Geomagnetic Field Element DF"
       UNITS           (CDF_CHAR/2): "nT"
  Variable Data:
    Record # 1: 0.0254182
    Record # 2: 0.0189378
    ...
