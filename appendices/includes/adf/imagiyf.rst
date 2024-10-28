.. _app_iyf:


INTERMAGNET Format for Yearmean File : IYF V1.02
------------------------------------------------


Magnetic data with 1nT or 0.1min of arc resolution are organized
on a year file basis. One file contains all annual mean values of
the geomagnetic field components that are available from the
observatory.

File name: "YEARMEAN" and the three-letter observatory ID code as
an extension. eg: YEARMEAN.BOU for Boulder.

Each file may have from 1 to 3 tables containing annual mean
values. The file must contain a table of annual means for ALLDAYS,
but may also contain tables of annual means for QUIET-DAYS and
DISTURBED-DAYS.

Description of the Header Block
```````````````````````````````

The header contains information on observatory name, ID-code,
Colatitude, Longitude and Elevation to WGS-84 datum. It further
contains the headers for each data columns.

eg: The header for Wingst is:

.. highlight:: none

::

                                ANNUAL MEAN VALUES

                               WINGST, WNG, GERMANY.

       COLATITUDE:  36.26       LONGITUDE:   9.07 E       ELEVATION:   50 m

        YEAR      D        I         H      X      Y      Z      F  * ELE Note
               Deg. min Deg. min     nT     nT     nT     nT     nT

.. rubric:: Description of data space (75 characters per line including CrLf)

All data fields are right-justified. The field width must be
maintained, either by zero-filling or space-filling. The '+'sign
for positive values is optional.

::

    _YYYY.yyy_DDD_dd.d_III_ii.i_HHHHHH_XXXXXX_YYYYYY_ZZZZZZ_FFFFFF_A_EEEE_NNNCrLf
    ....
    ....

.. tabularcolumns:: |>{\centering\arraybackslash}p{2cm}|p{9cm}|

.. table::
    :class: longtable
    :widths: auto
    :align: center

    +----------+----------------------------------------------------------+
    | YYYY.yyy | Epoch is given with 3 decimals                           |
    +----------+----------------------------------------------------------+
    | DDD_dd.d | Declination is given in degrees and decimal minutes of   |
    |          | arc                                                      |
    +----------+----------------------------------------------------------+
    | III_ii.i | Inclination is given in degrees and decimal minutes of   |
    |          | arc                                                      |
    +----------+----------------------------------------------------------+
    | HHHHHH   | H-component is given in nT                               |
    +----------+----------------------------------------------------------+
    | XXXXXX   | X-component is given in nT                               |
    +----------+----------------------------------------------------------+
    | YYYYYY   | Y-component is given in nT                               |
    +----------+----------------------------------------------------------+
    | ZZZZZZ   | Z-component is given in nT                               |
    +----------+----------------------------------------------------------+
    | FFFFFF   | F-component is given in nT                               |
    +----------+----------------------------------------------------------+
    | A        | Type of annual means. May be "A"ll, "Q"uiet,             |
    |          | "D"isturbed, "I"ncomplete" or "J"ump. The "J" is not an  |
    |          | annual mean value, but indicates a jump in the           |
    |          | observatory recordings, which should be described in a   |
    |          | note.                                                    |
    +----------+----------------------------------------------------------+
    | EEEE     | recorded elements. eg:"XYZF" or "HDZF"                   |
    +----------+----------------------------------------------------------+
    | NNN      | Note number                                              |
    +----------+----------------------------------------------------------+
    | CrLf     | Indicates a Carriage return Line feed                    |
    +----------+----------------------------------------------------------+
    | \_       | Represents a space                                       |
    +----------+----------------------------------------------------------+

- Missing angular values must be coded as three 9 digits, a
  space, two 9 digits, a dot and one 9 digit: 999 99.9
- Missing component values must be coded as six 9 digits: 999999
- Angular values are written as degrees and minutes. Values may
  be written in the range 0 to 360 or -180 to 180. Observatories
  may choose which range to use. Negative values must always have
  the minus sign before the degree field, never before the minute
  field (including values between 0 and -1 degrees, for example
  "-0 59" means a value of minus zero degrees fifty nine
  minutes). This applies to all types of records, including jump
  records.

Description of the Footer
`````````````````````````


At the end of the file is added a footer describing the data. The
footer contains notes on jumps, incomplete data sets etc. A sample
footer looks like this:

::

      * A = All days
      * Q = Quiet Days
      * D = Disturbed Days
      * I = Incomplete
      * J = Jump: jump value = old site value - new site value

      ELE = Recorded elements from which the annual means were derived.
      If an independent total field measurement is not made at an
      observatory, this field should not include an 'F' code. For
      example, an observatory using a three component fluxgate with one
      horizontal sensor aligned along the magnetic meridian and a proton
      magnetometer would put 'HDZF' in this field. An observatory using
      only the fluxgate would put 'HDZ'.

      Notes:

      1. The jump in the values from 1988 to 1989 is due to
         establishment of a new absolute pillar during 1988.
      2. The jump in the values from 1993 to 1994 is due to a change in
         the difference delta-F between the PPM pillar and the absolute
         pillar. The change happened between spring 1989 and autumn
         1993. Why and when is unknown.


Sample of a Yearmean File
`````````````````````````

::

                                 ANNUAL MEAN VALUES

                             NARSARSUAQ, NAQ, GREENLAND

       COLATITUDE:  28.84       LONGITUDE: 314.56 E       ELEVATION:  4 meters

         YEAR      D        I        H      X      Y      Z      F  * ELE Note
                Deg.  '  Deg.  '     nT     nT     nT     nT     nT

      1983.500 326 41.6  77 15.8  12152  10156  -6673  53764  55120 A  DHZ
      1984.500 326 55.7  77 14.3  12171  10199  -6642  53736  55097 A  DHZ
      1985.500 327 11.1  77 12.9  12187  10242  -6604  53706  55071 A  DHZ
      1986.500 327 26.8  77 11.7  12201  10284  -6565  53679  55048 A  DHZ
      1987.500 327 44.5  77 09.9  12223  10336  -6524  53647  55022 A  DHZ
      1988.500 328 00.5  77 09.0  12235  10377  -6482  53633  55011 A  DHZ
      1989.000   0 02.6   0 00.7     -4      2     10     30     28 J  DHZ   1
      1989.500 328 13.8  77 07.2  12254  10418  -6452  53592  54975 A  DHZ
      1990.500 328 29.9  77 05.9  12271  10463  -6412  53571  54959 A  DHZ
      1991.500 328 45.6  77 04.9  12284  10503  -6371  53555  54946 A  DHZ
      1992.500 329 01.3  77 03.4  12302  10547  -6332  53525  54920 A  DHZ
      1993.500 329 17.9  77 01.6  12323  10596  -6292  53495  54896 A  DHZ
      1994.000   0 00.0   0 00.0     -1     -1      0     -2     -3 J  DHZ   2
      1994.500 329 34.3  77 00.7  12335  10636  -6247  53476  54880 A  DHZ
      1995.500 329 53.6  76 58.3  12366  10698  -6203  53444  54856 A  DHZ
      1996.500 330 13.6  76 56.0  12395  10759  -6155  53409  54828 A  DHZ
      1997.500 330 33.9  76 54.0  12423  10819  -6105  53381  54807 A  DHZ
      1998.500 330 55.6  76 52.2  12446  10878  -6048  53361  54793 A  DHZ
      1999.500 331 17.3  76 50.2  12473  10939  -5992  53332  54771 A  DHZ
      2000.500 331 39.0  76 48.4  12497  10998  -5934  53311  54756 A  DHZ
      2001.500 332 01.3  76 46.1  12527  11063  -5877  53278  54731 A  DHZ
      2002.500 332 23.6  76 44.2  12553  11124  -5817  53254  54714 A  DHZ
      2003.500 332 45.2  76 43.3  12564  11170  -5752  53237  54699 A  DHZ
      2004.500 333 07.8  76 40.5  12600  11240  -5695  53202  54674 A  DHZ
      2005.500 333 29.3  76 38.7  12624  11296  -5635  53176  54654 A  DHZ
      2006.500 333 50.4  76 36.2  12656  11360  -5580  53140  54626 A  DHZ
      2007.500 334 10.9  76 34.0  12686  11420  -5525  53113  54607 A  DHZ


      1983.500 326 42.3  77 15.1  12164  10167  -6677  53765  55124 Q  DHZ
      1984.500 326 56.3  77 13.3  12186  10213  -6648  53734  55098 Q  DHZ
      1985.500 327 11.6  77 12.0  12202  10256  -6611  53704  55073 Q  DHZ
      1986.500 327 27.4  77 10.8  12215  10297  -6571  53676  55048 Q  DHZ
      1987.500 327 44.9  77 09.4  12232  10345  -6527  53648  55025 Q  DHZ
      1988.500 328 00.8  77 08.2  12246  10387  -6487  53631  55011 Q  DHZ
      1989.000   0 02.6   0 00.7     -4      2     10     30     28 J  DHZ   1
      1989.500 328 14.4  77 06.6  12263  10427  -6455  53591  54976 Q  DHZ
      1990.500 328 30.0  77 05.3  12279  10470  -6416  53567  54956 Q  DHZ
      1991.500 328 46.1  77 04.0  12297  10515  -6376  53551  54945 Q  DHZ
      1992.500 329 01.6  77 02.7  12312  10556  -6336  53521  54919 Q  DHZ
      1993.500 329 18.2  77 00.9  12335  10607  -6297  53491  54895 Q  DHZ
      1994.000   0 00.0   0 00.0     -1     -1      0     -2     -3 J  DHZ   2
      1994.500 329 35.4  76 59.2  12357  10657  -6255  53470  54879 Q  DHZ
      1995.500 329 54.2  76 57.5  12380  10711  -6208  53443  54858 Q  DHZ
      1996.500 330 13.6  76 55.5  12403  10766  -6159  53407  54828 Q  DHZ
      1997.500 330 34.2  76 53.4  12431  10827  -6108  53380  54808 Q  DHZ
      1998.500 330 55.5  76 51.6  12456  10886  -6053  53359  54793 Q  DHZ
      1999.500 331 17.9  76 49.6  12483  10949  -5995  53330  54771 Q  DHZ
      2000.500 331 39.3  76 47.8  12507  11007  -5938  53308  54755 Q  DHZ
      2001.500 332 01.5  76 45.6  12535  11070  -5880  53278  54733 Q  DHZ
      2002.500 332 23.7  76 43.6  12562  11132  -5821  53252  54714 Q  DHZ
      2003.500 332 45.9  76 42.0  12584  11189  -5759  53234  54701 Q  DHZ
      2004.500 333 08.1  76 39.7  12613  11252  -5700  53200  54675 Q  DHZ
      2005.500 333 29.6  76 37.8  12640  11311  -5641  53177  54659 Q  DHZ
      2006.500 333 50.5  76 35.5  12669  11371  -5585  53141  54630 Q  DHZ
      2007.500 334 11.0  76 33.5  12694  11427  -5528  53114  54610 Q  DHZ


      1983.500 326 40.4  77 17.7  12121  10128  -6659  53763  55112 D  DHZ
      1984.500 326 54.6  77 16.5  12136  10168  -6626  53744  55097 D  DHZ
      1985.500 327 10.1  77 14.7  12158  10216  -6592  53707  55066 D  DHZ
      1986.500 327 25.6  77 13.7  12169  10255  -6552  53683  55045 D  DHZ
      1987.500 327 43.9  77 11.0  12205  10320  -6516  53645  55016 D  DHZ
      1988.500 327 59.5  77 10.9  12204  10349  -6469  53636  55007 D  DHZ
      1989.000   0 02.6   0 00.7     -4      2     10     30     28 J  DHZ   1
      1989.500 328 12.2  77 08.9  12228  10393  -6443  53598  54975 D  DHZ
      1990.500 328 30.0  77 07.3  12249  10444  -6400  53577  54959 D  DHZ
      1991.500 328 45.1  77 06.5  12258  10480  -6359  53560  54945 D  DHZ
      1992.500 329 00.8  77 05.6  12268  10517  -6316  53539  54927 D  DHZ
      1993.500 329 16.8  77 03.5  12295  10570  -6281  53502  54897 D  DHZ
      1994.000   0 00.0  00 00.0     -1     -1      0     -2     -3 J  DHZ   2
      1994.500 329 33.2  77 02.9  12300  10604  -6233  53481  54877 D  DHZ
      1995.500 329 52.6  76 59.7  12344  10677  -6195  53445  54852 D  DHZ
      1996.500 330 12.9  76 57.1  12378  10743  -6149  53411  54827 D  DHZ
      1997.500 330 33.7  76 54.8  12409  10807  -6099  53382  54805 D  DHZ
      1998.500 330 54.7  76 54.2  12416  10850  -6036  53371  54796 D  DHZ
      1999.500 331 17.0  76 51.9  12446  10915  -5980  53336  54769 D  DHZ
      2000.500 331 37.8  76 50.1  12472  10974  -5926  53317  54756 D  DHZ
      2001.500 332 00.3  76 47.0  12512  11048  -5873  53276  54726 D  DHZ
      2002.500 332 23.3  76 45.3  12536  11108  -5810  53256  54711 D  DHZ
      2003.500 332 44.1  76 45.7  12526  11134  -5738  53245  54698 D  DHZ
      2004.500 333 06.5  76 42.6  12567  11208  -5684  53206  54670 D  DHZ
      2005.500 333 29.1  76 40.1  12600  11275  -5625  53174  54647 D  DHZ
      2006.500 333 50.1  76 37.7  12631  11337  -5570  53140  54621 D  DHZ
      2007.500 334 10.9  76 34.9  12672  11407  -5519  53113  54604 D  DHZ

     * A = All Days
     * Q = Quiet Days
     * D = Disturbed Days
     * J = Jumps       jump value = old site value - new site value

     ELE = Recorded elements from which the annual mean values were derived

     Notes:   1. The jump in the values from 1988 to 1989 is due to
                 establishment of a new absolute pillar during 1988.
              2. The jump in the values from 1993 to 1994 is due to
                 a change in the difference delta-F between the PPM
                 pillar and the absolute pillar. The change happened
                 between spring 1989 and autumn 1993. Why and when
                 is unknown.

Sample of Missing Values
````````````````````````

::

     YEAR      D        I        H      X      Y      Z      F  * ELE Note
            Deg.  '  Deg.  '     nT     nT     nT     nT     nT

  1983.500 999 99.9 999 99.9 999999 999999 999999 999999 999999 A  DHZ
  1984.500 999 99.9  77 14.3  12171 999999  -6642  53736  55097 A  DHZ
