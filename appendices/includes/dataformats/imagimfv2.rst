.. _app_imag_imfv_2:

INTERMAGNET Satellite Transmission Format : IMFV2.83
----------------------------------------------------

.. include:: ./appendices.rst


The INTERMAGNET satellite data transmission format IMFV2.83 defines the structure of 126
bytes of magnetic observatory information. METEOSAT users, who must transmit once per hour,
will send five 12-minute IMFV2.83 data blocks. GOES users transmit at 12-minute intervals
one IMFV2.83 data block encoded in NESS-BINARY (189 bytes). The order of transmission to
the satellite will be in byte sequence low-byte first, then high-byte. Refer to
|app_sat_cod| for satellite coding examples.REFERENCE MEASUREMENT (RM) or  FREE SPACE

.. tabularcolumns:: |p{3.5cm}|p{8cm}|p{2cm}|p{2cm}|

.. table::
    :widths: auto
    :align: center

    +--------------------------+-------------------------------------------------+------------+--------------------------+
    |                          | Day of first sample (1-365/366)                 |  12 Bits   | 1 - 3 [#f1]_             |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | Minute of the day of first sample (0 - 1439)    |  12 Bits   | 1 - 3 [#f1]_             |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | Offset for C1                                   |  8 Bits    | 4                        |
    |                          +-------------------------------------------------+------------+--------------------------+
    | |                        | Offset for C2                                   |  8 Bits    | 5                        |
    |                          +-------------------------------------------------+------------+--------------------------+
    |   **HEADER**             | Offset for C3                                   |  8 Bits    | 6                        |
    |                          +-------------------------------------------------+------------+--------------------------+
    |   **12 BYTES**           | Offset for C4                                   |  8 Bits    | 7                        |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | Flag #1                                         |  8 Bits    | 8                        |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | Flag #2                                         |  8 Bits    | 9                        |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | Colatitude in 1/10 degrees (0 - 1800)           |  12 Bits   | 10 - 12 [#f1]_           |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | Flag #2                                         |  12 Bits   | 10 - 12 [#f1]_           |
    +--------------------------+-------------------------------------------------+------------+--------------------------+
    |  **08 BYTES**            | FREE SPACE                                      |  64 Bits   | 13 - 20                  |
    +--------------------------+-------------------------------------------------+------------+--------------------------+
    |  **10 BYTES**            | REFERENCE MEASUREMENT (RM) or  FREE SPACE       |  80 Bits   | 21 - 30                  |
    +--------------------------+-------------------------------------------------+------------+--------------------------+
    |                          | C1 for Sample 1                                 |  16 Bits   | 31 - 32                  |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | C2 for Sample 1                                 |  16 Bits   | 33 - 34                  |
    |                          +-------------------------------------------------+------------+--------------------------+
    ||                         | C3 for Sample 1                                 |  16 Bits   | 34 - 35                  |
    |                          +-------------------------------------------------+------------+--------------------------+
    |  **MIN VALUES**          | ...                                             | ...        | ...                      |
    |                          +-------------------------------------------------+------------+--------------------------+
    |  **96 BYTES**            | C1 for Sample 12                                |  16 Bits   | 119 - 120                |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | C2 for Sample 12                                |  16 Bits   | 121 - 122                |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | C3 for Sample 12                                |  16 Bits   | 123 - 124                |
    |                          +-------------------------------------------------+------------+--------------------------+
    |                          | C4 for Sample 12                                |  16 Bits   | 125 - 126                |
    +--------------------------+-------------------------------------------------+------------+--------------------------+


.. [#f1] See section :ref:`app_imag_imfv_2_header`.

.. tabularcolumns:: |p{1cm}|p{13cm}|

.. table:: Flag#1
    :widths: 20,10
    :align: center

    +--------+----------------------------------------------------------------------------------+
    | MSB    |               Description                                                        |
    +========+==================================================================================+
    | 8      |                                                                                  |
    |        | .. highlight:: none                                                              |
    |        | .. code::                                                                        |
    |        |                                                                                  |
    |        |    Orientation Code Component 1 Component 2 Component 3 Component 4              |
    |        |          0              X           Y           Z           F                    |
    |        |          1              H           D           Z           F                    |
    |        |          2                          D           I           F                    |
    |        |          3              Other                                                    |
    |        |                                                                                  |
    +--------+                                                                                  |
    | 7      |                                                                                  |
    +--------+----------------------------------------------------------------------------------+
    | 6      | Scale factor for X or H                                                          |
    +--------+----------------------------------------------------------------------------------+
    | 5      | Scale factor for Y or D                                                          |
    +--------+----------------------------------------------------------------------------------+
    | 4      | Scale factor for Z or I                                                          |
    +--------+----------------------------------------------------------------------------------+
    | 3      | Scale factor for F                                                               |
    +--------+----------------------------------------------------------------------------------+
    | 2      |  Filtering - 0: INTERMAGNET approved filtering, 1: non-approved filtering.       |
    |        |                                                                                  |
    |        |  See INTERMAGNET terminology "filtering".                                        |
    +--------+----------------------------------------------------------------------------------+
    | 1      | Alert capability - The IMO has the ability to                                    |
    |        | detect magnetic events if the flag is set to 1.                                  |
    |        |                                                                                  |
    |        | 0: not active                                                                    |
    |        |                                                                                  |
    |        | 1: active                                                                        |
    +--------+----------------------------------------------------------------------------------+

.. tabularcolumns:: |p{1cm}|p{13cm}|

.. table:: Flag#2
    :widths: auto
    :align: center

    +--------+-------------------------------------------------------------------+
    | MSB    | Description                                                       |
    +========+===================================================================+
    | 8      | Sudden storm commencement detected                                |
    +--------+-------------------------------------------------------------------+
    | 7      | Storm in progress                                                 |
    |        |                                                                   |
    |        | A storm is in progress if  the level of magnetic activity         |
    |        | is equivalent to K > 4   for past one-hour                        |
    |        |                                                                   |
    |        | period.                                                           |
    |        | The flag will be reset to zero when the equivalent level of       |
    |        | activity drops to K <= 4.                                         |
    +--------+-------------------------------------------------------------------+
    | 6      | 0: No Reference Measurement (RM) capability                       |
    |        | bytes 13-30 are user free space                                   |
    |        |                                                                   |
    |        | 1: Base Reference Measurement data available inbytes 21-30.       |
    |        |                                                                   |
    |        | Bytes' 13-20 are user free space.                                 |
    +--------+-------------------------------------------------------------------+
    | 5      | Free (user defined)                                               |
    +--------+-------------------------------------------------------------------+
    | 4      | Free (user defined)                                               |
    +--------+-------------------------------------------------------------------+
    | 3      | Free (user defined)                                               |
    +--------+-------------------------------------------------------------------+
    | 2      | Free (user defined)                                               |
    +--------+-------------------------------------------------------------------+
    | 1      | Free (user defined)                                               |
    +--------+-------------------------------------------------------------------+


.. _app_imag_imfv_2_header:

IMFV2.83 Header Encoding
````````````````````````

In IMFV2.83 format, the time stamp and site identification code are encoded
in 3-byte strings formed from two 12-bit fields combined as described below:

.. tabularcolumns:: |p{4cm}|p{4cm}|

.. table::
    :widths: auto
    :align: center

    =========================== ============================
    Time Stamp Input            Encoded Output
    =========================== ============================
    Least sig. 8 bits of day    Byte 1
    Most sig. 4 bits of day     Byte 2, four least sig. bits
    Least sig. 4 bits of minute Byte 2, four most sig. bits
    Most sig. 8 bits of minute  Byte 3
    =========================== ============================

.. tabularcolumns:: |p{5cm}|p{4cm}|

.. table::
    :widths: auto
    :align: center

    =================================== =============================
    Site Identification Code Input      Encoded Output
    =================================== =============================
    Least sig. 8 bits of colatitude     Byte 10
    Most sig. 4 bits of colatitude      Byte 11, four least sig. bits
    Least sig. 4 bits of east longitude Byte 11, four most sig. bits
    Most sig. 8 bits of east longitude  Byte 12
    =================================== =============================

| Example:
| The time stamp for day 30, minute 684 would be encoded as:

.. tabularcolumns:: |p{4cm}|c|c|c|c|c|c|c|c|c|c|c|c|c|

.. table:: Input fields
    :widths: auto
    :align: center

    ======================== == == = = = = = = = = = = ===
    Bit (MSB to LSB)         11 10 9 8 7 6 5 4 3 2 1 0 Hex
    Day 30 (first item)      0  0  0 0 0 0 0 1 1 1 1 0 01E
    Minute 684 (second item) 0  0  1 0 1 0 1 0 1 1 0 0 2AC
    ======================== == == = = = = = = = = = = ===


.. tabularcolumns:: |p{1cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|

.. table:: Output Encoded field
    :widths: auto
    :align: center


    +--------+--------+-------------+----------------+-----------+--------+----------------+
    |        | .. centered:: Byte 0 |  .. centered:: Byte 1      | .. centered:: Byte 2    |
    +========+========+=============+================+===========+========+================+
    | Byte   | 0001   | 1110        |1100            | 0000      |0010    | 1001           |
    +--------+--------+-------------+----------------+-----------+--------+----------------+
    | Hex    | 1      | E           | C              | 0         | 2      | A              |
    +--------+--------+-------------+----------------+-----------+--------+----------------+
    | Value  |      8 LSB Day       | 4 LSB Minute   | 4 MSB Day | 8 MSB Minute            |
    +--------+--------+-------------+----------------+-----------+--------+----------------+




IMFV2.83 Data Value Encoding
````````````````````````````

Constraints on the bandwidth of a GOES satellite communications
channel dictate a maximum transmission block of 126 bytes of data
once every 12 minutes from an INTERMAGNET Magnetic Observatory (IMO).
To conserve bytes, each measurement of a magnetic component is
represented using only 2 bytes which, upon reception, are interpreted
together with header information to produce a resultant 3-byte
representation at the Geomagnetic Information Node (GIN). All
magnetic field values in this encoding description are expressed in
tenths of nanoTeslas (tnT) unless otherwise noted. The resolution of
the measurements is 1 tnT and so a 16-bit representation allows a 216
= 65536 tnT (6553.6 nT) dynamic range within a 12-minute IMFV2.83
block. This is inadequate to accomodate magnetic storms at some
locations, and so the encoding scheme produces measurements at
reduced sensitivity when extremely large excursions are present. The
INTERMAGNET data encoding produces an Offset (OFF) value and a Scale
Factor (SF) flag bit for each component, as well as the encoded
individual minute values (see diagram at end of appendix). The OFF
and SF apply to all measurements of a component within an IMFV2.83
data block.

We define the terms used in encoding as follows:

.. tabularcolumns:: |p{2cm}|p{9cm}|

.. table:: Input fields
    :widths: auto
    :align: center

    ================== ==================================================================
    Data(i)            Set of minute values measured in tnT
    D\ :sub:`pos` (i)  Minute values shifted by 1048576 to be always positive
    D\ :sub:`max`      Largest D\ :sub:`pos` (i) of a given component in IMFV2.83 block
    D\ :sub:`min`      Smallest D\ :sub:`pos` (i) of a given component in IMFV2.83 block
    OFF                Offset value
    BF                 Bias Factor = 8192
    SM                 Scale Multiplier for sensitivity of encoded data
    SF                 Scale Factor flag for sensivity of encoded data
    E(i)               Set of encoded minute values
    ================== ==================================================================

Numbers used in this encoding algorithm have been chosen to permit
simple binary arithmetic operations:

-  8192 = 213
-  57344 = 216 - 213
-  1048576 = 220
-  2097151 = 221 - 1

Encoding of a 12-minute IMFV2.83 data block begins by adding a
constant 1048576 tnT to the minute values Data(i) to produce a new
data set :math:`D_{pos}(i)` whose values are always positive.

.. math::

  D_{pos}(i) = Data(i) + 1048576

The limiting values of these :math:`D_{pos}(i)` are 0 and 2097151tnT.
An Offset value (OFF) is next computed from the :math:`D_{pos}(i)`
for each component by using the minimum value of the component,
:math:`D_{min}`.

.. math::

    OFF = INT (D_{min}/BF)

where INT means the truncated integer after the division. The OFF
value for each component may be anywhere in the range of 0 to 255 and
the OFF values for the four components are stored in bytes 4,5,6,7 of
the header for use in decoding the data after reception at a GIN.
A Scale Multiplier (SM) for each component is now computed:

.. math::

    SM = INT ((D_{max} - OFF*BF)/57344) + 1

The encoding algorithm produces an SM whose value is governed by the
range of :math:`D_{pos}(i)` within a data block. In this application
to format IMFV2.83, however, SM can in practice be limited to values
of either 1 or 2. Format IMFV2.83 reserves only one flag bit per
component for storing scale information. These flags are bits 6,5,4,3
of byte 8 in the header, labelled Scale Factor (SF). Flag bit SF=0
represents SM=1, where the encoded data are considered at normal
sensitivity (1 tnT/bit). At SM=1, the dynamic range available in the
data block is at least 49152 tnT (= 57344-BF) and at most 57344 tnT,
depending upon where the :math:`D_{min}` value sits relative to the
quantity OFF*BF. Flag bit SF=1 represents SM=2, where the encoded
data are considered as half sensitivity (2 tnT/bit). At SM=2, the
dynamic range in the data block is at least 106496 tnT (= 2*57344-BF)
and at most 114688 tnT (= 2*57344) depending again upon where
:math:`D_{min}` is relative to the quantity OFF*BF.
Encoded data values are now computed as:

.. math::

  E(i) = INT((D_{pos}(i) - OFF*BF)/SM)

and are stored in bytes 31 to 126. Upon reception at the GIN, encoded
data are reconstituted using the expression:

.. math::

  Data(i) = E(i)*SM + OFF*BF - 1048576

This reconstitution is exact for SM=1 but rounded down by no more
than 2 tnT on those infrequent occasions when SM=2.
In summary, the expressions defining each of the encoding and
reconstitution steps are:

1. :math:`D_{pos}(i) = Data(i) + 1048576`
#. :math:`OFF = INT (D_{min}/BF)`
#. :math:`SM = INT ((D_{max} - OFF*BF)/57344) + 1`
#. :math:`E(i) = INT((D_{pos}(i) - OFF*BF)/SM)`
#. :math:`Data(i) = E(i)*SM + OFF*BF - 1048576`

Scale Factor flags are set

.. table::
    :widths: auto
    :align: center

    == ==
    SF SM
    == ==
    0  1
    1  2
    == ==

.. note::

    E(i) set to 65535 (FFFF hex) indicates missing or invalid
    data.

.. figure:: ../img/imfv283.png
    :align: center
