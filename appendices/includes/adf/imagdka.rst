.. _app_dka:


INTERMAGNET Format for K-Index ASCII File (DKA)
-----------------------------------------------

A DKA file contains local geomagnetic K-indices for an observatory for
one calendar year. Beginning with the 2005 archive, INTERMAGNET generates
DKA files from the K-index values contained in the INTERMAGNET Archive
Format (IAF) records. Each daily record contains eight K-indices, one for
each three-hour universal-time (UT) interval, and their daily sum (SK).

The archive filename is XXXYYK.DKA, where XXX is the three-letter
observatory code and YY is the last two digits of the year. For example,
OTT15K.DKA contains Ottawa K-indices for 2015.

Description of the Header Block
```````````````````````````````

The header identifies the observatory by its three-letter code, its
geographical latitude and longitude, the year of the K-indices, and the
observatory's K9 limit in nanoteslas (nT). Longitude is expressed in degrees
east. The final header line names the daily-record fields. Blank lines
separate the header elements and the data records.

For example, the header for Ottawa in 2015 is:

.. highlight:: none

::

                                 OTT
                    Geographical latitude:    45.403 N
                    Geographical longitude:  284.448 E

              K-index values for 2015     (K9-limit =  750 nT)

    DA-MON-YR  DAY #    1    2    3    4      5    6    7    8       SK

Description of the Daily Records
````````````````````````````````

A daily record contains the date, day of year, eight integer K-indices and
the daily K-index sum (SK). The data fields are right-justified and follow
the alignment illustrated in the example below. The example record is 69
characters long, excluding the line ending.

::

    01-JAN-15   001     2    1    1    0      2    1    1    2       10

.. table:: Daily-record fields
   :class: longtable
   :align: center

   +------------+------------------------------------------------------------+
   | Field      | Description                                                |
   +============+============================================================+
   | DA-MON-YR  | Date in DD-MMM-YY format, with a three-letter              |
   |            | uppercase English month abbreviation.                      |
   +------------+------------------------------------------------------------+
   | DAY #      | Day of year, numbered 001 to 365 (366 in a                 |
   |            | leap year).                                                |
   +------------+------------------------------------------------------------+
   | 1 to 8     | K-indices for consecutive three-hour UT intervals          |
   |            | starting at 00:00, 03:00, 06:00, 09:00, 12:00,             |
   |            | 15:00, 18:00 and 21:00, respectively.                      |
   +------------+------------------------------------------------------------+
   | SK         | Sum of the eight K-indices for the day.                    |
   +------------+------------------------------------------------------------+

Each valid K-index value is an integer from 0 to 9. A missing K-index value
is represented by -1. When all eight K-indices are present, SK is their
arithmetic sum (from 0 to 72). If any K-index is missing, SK is -1, not the
sum of the remaining indices.

For example, Ottawa records with missing indices are:

::

    27-JUN-15   178     2    2    2    3      2    3   -1   -1       -1
    28-JUN-15   179    -1   -1   -1   -1     -1   -1   -1   -1       -1

A complete annual file has one record for each calendar day: 365 records
in a common year or 366 records in a leap year.

Scientific and Historical Notes
```````````````````````````````

The K-index is a local, quasi-logarithmic measure of geomagnetic activity
scaled from disturbances in the horizontal magnetic field over a three-hour
interval. The K9 limit is the observatory-dependent lower amplitude limit
for K = 9. The DKA file records the resulting indices but does not identify
the method used to derive them. The observatory README.XXX file (where XXX
is the three-letter observatory code) should document the K-index derivation
method and the K9 limit actually used, particularly where this differs from
the value reported in the DKA header.

Before the 2005 archive, DKA files were supplied by individual observatories.
Older files can differ in header content, numerical notation, missing-value
codes and record padding. Some include an additional AK field representing
the daily mean equivalent amplitude index derived from the eight K-indices.
