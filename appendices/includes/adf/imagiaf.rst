
.. _app_iaf:

INTERMAGNET Archive Format : IAF
--------------------------------


IAFV2.11 Binary Data Structure Format-32 Bit Words
``````````````````````````````````````````````````

.. tabularcolumns:: |>{\centering\arraybackslash}p{2.5cm}|>{\centering\arraybackslash}p{1cm}|p{4cm}|p{6cm}|

.. table::
    :widths: auto
    :align: center

    +-----------------+-------------+-----------------+----------------------------------------+
    | Section         | Word        | Field Name      | Comment                                |
    +=================+=============+=================+========================================+
    | Header          | 1           | Station ID      | eg: BOU = HEX(20 42 4F 55)             |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 2           | Year and day    | eg: 1989001; year 1989, day January 01 |
    |                 |             | number          |                                        |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 3           | Co-latitude     | (90° -                                 |
    |                 |             |                 | Latitude) \*                           |
    |                 |             |                 | 1000, to WGS-84                        |
    |                 |             |                 | datum                                  |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 4           | Longitude       | East Longitude                         |
    |                 |             |                 | \* 1000, to                            |
    |                 |             |                 | WGS-84 datum                           |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 5           | Elevation       | elevation in                           |
    |                 |             |                 | meters above                           |
    |                 |             |                 | sea level, to                          |
    |                 |             |                 | WGS-84 datum                           |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 6           | Orientation     | eg: XYZG =                             |
    |                 |             |                 | HEX(58 59 5A                           |
    |                 |             |                 | 47); HDZG =                            |
    |                 |             |                 | HEX(48 44 5A                           |
    |                 |             |                 | 47); XYZ =                             |
    |                 |             |                 | HEX(20 58 59                           |
    |                 |             |                 | 5A); and HDZ =                         |
    |                 |             |                 | HEX(20 48 44                           |
    |                 |             |                 | 5A)                                    |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 7           | Source          | eg: DMI =                              |
    |                 |             |                 | HEX(20 44 4D                           |
    |                 |             |                 | 49)                                    |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 8           | D conversion    | H/3438*10000                           |
    |                 |             |                 | where H=annual                         |
    |                 |             |                 | mean of H (set                         |
    |                 |             |                 | to 10000 for                           |
    |                 |             |                 | XYZG)                                  |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 9           | Data Quality    | IMAG = HEX (49                         |
    |                 |             |                 | 4D 41 47)                              |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 10          | Instrumentation | eg: LC(Linear                          |
    |                 |             |                 | Core) = HEX(20                         |
    |                 |             |                 | 20 4C 43) (or                          |
    |                 |             |                 | RC(Ring Core))                         |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 11          | K9 value in nT  | eg: 750                                |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 12          | Sampling rate   | eg: 125                                |
    |                 |             | (ms)            |                                        |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 13          | Sensor          | eg: XYZF, DIF,                         |
    |                 |             | orientation     | UVZ, HDZ, HDZF                         |
    |                 |             |                 | etc.                                   |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 14          | Publication     | eg: YYMM = 0806                        |
    |                 |             | Date            | (June 2008) HEX                        |
    |                 |             |                 | (30 38 30 36)                          |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 15          | IAF version     | HEX(04 tt 00                           |
    |                 |             | number and data | 00) version                            |
    |                 |             | type            | 2.11 and tt is                         |
    |                 |             |                 | data type flag                         |
    |                 |             |                 | (00 =                                  |
    |                 |             |                 | definitive, 01                         |
    |                 |             |                 | = quasi-definitive)                    |
    |                 |             |                 |                                        |
    |                 |             |                 |                                        |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 16          | Reserved for    |                                        |
    |                 |             | future use      |                                        |
    +-----------------+-------------+-----------------+----------------------------------------+
    | One minute data | 17          | 1440 mean       | Missing value =                        |
    |                 |             | minute values - | 999999                                 |
    |                 |             | element 1 (one  |                                        |
    |                 |             | day)            |                                        |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | ...         | 1440 mean       | Missing value =                        |
    |                 |             | minute values - | 999999                                 |
    |                 |             | element 2 (one  |                                        |
    |                 |             | day)            |                                        |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | ...         | 1440 mean       | Missing value =                        |
    |                 |             | minute values - | 999999                                 |
    |                 |             | element 3 (one  |                                        |
    |                 |             | day)            |                                        |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 5776        | 1440 mean       | Missing value =                        |
    |                 |             | minute values - | 999999                                 |
    |                 |             | element 4 (one  |                                        |
    |                 |             | day)            | Scalar                                 |
    |                 |             |                 | not recorded =                         |
    |                 |             |                 | 888888                                 |
    +-----------------+-------------+-----------------+----------------------------------------+
    | Mean hourly     | 5777        | 24 mean hourly  | Missing value =                        |
    | data            |             | values -        | 999999                                 |
    |                 |             | element 1       |                                        |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | ...         | 24 mean hourly  | Missing value =                        |
    |                 |             | values -        | 999999                                 |
    |                 |             | element 2       |                                        |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | ...         | 24 mean hourly  | Missing value =                        |
    |                 |             | values -        | 999999                                 |
    |                 |             | element 3       |                                        |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 5872        | 24 mean hourly  | Missing value =                        |
    |                 |             | values -        | 999999                                 |
    |                 |             | element 4       |                                        |
    +-----------------+-------------+-----------------+----------------------------------------+
    | Daily means     | 5873        | daily mean      | Missing value =                        |
    |                 |             | value element 1 | 999999                                 |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 5874        | daily mean      | Missing value =                        |
    |                 |             | value element 2 | 999999                                 |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 5875        | daily mean      | Missing value =                        |
    |                 |             | value element 3 | 999999                                 |
    +                 +-------------+-----------------+----------------------------------------+
    |                 | 5876        | daily mean      | Missing value =                        |
    |                 |             | value element 4 | 999999                                 |
    +-----------------+-------------+-----------------+----------------------------------------+
    | K indices       | 5877        | 8 K-values      | Missing value =                        |
    |                 |             |                 | 999                                    |
    +-----------------+-------------+-----------------+----------------------------------------+
    | Reserved        | 5885 - 5888 | Reserved for    |                                        |
    |                 |             | each            |                                        |
    |                 |             | contributing    |                                        |
    |                 |             | institution     |                                        |
    +-----------------+-------------+-----------------+----------------------------------------+


See  :numref:`sub_dat_1min_data_enc_iaf_211` for details.




IAFV2.10 Binary Data Structure Format-32 Bit Words
``````````````````````````````````````````````````

.. tabularcolumns:: |>{\centering\arraybackslash}p{2.5cm}|>{\centering\arraybackslash}p{1cm}|p{4cm}|p{6cm}|

.. table::
    :widths: auto
    :align: center

    +-----------------+-------------+-----------------+-----------------+
    | Section         | Word        | Field Name      | Comment         |
    +=================+=============+=================+=================+
    | Header          | 1           | Station ID      | eg: BOU =       |
    |                 |             |                 | HEX(20 42 4F    |
    |                 |             |                 | 55)             |
    +                 +-------------+-----------------+-----------------+
    |                 | 2           | Year and day    | eg: 1989001;    |
    |                 |             | number          | year 1989, day  |
    |                 |             |                 | January 01      |
    +                 +-------------+-----------------+-----------------+
    |                 | 3           | Co-latitude     | (90° -          |
    |                 |             |                 | Latitude) \*    |
    |                 |             |                 | 1000, to WGS-84 |
    |                 |             |                 | datum           |
    +                 +-------------+-----------------+-----------------+
    |                 | 4           | Longitude       | East Longitude  |
    |                 |             |                 | \* 1000, to     |
    |                 |             |                 | WGS-84 datum    |
    +                 +-------------+-----------------+-----------------+
    |                 | 5           | Elevation       | elevation in    |
    |                 |             |                 | meters above    |
    |                 |             |                 | sea level, to   |
    |                 |             |                 | WGS-84 datum    |
    +                 +-------------+-----------------+-----------------+
    |                 | 6           | Orientation     | eg: XYZG =      |
    |                 |             |                 | HEX(58 59 5A    |
    |                 |             |                 | 47); HDZG =     |
    |                 |             |                 | HEX(48 44 5A    |
    |                 |             |                 | 47); XYZ =      |
    |                 |             |                 | HEX(20 58 59    |
    |                 |             |                 | 5A); and HDZ =  |
    |                 |             |                 | HEX(20 48 44    |
    |                 |             |                 | 5A)             |
    +                 +-------------+-----------------+-----------------+
    |                 | 7           | Source          | eg: DMI =       |
    |                 |             |                 | HEX(20 44 4D    |
    |                 |             |                 | 49)             |
    +                 +-------------+-----------------+-----------------+
    |                 | 8           | D conversion    | H/3438*10000    |
    |                 |             |                 | where H=annual  |
    |                 |             |                 | mean of H (set  |
    |                 |             |                 | to 10000 for    |
    |                 |             |                 | XYZG)           |
    +                 +-------------+-----------------+-----------------+
    |                 | 9           | Data Quality    | IMAG = HEX (49  |
    |                 |             |                 | 4D 41 47)       |
    +                 +-------------+-----------------+-----------------+
    |                 | 10          | Instrumentation | eg: LC(Linear   |
    |                 |             |                 | Core) = HEX(20  |
    |                 |             |                 | 20 4C 43) (or   |
    |                 |             |                 | RC(Ring Core))  |
    +                 +-------------+-----------------+-----------------+
    |                 | 11          | K9 value in nT  | eg: 750         |
    +                 +-------------+-----------------+-----------------+
    |                 | 12          | Sampling rate   | eg: 125         |
    |                 |             | (ms)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | 13          | Sensor          | eg: XYZF, DIF,  |
    |                 |             | orientation     | UVZ, HDZ, HDZF  |
    |                 |             |                 | etc.            |
    +                 +-------------+-----------------+-----------------+
    |                 | 14          | Publication     | eg: YYMM = 0806 |
    |                 |             | Date            | (June 2008) HEX |
    |                 |             |                 | (30 38 30 36)   |
    +                 +-------------+-----------------+-----------------+
    |                 | 15          | IAF version     | HEX(03 00 00    |
    |                 |             | number          | 00) version     |
    |                 |             |                 | 2.10            |
    +                 +-------------+-----------------+-----------------+
    |                 | 16          | Reserved for    |                 |
    |                 |             | future use      |                 |
    +-----------------+-------------+-----------------+-----------------+
    | One minute data | 17          | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 1 (one  |                 |
    |                 |             | day)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 2 (one  |                 |
    |                 |             | day)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 3 (one  |                 |
    |                 |             | day)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | 5776        | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 4 (one  |                 |
    |                 |             | day)            | Scalar          |
    |                 |             |                 | not recorded =  |
    |                 |             |                 | 888888          |
    +-----------------+-------------+-----------------+-----------------+
    | Mean hourly     | 5777        | 24 mean hourly  | Missing value = |
    | data            |             | values -        | 999999          |
    |                 |             | element 1       |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 24 mean hourly  | Missing value = |
    |                 |             | values -        | 999999          |
    |                 |             | element 2       |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 24 mean hourly  | Missing value = |
    |                 |             | values -        | 999999          |
    |                 |             | element 3       |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | 5872        | 24 mean hourly  | Missing value = |
    |                 |             | values -        | 999999          |
    |                 |             | element 4       |                 |
    +-----------------+-------------+-----------------+-----------------+
    | Daily means     | 5873        | daily mean      | Missing value = |
    |                 |             | value element 1 | 999999          |
    +                 +-------------+-----------------+-----------------+
    |                 | 5874        | daily mean      | Missing value = |
    |                 |             | value element 2 | 999999          |
    +                 +-------------+-----------------+-----------------+
    |                 | 5875        | daily mean      | Missing value = |
    |                 |             | value element 3 | 999999          |
    +                 +-------------+-----------------+-----------------+
    |                 | 5876        | daily mean      | Missing value = |
    |                 |             | value element 4 | 999999          |
    +-----------------+-------------+-----------------+-----------------+
    | K indices       | 5877        | 8 K-values      | Missing value = |
    |                 |             |                 | 999             |
    +-----------------+-------------+-----------------+-----------------+
    | Reserved        | 5885 - 5888 | Reserved for    |                 |
    |                 |             | each            |                 |
    |                 |             | contributing    |                 |
    |                 |             | institution     |                 |
    +-----------------+-------------+-----------------+-----------------+


IAFV2.10 (2010 to 2013)
"""""""""""""""""""""""


Words 1 to 16 comprise the header section containing a mixture
of text and numeric fields, including a 3-letter observatory
identification preceded with a space [hex20] (ID) code, the
year concatenated with the day of the year, co-latitude,
longitude, elevation, reported orientation, originating
organization, a D-conversion factor, data quality,
instrumentation, K-9, sampling rate, sensor orientation,
publication date and format version/data type. Latitude,
longitude/colatitude and elevation must be given using the
WGS-84 datum. From 2010 onward, the orientation codes "XYZ" and
"HDZ" have been added to "XYZG" and "HDZG" where "G" represents
ΔF (see description below). These new codes indicate that the
observatory is recording 3 elements only (no scalar
instrument). The D-conversion factor is a fixed value used only
in the graphics portion of the access software to allow
Declination to be plotted in minutes of arc and equivalent
nanoteslas (nT). It is given as H/3438*10000, where H is the
annual mean value of the horizontal intensity. Example: If H is
16500 D will be 47993(Integer). When XYZG or XYZ is used, the
D-conversion factor should be set to 10000.

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
1.10, two (0x02) represents version 2.00 and three (0x03)
represents version 2.10. The other three bytes of word 15 are
reserved for future use and padded with zeros. Word 16 is
reserved for future use.

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
record 999999 (missing value), this is done because the
4\ :sup:`th` element in the data is a quality check for minute
mean data and this quality check is meaningless for hourly
means. Words 5873-5876 store the 4 daily mean values. From 2009
onward, word 5876 always record 999999 (missing value) because
the quality check for daily means is also meaningless. From
2009 onward, the last 4 words (5885-5888) are available for
each contributing institution. Missing data for minute, hour,
and day values are stored as "999999". From 2010 onward, if a
scalar instrument is not used (so no data is recorded in the
fourth element) the value "888888" should be used instead of
"999999". Missing K-Index values are stored as "999".


IAFV2.00 Binary Data Structure Format-32 Bit Words
``````````````````````````````````````````````````

.. tabularcolumns:: |>{\centering\arraybackslash}p{2.5cm}|>{\centering\arraybackslash}p{1cm}|p{4cm}|p{6cm}|

.. table::
    :widths: auto
    :align: center

    +-----------------+-------------+-----------------+-----------------+
    | Section         | Word        | Field Name      | Comment         |
    +=================+=============+=================+=================+
    | Header          | 1           | Station ID      | eg: BOU =       |
    |                 |             |                 | HEX(20 42 4F    |
    |                 |             |                 | 55)             |
    +                 +-------------+-----------------+-----------------+
    |                 | 2           | Year and day    | eg: 1989001;    |
    |                 |             | number          | year 1989, day  |
    |                 |             |                 | January 01      |
    +                 +-------------+-----------------+-----------------+
    |                 | 3           | Co-latitude     | (90° -          |
    |                 |             |                 | Latitude) \*    |
    |                 |             |                 | 1000, to WGS-84 |
    |                 |             |                 | datum           |
    +                 +-------------+-----------------+-----------------+
    |                 | 4           | Longitude       | East Longitude  |
    |                 |             |                 | \* 1000, to     |
    |                 |             |                 | WGS-84 datum    |
    +                 +-------------+-----------------+-----------------+
    |                 | 5           | Elevation       | elevation in    |
    |                 |             |                 | meters above    |
    |                 |             |                 | sea level, to   |
    |                 |             |                 | WGS-84 datum    |
    +                 +-------------+-----------------+-----------------+
    |                 | 6           | Orientation     | eg: XYZG =      |
    |                 |             |                 | HEX(58 59 5A    |
    |                 |             |                 | 47); and HDZG = |
    |                 |             |                 | HEX(48 44 5A    |
    |                 |             |                 | 47)             |
    +                 +-------------+-----------------+-----------------+
    |                 | 7           | Source          | eg: DMI =       |
    |                 |             |                 | HEX(20 44 4D    |
    |                 |             |                 | 49)             |
    +                 +-------------+-----------------+-----------------+
    |                 | 8           | D conversion    | H/3438*10000    |
    |                 |             |                 | where H=annual  |
    |                 |             |                 | mean of H (set  |
    |                 |             |                 | to 10000 for    |
    |                 |             |                 | XYZG)           |
    +                 +-------------+-----------------+-----------------+
    |                 | 9           | Data Quality    | IMAG = HEX (49  |
    |                 |             |                 | 4D 41 47)       |
    +                 +-------------+-----------------+-----------------+
    |                 | 10          | Instrumentation | eg: LC(Linear   |
    |                 |             |                 | Core) = HEX(20  |
    |                 |             |                 | 20 4C 43) (or   |
    |                 |             |                 | RC(Ring Core))  |
    +                 +-------------+-----------------+-----------------+
    |                 | 11          | K9 value in nT  | eg: 750         |
    +                 +-------------+-----------------+-----------------+
    |                 | 12          | Sampling rate   | eg: 125         |
    |                 |             | (ms)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | 13          | Sensor          | eg: XYZF, DIF,  |
    |                 |             | orientation     | UVZ, HDZ, HDZF  |
    |                 |             |                 | etc.            |
    +                 +-------------+-----------------+-----------------+
    |                 | 14          | Publication     | eg: YYMM = 0806 |
    |                 |             | Date            | (June 2008) HEX |
    |                 |             |                 | (30 38 30 36)   |
    +                 +-------------+-----------------+-----------------+
    |                 | 15          | IAF version     | HEX(02 00 00    |
    |                 |             | number          | 00) version     |
    |                 |             |                 | 2.00            |
    +                 +-------------+-----------------+-----------------+
    |                 | 16          | Reserved for    |                 |
    |                 |             | future use      |                 |
    +-----------------+-------------+-----------------+-----------------+
    | One minute data | 17          | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 1 (one  |                 |
    |                 |             | day)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 2 (one  |                 |
    |                 |             | day)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 3 (one  |                 |
    |                 |             | day)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | 5776        | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 4 (one  |                 |
    |                 |             | day)            |                 |
    +-----------------+-------------+-----------------+-----------------+
    | Mean hourly     | 5777        | 24 mean hourly  | Missing value = |
    | data            |             | values -        | 999999          |
    |                 |             | element 1       |                 |
    +                 +-------------+-----------------+-----------------+
    |                 |             | values -        | 999999          |
    |                 |             | element 2       |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 24 mean hourly  | Missing value = |
    |                 |             | values -        | 999999          |
    |                 |             | element 3       |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | 5872        | 24 mean hourly  | Missing value = |
    |                 |             | values -        | 999999          |
    |                 |             | element 4       |                 |
    +-----------------+-------------+-----------------+-----------------+
    | Daily means     | 5873        | daily mean      | Missing value = |
    |                 |             | value element 1 | 999999          |
    +                 +-------------+-----------------+-----------------+
    |                 | 5874        | daily mean      | Missing value = |
    |                 |             | value element 2 | 999999          |
    +                 +-------------+-----------------+-----------------+
    |                 | 5875        | daily mean      | Missing value = |
    |                 |             | value element 3 | 999999          |
    +                 +-------------+-----------------+-----------------+
    |                 | 5876        | daily mean      | Missing value = |
    |                 |             | value element 4 | 999999          |
    +-----------------+-------------+-----------------+-----------------+
    | K indices       | 5877        | 8 K-values      | Missing value = |
    |                 |             |                 | 999             |
    +-----------------+-------------+-----------------+-----------------+
    | Reserved        | 5885 - 5888 | Reserved for    |                 |
    |                 |             | each            |                 |
    |                 |             | contributing    |                 |
    |                 |             | institution     |                 |
    +-----------------+-------------+-----------------+-----------------+


IAFV2.00 (2009)
"""""""""""""""

Words 1 to 16 comprise the header section containing a mixture
of text and numeric fields, including a 3-letter observatory
identification preceded with a space [hex20] (ID) code, the
year concatenated with the day of the year, co-latitude,
longitude, elevation, reported orientation, originating
organization, a D-conversion factor, data quality,
instrumentation, K-9, sampling rate, sensor orientation,
publication date and format version/data type. Latitude,
longitude/colatitude and elevation must be given using the
WGS-84 datum. From 2009 onward, the orientation must be "XYZG"
or "HDZG" where "G" represents ΔF (see description below). The
D-conversion factor is a fixed value used only in the graphics
portion of the access software to allow Declination to be
plotted in minutes of arc and equivalent nanoteslas (nT). It is
given as H/3438*10000, where H is the annual mean value of the
horizontal intensity. Example: If H is 16500 D will be
47993(Integer). When XYZG is used, the D-conversion factor
should be set to 10000.

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
Format version number code provided by INTERMAGNET. It takes
the form of a binary single byte number ranging from 0 to 255.
Zero (0x00) represents version 1.00, one (0x01) represents
version 1.10 and two (0x02) represents version 2.00. The other
three bytes of word 15 are reserved for future use and padded
with zeros. Word 16 is reserved for future use.

Words 17-5776 contain the minute values of the 4 geomagnetic
elements (successively X,Y,Z,G or H,D,Z,G ) for the day. From
2009 onward, the 4th element contains the difference between
the square root of the sum of the squares of the variometer
components, F(v), and the total field from an independent
scalar recording, F(s). This difference, ΔF, is defined as F(v)
- F(s). Both F(v) and F(s) must be corrected to the location in
the observatory where absolute geomagnetic observations are
made. When F(s) is missing or both F(s) and F(v) are missing,
ΔF must be set to 999999. When F(v) only is missing, ΔF must be
set to -F(s). The values of the 4 elements are stored in
tenth-units with an implied decimal point. Thus, an H value of
21305.6 is stored (in tenth-nT) as 213056 with a decimal point
implied between the last and next-to-last digits. Words
5777-5872 are used for the hourly mean values of the successive
4 elements. From 2009 onward, words 5849-5872 always record
999999 (missing value), this is done because the 4th element in
the data is a quality check for minute mean data and this
quality check is meaningless for hourly means. Words 5873-5876
store the 4 daily mean values. From 2009 onward, word 5876
always record 999999 (missing value) because the quality check
for daily means is also meaningless. From 2009 onward, the last
4 words (5885-5888) are available for each contributing
institution. Missing data for minute, hour, and day values are
stored as "999999". Missing K-Index values are stored as "999".


IAFV1.10 Binary Data Structure Format-32 Bit Words
``````````````````````````````````````````````````

.. tabularcolumns:: |>{\centering\arraybackslash}p{2.5cm}|>{\centering\arraybackslash}p{1cm}|p{4cm}|p{6cm}|

.. table::
    :widths: auto
    :align: center

    +-----------------+-------------+-----------------+-----------------+
    | Section         | Word        | Field Name      | Comment         |
    +=================+=============+=================+=================+
    | Header          | 1           | Station ID      | eg: BOU =       |
    |                 |             |                 | HEX(20 42 4F    |
    |                 |             |                 | 55)             |
    +                 +-------------+-----------------+-----------------+
    |                 | 2           | Year and day    | eg: 1989001;    |
    |                 |             | number          | year 1989, day  |
    |                 |             |                 | January 01      |
    +                 +-------------+-----------------+-----------------+
    |                 | 3           | Co-latitude     | (90° -          |
    |                 |             |                 | Latitude) \*    |
    |                 |             |                 | 1000, to WGS-84 |
    |                 |             |                 | datum           |
    +                 +-------------+-----------------+-----------------+
    |                 | 4           | Longitude       | East Longitude  |
    |                 |             |                 | \* 1000, to     |
    |                 |             |                 | WGS-84 datum    |
    +                 +-------------+-----------------+-----------------+
    |                 | 5           | Elevation       | elevation in    |
    |                 |             |                 | meters above    |
    |                 |             |                 | sea level, to   |
    |                 |             |                 | WGS-84 datum    |
    +                 +-------------+-----------------+-----------------+
    |                 | 6           | Orientation     | eg: XYZF =      |
    |                 |             |                 | HEX(58 59 5A    |
    |                 |             |                 | 46); and HDZF = |
    |                 |             |                 | HEX(48 44 5A    |
    |                 |             |                 | 46)             |
    +                 +-------------+-----------------+-----------------+
    |                 | 7           | Source          | eg: DMI =       |
    |                 |             |                 | HEX(20 44 4D    |
    |                 |             |                 | 49)             |
    +                 +-------------+-----------------+-----------------+
    |                 | 8           | D conversion    | H/3438*10000    |
    |                 |             |                 | where H=annual  |
    |                 |             |                 | mean of H (set  |
    |                 |             |                 | to 10000 for    |
    |                 |             |                 | XYZF)           |
    +                 +-------------+-----------------+-----------------+
    |                 | 9           | Data Quality    | IMAG = HEX (49  |
    |                 |             |                 | 4D 41 47)       |
    +                 +-------------+-----------------+-----------------+
    |                 | 10          | Instrumentation | eg: LC(Linear   |
    |                 |             |                 | Core) = HEX(20  |
    |                 |             |                 | 20 4C 43) (or   |
    |                 |             |                 | RC(Ring Core))  |
    +                 +-------------+-----------------+-----------------+
    |                 | 11          | K9 value in nT  | eg: 750         |
    +                 +-------------+-----------------+-----------------+
    |                 | 12          | Sampling rate   | eg: 125         |
    |                 |             | (ms)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | 13          | Sensor          | eg: XYZF, DIF,  |
    |                 |             | orientation     | UVZ, HDZ, HDZF  |
    |                 |             |                 | etc.            |
    +                 +-------------+-----------------+-----------------+
    |                 | 14          | Publication     | eg: YYMM = 0806 |
    |                 |             | Date            | (June 2008) HEX |
    |                 |             |                 | (30 38 30 36)   |
    +                 +-------------+-----------------+-----------------+
    |                 | 15          | IAF version     | HEX(01 00 00    |
    |                 |             | number          | 00) IAFV1.10    |
    +                 +-------------+-----------------+-----------------+
    |                 | 16          | Reserved for    |                 |
    |                 |             | future use      |                 |
    +-----------------+-------------+-----------------+-----------------+
    | One minute data | 17          | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 1 (one  |                 |
    |                 |             | day)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 2 (one  |                 |
    |                 |             | day)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 3 (one  |                 |
    |                 |             | day)            |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | 5776        | 1440 mean       | Missing value = |
    |                 |             | minute values - | 999999          |
    |                 |             | element 4 (one  |                 |
    |                 |             | day)            |                 |
    +-----------------+-------------+-----------------+-----------------+
    | Mean hourly     | 5777        | 24 mean hourly  | Missing value = |
    | data            |             | values -        | 999999          |
    |                 |             | element 1       |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 24 mean hourly  | Missing value = |
    |                 |             | values -        | 999999          |
    |                 |             | element 2       |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | ...         | 24 mean hourly  | Missing value = |
    |                 |             | values -        | 999999          |
    |                 |             | element 3       |                 |
    +                 +-------------+-----------------+-----------------+
    |                 | 5872        | 24 mean hourly  | Missing value = |
    |                 |             | values -        | 999999          |
    |                 |             | element 4       |                 |
    +-----------------+-------------+-----------------+-----------------+
    | Daily means     | 5873        | daily mean      | Missing value = |
    |                 |             | value element 1 | 999999          |
    +                 +-------------+-----------------+-----------------+
    |                 | 5874        | daily mean      | Missing value = |
    |                 |             | value element 2 | 999999          |
    +                 +-------------+-----------------+-----------------+
    |                 | 5875        | daily mean      | Missing value = |
    |                 |             | value element 3 | 999999          |
    +                 +-------------+-----------------+-----------------+
    |                 | 5876        | daily mean      | Missing value = |
    |                 |             | value element 4 | 999999          |
    +-----------------+-------------+-----------------+-----------------+
    | K indices       | 5877        | 8 digitally     | Missing value = |
    |                 |             | derived         | 999             |
    |                 |             | K-values        |                 |
    +-----------------+-------------+-----------------+-----------------+
    | Reserved        | 5885 - 5888 | Reserved for    |                 |
    |                 |             | future use = 0  |                 |
    +-----------------+-------------+-----------------+-----------------+

IAFV1.10 (2008)
"""""""""""""""

Words 1 to 16 comprise the header section containing a mixture
of text and numeric fields, including a 3-letter observatory
identification preceded with a space [hex20] (ID) code, the
year concatenated with the day of the year, co-latitude,
longitude, elevation, reported orientation, originating
organization, a D-conversion factor, data quality,
instrumentation, K-9, sampling rate, sensor orientation,
publication date and format version/data type. Latitude,
longitude/colatitude and elevation must be given using the
WGS-84 datum. The orientation must be "XYZF" or "HDZF". If the
F element is not measured, it must be filled with 999999 in the
data section. The D-conversion factor is a fixed value used
only in the graphics portion of the access software to allow
Declination to be plotted in minutes of arc and equivalent
nanoteslas (nT). It is given as H/3438*10000, where H is the
annual mean value of the horizontal intensity. Example: If H is
16500 D will be 47993(Integer). When XYZF is used, the
D-conversion factor should be set to 10000.

ASCII values, such as the observatory ID and orientation, are
also stored as 32-bit words, but are coded as the hexadecimal
byte-string corresponding to the ASCII string. For example, the
string "HDZF" is coded as the sequence "48 44 5A 46".

Word 11 is the K-9 value for the observatory in nT, word 12 is
the digital sampling rate in msec, and word 13 is the sensor
orientation. Sensor orientation could be XYZF, DIF, UVZ, HDZ,
HDZF etc. and should indicates which components are actually
measured. If a three component sensor orientation is used, a
space must be added at the end. Word 14 is the publication date
encoded as 4 ASCII bytes "YYMM" provided by INTERMAGNET. The
high byte (left most) of word 15 is the INTERMAGNET Archive
Format version number code provided by INTERMAGNET. It takes
the form of a binary single byte number ranging from 0 to 255.
Zero (0x00) represents version 1.00 and one (0x01) represents
version 1.10. The other three bytes of word 15 are reserved for
future use and padded with zeros. Word 16 is reserved for
future use.

Words 17-5776 contain the minute values of the 4 components
(successively X,Y,Z,F or H,D,Z,F) for the day. The 4th
component "F" should be included only if it is measured from a
scalar instrument independent of the other 3 components
otherwise it must be filled with 999999. The values of the 4
components are stored in tenth-units with an implied decimal
point. Thus, an H value of 21305.6 is stored (in tenth-nT) as
213056 with a decimal point implied between the last and
next-to-last digits and a D value of 527.6 is stored (in
tenth-minutes) as 5276 also with a decimal point implied
between the last and next-to-last digits. Words 5777-5872 are
used for the hourly mean values of the successive 4 components.
Words 5873-5876 store the 4 daily mean values. Words 5877-5884
contain the K-Index*10. The last 4 words (5885-5888) are
reserved for future use and padded with zeros. Missing data for
minute, hour, and day values are stored as "999999". Missing
K-Index and Ak values are stored as "999".


IAFV1.00 Binary Data Structure Format-32 Bit Words
``````````````````````````````````````````````````

.. tabularcolumns:: |>{\centering\arraybackslash}p{2.5cm}|>{\centering\arraybackslash}p{1cm}|p{4cm}|p{6cm}|

.. table::
    :widths: auto
    :align: center

    +-----------------+-------------+-----------------+-----------------------------------------+
    | Section         | Word        | Field Name      | Comment                                 |
    +=================+=============+=================+=========================================+
    | Header          | 1           | Station ID      | eg: BOU =                               |
    |                 |             |                 | HEX(20 42 4F                            |
    |                 |             |                 | 55)                                     |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 2           | Year and day    | eg: 1989001;                            |
    |                 |             | number          | year 1989, day                          |
    |                 |             |                 | January 01                              |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 3           | Co-latitude     | (90° -                                  |
    |                 |             |                 | Latitude) \*                            |
    |                 |             |                 | 1000, to WGS-84                         |
    |                 |             |                 | datum                                   |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 4           | Longitude       | East Longitude                          |
    |                 |             |                 | \* 1000, to                             |
    |                 |             |                 | WGS-84 datum                            |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 5           | Elevation       | elevation in                            |
    |                 |             |                 | meters above                            |
    |                 |             |                 | sea level, to                           |
    |                 |             |                 | WGS-84 datum                            |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 6           | Orientation     | eg: XYZF =                              |
    |                 |             |                 | HEX(58 59 5A                            |
    |                 |             |                 | 46); and HDZF =                         |
    |                 |             |                 | HEX(48 44 5A                            |
    |                 |             |                 | 46)                                     |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 7           | Source          | eg: DMI = HEX(20 44 4D 49)              |
    |                 |             |                 |                                         |
    |                 |             |                 |                                         |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 8           | D conversion    | H/3438*10000                            |
    |                 |             |                 | where H=annual                          |
    |                 |             |                 | mean of H                               |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 9           | Data Quality    | IMAG = HEX (49                          |
    |                 |             |                 | 4D 41 47)                               |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 10          | Instrumentation | eg: LC(Linear                           |
    |                 |             |                 | Core) = HEX(20                          |
    |                 |             |                 | 20 4C 43) (or                           |
    |                 |             |                 | RC(Ring Core))                          |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 11          | K9 value in nT  | eg: 750                                 |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 12          | Sampling rate   | eg: 125                                 |
    |                 |             | (ms)            |                                         |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 13          | Sensor          | eg: XYZF, DIF,                          |
    |                 |             | orientation     | UVZ, HDZ, HDZF                          |
    |                 |             |                 | etc.                                    |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 14          | Reserved for    |                                         |
    |                 |             | future use      |                                         |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 15          | IAF version     | HEX(00 00 00                            |
    |                 |             | number          | 00) IAFV1.00                            |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 16          | Reserved for    |                                         |
    |                 |             | each            |                                         |
    |                 |             | contributing    |                                         |
    |                 |             | institution     |                                         |
    +-----------------+-------------+-----------------+-----------------------------------------+
    | One minute data | 17          | 1440 mean       | Missing value =                         |
    |                 |             | minute values - | 999999                                  |
    |                 |             | element 1 (one  |                                         |
    |                 |             | day)            |                                         |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | ...         | 1440 mean       | Missing value =                         |
    |                 |             | minute values - | 999999                                  |
    |                 |             | element 2 (one  |                                         |
    |                 |             | day)            |                                         |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | ...         | 1440 mean       | Missing value =                         |
    |                 |             | minute values - | 999999                                  |
    |                 |             | element 3 (one  |                                         |
    |                 |             | day)            |                                         |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 5776        | 1440 mean       | Missing value =                         |
    |                 |             | minute values - | 999999                                  |
    |                 |             | element 4 (one  |                                         |
    |                 |             | day)            |                                         |
    +-----------------+-------------+-----------------+-----------------------------------------+
    | Mean hourly     | 5777        | 24 mean hourly  | Missing value =                         |
    | data            |             | values -        | 999999                                  |
    |                 |             | element 1       |                                         |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | ...         | 24 mean hourly  | Missing value =                         |
    |                 |             | values -        | 999999                                  |
    |                 |             | element 2       |                                         |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | ...         | 24 mean hourly  | Missing value =                         |
    |                 |             | values -        | 999999                                  |
    |                 |             | element 3       |                                         |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 5872        | 24 mean hourly  | Missing value =                         |
    |                 |             | values -        | 999999                                  |
    |                 |             | element 4       |                                         |
    +-----------------+-------------+-----------------+-----------------------------------------+
    | Daily means     | 5873        | daily mean      | Missing value =                         |
    |                 |             | value element 1 | 999999                                  |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 5874        | daily mean      | Missing value =                         |
    |                 |             | value element 2 | 999999                                  |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 5875        | daily mean      | Missing value =                         |
    |                 |             | value element 3 | 999999                                  |
    +                 +-------------+-----------------+-----------------------------------------+
    |                 | 5876        | daily mean      | Missing value =                         |
    |                 |             | value element 4 | 999999                                  |
    +-----------------+-------------+-----------------+-----------------------------------------+
    | K indices       | 5877        | 8 digitally     | Missing value =                         |
    |                 |             | derived         | 999                                     |
    |                 |             | K-values        |                                         |
    +-----------------+-------------+-----------------+-----------------------------------------+
    | Reserved        | 5885 - 5888 | Reserved for    | see :numref:`sub_dat_1min_data_enc_iaf` |
    |                 |             | future use = 0  | for details on word   5885              |
    |                 |             |                 |                                         |
    |                 |             |                 |                                         |
    +-----------------+-------------+-----------------+-----------------------------------------+

IAFV1.00 (2007 and before)
""""""""""""""""""""""""""

Words 1 to 16 comprise the header section containing a mixture
of text and numeric fields, including a 3-letter observatory
identification preceded with a space [hex20] (ID) code, the
year concatenated with the day of the year, co-latitude,
longitude, elevation, reported orientation, originating
organization, a D-conversion factor, data quality,
instrumentation, K-9, sampling rate and sensor orientation.
Latitude, longitude/colatitude and elevation must be given
using the WGS-84 datum. From 1991 to 2005, the fourth component
is the total field from either a scalar (independent)
instrument or the total field calculated from the main
observatory instrument. INTERMAGNET has a list of which
observatories supplied which type of total field value between
1991 and 2005 and this list is available as a spreadsheet in
the archive viewer software. The D-conversion factor is a fixed
value used only in the graphics portion of the access software
to allow Declination to be plotted in minutes of arc and
equivalent nanoteslas (nT). It is given as H/3438*10000, where
H is the annual mean value of the horizontal intensity.
Example: If H is 16500 D will be 47993(Integer). This
conversion factor only applies to HDZ observatory data supplied
before 2005.

ASCII values, such as the observatory ID and orientation, are
also stored as 32-bit words, but are coded as the hexadecimal
byte-string corresponding to the ASCII string. For example, the
string "HDZF" is coded as the sequence "48 44 5A 46".

Word 11 is the K-9 value for the observatory in nT, word 12 is
the digital sampling rate in msec, and word 13 is the sensor
orientation. Sensor orientation could be XYZF, DIF, UVZ, HDZ,
HDZF etc. and should indicates which components are actually
measured. If a three component sensor orientation is used, a
space must be added at the end. Word 14-15 are reserved for
future use and padded with zeros. In version 1.10 and later,
word 15 have been defined to represent the version number.
Previously, it should have been coded to zero by IMOs, that is
the reason this word was chosen for the version number (zero
represents version 1.00). Word 16 is set aside for each
contributing institution to use as they wish, provided it is
coded as a 32-bit binary value.

Words 17-5776 contain the minute values of the 4 components
(successively X,Y,Z,F or H,D,Z,F) for the day. Until 2005, the
4th component could contain "F" from either a scalar or
calculated from the vector instrument. From 2006 onward, the
4th component contains "F" only if it is measured from a scalar
instrument independent of the other 3 components otherwise it
must be filled with 999999. The values of the 4 components are
stored in tenth-units with an implied decimal point. Thus, an H
value of 21305.6 is stored (in tenth-nT) as 213056 with a
decimal point implied between the last and next-to-last digits
and a D value of 527.6 is stored (in tenth-minutes) as 5276
also\* with a decimal point implied between the last and
nextto- last digits. Words 5777-5872 are used for the hourly
mean values of the successive 4 components. Words 5873-5876
store the 4 daily mean values. Prior to the 1994 CD-ROM, words
5877-5884 held the 8 (K-Index*10) values for the day. The true
IAGA K-Index could be obtained from these K-Index*10 values by
truncating the second (least significant) digit. From 1994
onward, words 5877-5884 contain the K-Index*10. Until 1998,
word 5885 contained the equivalent daily amplitude index (Ak).
From 1999 onward, word 5885 is reserved for future use and
padded with zeros. The last 3 words (5886-5888) are reserved
for future use and padded with zeros. Missing data for minute,
hour, and day values are stored as "999999". Missing K-Index
and Ak values are stored as "999".
