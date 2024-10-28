.. _app_imag_imfv_1:

INTERMAGNET Gin Dissemination Format for Minute Values : IMFV
-------------------------------------------------------------

.. _app_imag_imfv_123:

IMFV1.23
````````

Magnetic data, with tenth-nanotesla resolution, are organized on a day
file basis. One file contains 24 one-hour blocks, each containing 60
minutes worth of values. Blocks of 60 minutes of data are transmitted.
Blocks are padded with 9's if incomplete. Information is coded in ASCII.

File name: To remain compatible with all operating systems, the file
name is limited to 8 characters and will contain the date and the
three-letter code as an extension. eg: MAR1591.BOU for Boulder, March
15, 1991; and JUN2391.OTT for June 23, 1991 at Ottawa.

.. _app_imag_imfv_123_header:

Description of the Header Block (64 characters including CrLf)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. highlight:: none

::

   IDC_DDDDDDD_DOY_HH_COMP_T_GIN_COLALONG_DECBAS_RRRRRRRRRRRRRRRRCrLf

.. tabularcolumns:: |p{2cm}|p{13.5cm}|

.. table::
    :widths: auto
    :align: center
    :class: longtable

    +----------------+-------------------------------------------------+
    | Field          | Description                                     |
    +----------------+-------------------------------------------------+
    | IDC            | Indicates the IAGA three letter observatory     |
    |                | identification (ID) code eg: BOU for Boulder,   |
    |                | OTT for Ottawa, LER for Lerwick, etc.           |
    +----------------+-------------------------------------------------+
    | DDDDDDD        | Indicates the date, eg: FEB1591 for February    |
    |                | 15, 1991.                                       |
    +----------------+-------------------------------------------------+
    | DOY            | Indicates day of the year (1-366)               |
    +----------------+-------------------------------------------------+
    | HH             | Indicates the Hour (0-23). The first line       |
    |                | following the header will contain the values    |
    |                | corresponding to minute 0 and 1 of this hour.   |
    |                | The first value of the day file is hour 0       |
    |                | minute 0.                                       |
    +----------------+-------------------------------------------------+
    | COMP           | Order in which the components are listed, can   |
    |                | be HDZF, HDZG, XYZF, XYZG. G represents the     |
    |                | difference between a measured ‘Scalar’ F and a  |
    |                | computed ‘vector’ F: G = F(vector) - F(scalar). |
    |                | All components excluding D must be in tenths of |
    |                | nT. D must be in hundredths of minutes, east.   |
    |                | The F or G component should be included only if |
    |                | it is measured from a scalar instrument         |
    |                | independent of the other 3 components otherwise |
    |                | it must be filled with 999999.                  |
    +----------------+-------------------------------------------------+
    | T              | One-letter code for data type. R=Reported,      |
    |                | A=Adjusted, Q=Quasi-definitive, D=Definitive    |
    |                | data.                                           |
    |                |                                                 |
    |                | **Reported data** are defined as: the raw data  |
    |                | obtained from the IMO, either by satellite,     |
    |                | computer link, or other means. It will be       |
    |                | formatted in either version IMFV2.8N (binary)   |
    |                | or IMFV1.2N (ASCII,) without any RM (Reference  |
    |                | Measurements), or other modifications applied   |
    |                | to it.                                          |
    |                |                                                 |
    |                | **Adjusted data** are defined as: the Reported  |
    |                | data with RM, spike removal, timeshifts, and/or |
    |                | other modifications applied to it. It is        |
    |                | emphasized that only one (1) adjusted version   |
    |                | of the data would be allowed, to be completed   |
    |                | within 7 days of receipt of the Reported data   |
    |                | to prevent the proliferation of multiple        |
    |                | versions of the Adjusted data.                  |
    |                |                                                 |
    |                | **Quasi-definitive data** are defined as data   |
    |                | that have been corrected using provisional      |
    |                | baselines. Produced soon after their            |
    |                | acquisition, their accuracy is intended to be   |
    |                | very close to that of an observatory’s          |
    |                | definitive data product. 98% of the differences |
    |                | between quasi-definitive and definitive data    |
    |                | (X, Y, Z) monthly mean values should be less    |
    |                | than 5nT.                                       |
    |                |                                                 |
    |                | **Definitive data** are defined as the final    |
    |                | adopted data values. Definitive data will only  |
    |                | be distributed by the institution responsible   |
    |                | for the observatory.                            |
    +----------------+-------------------------------------------------+
    | GIN            | Three-letter code for GIN responsible for       |
    |                | processing the station (IMO) data eg:           |
    |                | EDI(Edinburgh), GOL(Golden), OTT(Ottawa),       |
    |                | PAR(Paris).                                     |
    +----------------+-------------------------------------------------+
    | COLALONG       | Colatitude and east longitude of the            |
    |                | observatory in tenths of degrees, to WGS-84     |
    |                | datum.                                          |
    +----------------+-------------------------------------------------+
    | DECBAS         | Baseline declination value in tenths of minutes |
    |                | East (0-216,000). Declination baseline values   |
    |                | to be provided annually. If components are      |
    |                | X,Y,Z then DECBAS=000000. The DECBAS value is   |
    |                | used to allow declination data to exceed 166.66 |
    |                | degrees (which is the limit of the declination  |
    |                | elements in each data record without any        |
    |                | offset). If the declination is > 166 degrees at |
    |                | an observatory then a DECBAS value should be    |
    |                | selected such that the minute samples lie       |
    |                | between 0 and 166 degrees. The declination      |
    |                | baseline DECBAS should be subtracted from the   |
    |                | minute data samples before coding them.         |
    +----------------+-------------------------------------------------+
    | RRR..RRR       | Reserved 16 bytes of R-characters for future    |
    |                | use.                                            |
    +----------------+-------------------------------------------------+
    | \_             | Indicates a space character.                    |
    +----------------+-------------------------------------------------+
    | CrLf           | Indicates a Carriage return, Line feed.         |
    +----------------+-------------------------------------------------+

Missing values for a vector component must be coded as a space (for
the sign bit) followed by six 9 digits: \_999999.

Missing values for the scalar component must be coded as six 9 digits: 999999

.. _app_imag_imfv_123_data:

Description of Data Space (64 characters per line including CrLf)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Component values are coded as signed integers, right-justified with a
field width of 7. Total field (F) values are coded as unsigned integers,
right-justified with a field width of 6. The field widths must be
maintained, either through zero-filling or space-filling. The '+' sign
for positive values is optional.

Two (2) minutes of data are concatenated on the same line

.. highlight:: none

::

    AAAAAAA_BBBBBBB_CCCCCCC_FFFFFF__AAAAAAA_BBBBBBB_CCCCCCC_FFFFFFCrLf
    (values for minute 0) (values for minute 1)
    . .
    . .
    . .
    AAAAAAA_BBBBBBB_CCCCCCC_FFFFFF__AAAAAAA_BBBBBBB_CCCCCCC_FFFFFFCrLf
    (values for minute 58) (values for minute 59)

.. tabularcolumns:: |p{2cm}|p{7cm}|

.. table::
    :widths: auto
    :align: center

    ======= =============================================
    Field   Description
    ======= =============================================
    AAAAAAA Indicates Component 1 data field (H,X, etc.).
    BBBBBBB Indicates Component 2 data field (D,Y, etc.).
    CCCCCCC Indicates Component 3 data field (Z,I, etc.).
    FFFFFF  Indicates Total Field data field.
    \_      Indicates space character.
    CrLf    Indicates Carriage Return and Line Feed.
    ======= =============================================

Sample of missing values

::

   _999999__999999__999999_999999___999999__999999__999999_999999CrLf

This example represents all components as missing for the first two
minutes of the hour.

"_" indicates a space character.

.. _app_imag_imfv_122:

IMFV1.22
````````

Magnetic data, with tenth-nanotesla resolution, are organized on a day
file basis. One file contains 24 one-hour blocks, each containing 60
minutes worth of values. Blocks of 60 minutes of data are transmitted.
Blocks are padded with 9's if incomplete. Information is coded in ASCII.

File name: To remain compatible with all operating systems, the file
name is limited to 8 characters and will contain the date and the
three-letter code as an extension. eg: MAR1591.BOU for Boulder, March
15, 1991; and JUN2391.OTT for June 23, 1991 at Ottawa.

.. _app_imag_imfv_122_header:

Description of the Header Block (64 characters including CrLf)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. highlight:: none

::

    IDC_DDDDDDD_DOY_HH_COMP_T_GIN_COLALONG_DECBAS_RRRRRRRRRRRRRRRRCrLf


.. tabularcolumns:: |p{2cm}|p{13.5cm}|

.. table::
    :widths: auto
    :align: center
    :class: longtable

    +----------------+-------------------------------------------------+
    | Field          | Description                                     |
    +================+=================================================+
    | IDC            | Indicates the IAGA three letter observatory     |
    |                | identification (ID) code eg: BOU for Boulder,   |
    |                | OTT for Ottawa, LER for Lerwick, etc.           |
    +----------------+-------------------------------------------------+
    | DDDDDDD        | Indicates the date, eg: FEB1591 for February    |
    |                | 15, 1991.                                       |
    +----------------+-------------------------------------------------+
    | DOY            | Indicates day of the year (1-366)               |
    +----------------+-------------------------------------------------+
    | HH             | Indicates the Hour (0-23). The first line       |
    |                | following the header will contain the values    |
    |                | corresponding to minute 0 and 1 of this hour.   |
    |                | The first value of the day file is hour 0       |
    |                | minute 0.                                       |
    +----------------+-------------------------------------------------+
    | COMP           | Order in which the components are listed, can   |
    |                | be HDZF, XYZF. All components excluding D must  |
    |                | be in tenths of nT. D must be in hundredths of  |
    |                | minutes, east. The F component should be        |
    |                | included only if it is measured from a scalar   |
    |                | instrument independent of the other 3           |
    |                | components otherwise it must be filled with     |
    |                | 999999.                                         |
    +----------------+-------------------------------------------------+
    | T              | One-letter code for data type. R=Reported,      |
    |                | A=Adjusted, D=Definitive data.                  |
    |                |                                                 |
    |                | **Reported data** are defined as: the raw data  |
    |                | obtained from the IMO, either by satellite,     |
    |                | computer link, or other means. It will be       |
    |                | formatted in either version IMFV2.8N (binary)   |
    |                | or IMFV1.2N (ASCII,) without any RM (Reference  |
    |                | Measurements), or other modifications applied   |
    |                | to it.                                          |
    |                |                                                 |
    |                | **Adjusted data** are defined as: the Reported  |
    |                | data with RM, spike removal, timeshifts, and/or |
    |                | other modifications applied to it. It is        |
    |                | emphasized that only one (1) adjusted version   |
    |                | of the data would be allowed, to be completed   |
    |                | within 7 days of receipt of the Reported data   |
    |                | to prevent the proliferation of multiple        |
    |                | versions of the Adjusted data.                  |
    |                |                                                 |
    |                | **Definitive data** are defined as the final    |
    |                | adopted data values. Definitive data will only  |
    |                | be distributed by the institution responsible   |
    |                | for the observatory.                            |
    +----------------+-------------------------------------------------+
    | GIN            | Three-letter code for GIN responsible for       |
    |                | processing the station (IMO) data eg:           |
    |                | EDI(Edinburgh), GOL(Golden), OTT(Ottawa),       |
    |                | PAR(Paris).                                     |
    +----------------+-------------------------------------------------+
    | COLALONG       | Colatitude and east longitude of the            |
    |                | observatory in tenths of degrees, to WGS-84     |
    |                | datum.                                          |
    +----------------+-------------------------------------------------+
    | DECBAS         | Baseline declination value in tenths of minutes |
    |                | East (0-216,000). Declination baseline values   |
    |                | to be provided annually. If components are      |
    |                | X,Y,Z then DECBAS=000000.                       |
    +----------------+-------------------------------------------------+
    | RRR..RRR       | Reserved 16 bytes of R-characters for future    |
    |                | use.                                            |
    +----------------+-------------------------------------------------+
    | \_             | Indicates a space character.                    |
    +----------------+-------------------------------------------------+
    | CrLf           | Indicates a Carriage return, Line feed.         |
    +----------------+-------------------------------------------------+

Missing values for a vector component must be coded as a space (for the sign bit) followed
by six 9 digits: \_999999.

Missing values for the scalar component must be coded as six 9 digits: 999999

Description of Data Space (64 characters per line including CrLf)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Component values are coded as signed integers, right-justified with a
field width of 7. Total field (F) values are coded as unsigned integers,
right-justified with a field width of 6. The field widths must be
maintained, either through zero-filling or space-filling. The '+' sign
for positive values is optional.

Two (2) minutes of data are concatenated on the same line

.. highlight:: none

::

    AAAAAAA_BBBBBBB_CCCCCCC_FFFFFF__AAAAAAA_BBBBBBB_CCCCCCC_FFFFFFCrLf
    (values for minute 0) (values for minute 1)
    . .
    . .
    . .
    AAAAAAA_BBBBBBB_CCCCCCC_FFFFFF__AAAAAAA_BBBBBBB_CCCCCCC_FFFFFFCrLf
    (values for minute 58) (values for minute 59)


.. tabularcolumns:: |p{2cm}|p{7cm}|

.. table::
    :widths: auto
    :align: center

    ======= =============================================
    Field   Description
    ======= =============================================
    AAAAAAA Indicates Component 1 data field (H,X, etc.).
    BBBBBBB Indicates Component 2 data field (D,Y, etc.).
    CCCCCCC Indicates Component 3 data field (Z,I, etc.).
    FFFFFF  Indicates Total Field data field.
    \_      Indicates space character.
    CrLf    Indicates Carriage Return and Line Feed.
    ======= =============================================

Sample of missing values

.. highlight:: none

::

   _999999__999999__999999_999999___999999__999999__999999_999999CrLf

This example represents all components as missing for the first two
minutes of the hour.

"_" indicates a space character.
