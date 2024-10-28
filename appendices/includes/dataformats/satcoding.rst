.. _app_sat_cod:

Satellite Coding Examples
-------------------------

Coding Example for Goes Satellite
`````````````````````````````````

Each block of 126 bytes in IMFV2.83 must be encoded in 189 NESS-BINARY
bytes (NESSbytes). NESSBINARY breaks each pair of source bytes (word)
into 3 NESSbytes. If the bits of the source word are B15-B0 with B15 the
most significant, then these are placed right-justified in NESSbytes as
follows: B15-B12 are in the first NESSbyte, B11-B6 are in the second
NESSbyte and B5-B0 are in the third NESSbyte. Within NESSbytes, bit 6 is
always set to 1 and bit 7 is set for odd parity. In the first NESSbyte,
bits 5 and 4 are filled by sign extension, i.e. they take the same value
as bit 3. As an example, consider the 16-bit source word h0C4E, d3150.

Step 1 - break into 3 formative NESSbytes.

-  byte 1: XXXX0000
-  byte 2: XX110001
-  byte 3: XX001110

Step 2 - sign extend in byte 1, bit 6=1, bit 7=odd parity.

-  NESSbyte 1:01000000
-  NESSbyte 2:11110001
-  NESSbyte 3:11001110

.. figure:: ../img/ness.png
    :align: center


After encoding, the 12-minute block is sent to the data collection platform (DCP) to be transmitted.

.. raw:: latex

    \newpage



Consider the following data set:

.. highlight:: none

::

   Date: March 23 1993 (day 082)
   Time of first sample 12:00
   Observatory identification: 04342275 (co-latitude 43.4E, longitude 227.5E)
   Sensor orientation is XYZF
   INTERMAGNET approved filtering
   No alert capability
   No RMs
   Flag #1: 00000000
   Flag #2: 00000000


Minute values of C1, C2, C3, C4

.. highlight:: none

::

   209062 -56 423216 472036
   209062 -52 423218 472038
   209058 -46 423220 472038
   209053 -49 423219 472035
   209052 -51 423214 472030
   209054 -55 423214 472031
   209061 -56 423215 472035
   209066 -55 423217 472039
   209062 -52 423214 472034
   209055 -54 423212 472030
   209055 -52 423213 472030
   209056 -50 423213 472031

Hex dump of IMFV2.83 binary of this 12-minute block: (126 characters)

**52 00 2D 99 7F B3 B9 00 00 B2 31 8E 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 A6 10 C8 1F 30 15 E4 13 A6 10 CC 1F 32 15 E6 13 A2 10
D2 1F 34 15 E6 13 9D 10 CF 1F 33 15 E3 13 9C 10 CD 1F 2E 15 DE 13 9E 10
C9 1F 2E 15 DF 13 A5 10 C8 1F 2F 15 E3 13 AA 10 C9 1F 31 15 E7 13 A6 10
CC 1F 2E 15 E2 13 9F 10 CA 1F 2C 15 DE 13 9F 10 CC 1F 2D 15 DE 13 A0 10
CE 1F 2D 15 DF 13**

After conversion to NESS-BINARY for GOES satellite: (189 characters)

**45 C8 40 C2 76 D9 C7 FE 73 FB 64 40 40 C2 F2 43 46 CE 40 40 40 40 40 40
40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 40 7A 58 D0
7C E0 DF 43 40 D5 FE D0 D3 7A 58 D0 7C 70 DF 43 C8 D5 FE 58 D3 7A C8 D0
FD C8 DF 43 D0 D5 FE 58 D3 79 F4 D0 7C 7C DF 43 4C D5 FE 4C D3 79 70 D0
7C F4 DF C2 F8 D5 FD F8 D3 79 F8 D0 7C 64 DF C2 F8 D5 FD 7C D3 7A 54 D0
7C E0 DF C2 7C D5 FE 4C D3 7A 68 D0 7C 64 DF 43 C4 D5 FE DC D3 7A 58 D0
7C 70 DF C2 F8 D5 FE C8 D3 79 7C D0 7C 68 DF C2 70 D5 FD F8 D3 79 7C D0
7C 70 DF C2 F4 D5 FD F8 D3 7A 40 D0 7C F8 DF C2 F4 D5 FD 7C D3**

Coding Example for Meteosat Satellite
`````````````````````````````````````

As the duration between two time slots on the METEOSAT satellite is one
hour, five 12-minute blocks are chained and sent to the DCP for
transmission. As a METEOSAT message is 640 bytes long, 10 bytes (hex00)
are added to the end of the 630 bytes of the 5 X 12-minute blocks (5 X
126 bytes). Binary from IMFV2.83 format is sent to the DCP without any
modification.

Consider the following data set:

.. highlight:: none

::

    Date: March 23 1993 (day 082)
    Time of first sample 12:00
    Observatory identification: 04342275 (co-latitude 43.4E, longitude 227.5E)
    Sensor orientation is XYZF
    INTERMAGNET approved filtering
    No alert capability
    No RMs
    Flag #1: 00000000
    Flag #2: 00000000


Minute values of C1, C2, C3, C4

Block #1: minute 0-11

.. highlight:: none

::

    209062 -56 423216 472036
    209062 -52 423218 472038
    209058 -46 423220 472038
    209053 -49 423219 472035
    209052 -51 423214 472030
    209054 -55 423214 472031
    209061 -56 423215 472035
    209066 -55 423217 472039
    209062 -52 423214 472034
    209055 -54 423212 472030
    209055 -52 423213 472030
    209056 -50 423213 472031

Block #2: minute 12-23

.. highlight:: none

::

    209059 -45 423215 472034
    209057 -45 423214 472032
    209059 -40 423216 472035
    209057 -42 423214 472032
    209054 -40 423213 472030
    209053 -42 423214 472030
    209048 -45 423214 472028
    209046 -47 423217 472030
    209045 -45 423217 472030
    209044 -46 423217 472029
    209043 -44 423214 472026
    209045 -43 423215 472028

Block #3 : minute 24-35

.. highlight:: none

::

    209050 -44 423215 472030
    209056 -45 423217 472035
    209064 -45 423218 472039
    209072 -43 423217 472042
    209073 -41 423216 472041
    209069 -39 423216 472039
    209063 -37 423215 472036
    209059 -36 423216 472035
    209054 -37 423216 472033
    209051 -42 423215 472030
    209046 -47 423215 472028
    209045 -50 423216 472029

Block #4: minute 36-47

.. highlight:: none

::

    209041 -56 423214 472025
    209044 -58 423215 472027
    209044 -60 423215 472027
    209049 -57 423217 472031
    209056 -54 423217 472035
    209063 -48 423217 472038
    209068 -45 423217 472040
    209070 -42 423216 472040
    209072 -40 423217 472042
    209070 -38 423216 472040
    209065 -40 423215 472037
    209063 -41 423215 472036

Block #5: minute 48-59

.. highlight:: none

::

    209067 -39 423217 472039
    209064 -41 423216 472037
    209059 -42 423215 472034
    209058 -41 423215 472034
    209061 -40 423214 472034
    209063 -37 423215 472036
    209060 -37 423215 472034
    209060 -38 423213 472033
    209063 -39 423213 472034
    209063 -40 423212 472033
    209068 -37 423215 472038
    209071 -33 423217 472041


Hex dump of IMFV2.83 binary of these five 12-minute blocks: (5 \* 126 +
10 trailing zeros = 640 characters)

**52 00 2D 99 7F B3 B9 00 00 B2 31 8E 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 A6 10 C8 1F 30 15 E4 13 A6 10 CC 1F 32 15 E6 13 A2 10
D2 1F 34 15 E6 13 9D 10 CF 1F 33 15 E3 13 9C 10 CD 1F 2E 15 DE 13 9E 10
C9 1F 2E 15 DF 13 A5 10 C8 1F 2F 15 E3 13 AA 10 C9 1F 31 15 E7 13 A6 10
CC 1F 2E 15 E2 13 9F 10 CA 1F 2C 15 DE 13 9F 10 CC 1F 2D 15 DE 13 A0 10
CE 1F 2D 15 DF 13 52 C0 2D 99 7F B3 B9 00 00 B2 31 8E 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 A3 10 D3 1F 2F 15 E2 13 A1 10 D3 1F
2E 15 E0 13 A3 10 D8 1F 30 15 E3 13 A1 10 D6 1F 2E 15 E0 13 9E 10 D8 1F
2D 15 DE 13 9D 10 D6 1F 2E 15 DE 13 98 10 D3 1F 2E 15 DC 13 96 10 D1 1F
31 15 DE 13 95 10 D3 1F 31 15 DE 13 94 10 D2 1F 31 15 DD 13 93 10 D4 1F
2E 15 DA 13 95 10 D5 1F 2F 15 DC 13 52 80 2E 99 7F B3 B9 00 00 B2 31 8E
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 9A 10 D4 1F 2F 15
DE 13 A0 10 D3 1F 31 15 E3 13 A8 10 D3 1F 32 15 E7 13 B0 10 D5 1F 31 15
EA 13 B1 10 D7 1F 30 15 E9 13 AD 10 D9 1F 30 15 E7 13 A7 10 DB 1F 2F 15
E4 13 A3 10 DC 1F 30 15 E3 13 9E 10 DB 1F 30 15 E1 13 9B 10 D6 1F 2F 15
DE 13 96 10 D1 1F 2F 15 DC 13 95 10 CE 1F 30 15 DD 13 52 40 2F 99 7F B3
B9 00 00 B2 31 8E 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
91 10 C8 1F 2E 15 D9 13 94 10 C6 1F 2F 15 DB 13 94 10 C4 1F 2F 15 DB 13
99 10 C7 1F 31 15 DF 13 A0 10 CA 1F 31 15 E3 13 A7 10 D0 1F 31 15 E6 13
AC 10 D3 1F 31 15 E8 13 AE 10 D6 1F 30 15 E8 13 B0 10 D8 1F 31 15 EA 13
AE 10 DA 1F 30 15 E8 13 A9 10 D8 1F 2F 15 E5 13 A7 10 D7 1F 2F 15 E4 13
52 00 30 99 7F B3 B9 00 00 B2 31 8E 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 AB 10 D9 1F 31 15 E7 13 A8 10 D7 1F 30 15 E5 13 A3 10
D6 1F 2F 15 E2 13 A2 10 D7 1F 2F 15 E2 13 A5 10 D8 1F 2E 15 E2 13 A7 10
DB 1F 2F 15 E4 13 A4 10 DB 1F 2F 15 E2 13 A4 10 DA 1F 2D 15 E1 13 A7 10
D9 1F 2D 15 E2 13 A7 10 D8 1F 2C 15 E1 13 AC 10 DB 1F 2F 15 E6 13 AF 10
DF 1F 31 15 E9 13 00 00 00 00 00 00 00 00 00 00**

Coding Example for GMS Satellite
````````````````````````````````

The GMS satellite system requires that DCP data transmission use a long
preamble, recommends that the length of time for data block be at least
63 seconds, and that transmitted data conform to a specified character
set. A base-44 coding algorithm was developed for converting binary data
to the GMS character set. The coded data format follows:

.. tabularcolumns:: |p{3.5cm}|p{2cm}|p{2.5cm}|p{2.5cm}|p{3.5cm}|

.. table::
    :widths: auto
    :align: center

    =============================== ================= ================== ================  ===================
    .. centered:: **HEADER 21 BYTES**
    ----------------------------------------------------------------------------------------------------------
    **Field**                       **Length (bit)**  **Length (word)**  **Position**      **Frame**
    Time Day of the year            12 Bits           3/4 word           0 word - 0.75
    Minute of the day               12 Bits           3/4 word           0.75 word - 1.5
    Offset for C1                   8 Bits            1/2 word           1.5 word - 2.0
    Offset for C2                   8 Bits            1/2 word           2.0 word - 2.5
    Offset for C3                   8 Bits            1/2 word           2.5 word - 3.0
    Offset for C4                   8 Bits            1/2 word           3.0 word - 3.5
    Flag #1 & #2                    16 Bits           1 word             3.5 word - 4.5
    Station colatitude              12 Bits           3/4 word           4.5 word - 5.25
    Station longitude               12 Bits           3/4 word           5.25 word - 6.0   -18 byte
    \                                                                                      (CR-CR-LF)-21 byte
    .. centered:: **FREE SPACE 27 BYTES CODED**
    ----------------------------------------------------------------------------------------------------------
    **Field**                       **Length (bit)**  **Length (word)**  **Position**      **Frame**
    D1 Indices and Basline control  8 Bits            1/2 word           6.0 word - 6.5
    ...
    D18 Indices and Basline control 8 Bits            1/2 word           15.5 word - 15.0  -48 byte
    \                                                                                      (CR-CR-LF)-51 byte
    .. centered:: **MINUTE VALUES 157 BYTES CODED**
    ----------------------------------------------------------------------------------------------------------
    **Field**                       **Length (bit)**  **Length (word)**  **Position**      **Frame**
    C1 for t+0 minute               16 Bits           1 word             15.0 word - 16.0  -54 byte
    C2 for t+0 minute               16 Bits           1 word             16.0 word - 17.0  -57 byte
    C3 for t+0 minute               16 Bits           1 word             17.0 word - 18.0  -60 byte
    C4 for t+0 minute               16 Bits           1 word             18.0 word - 19.0  -63 byte
    ...
    C4 for t+4 minute               16 Bits           1 word             34.0 word - 35.0  -111 byte
    \                                                                                      (CR-CR-LF)-114 byte
    C1 for t+5 minute               16 Bits           1 word             35.0 word - 36.0  -117 byte
    ...
    C4 for t+9 minute               16 Bits           1 word             54.0 word - 55.0  -174 byte
    \                                                                                      (CR-CR-LF)-177 byte
    C1 for t+10 minute              16 Bits           1 word             55.0 word - 56.0  -180 byte
    ...
    C1 for t+11 minute              16 Bits           1 word             59.0 word - 60.0  -192 byte
    C2 for t+11 minute              16 Bits           1 word             60.0 word - 61.0  -195 byte
    C3 for t+11 minute              16 Bits           1 word             61.0 word - 62.0  -198 byte
    C4 for t+11 minute              16 Bits           1 word             62.0 word - 63.0  -201 byte
    CRC                             16 Bits           1 word             63.0 word - 64.0  -204 byte
    \                                                                                      (CR-CR-LF)-208 byte
    =============================== ================= ================== ================  ===================

Time Framing for GMS
````````````````````

A multiple data transmission (12-minute data block repeated 3 times) may be used to satisfy
the GMS minimum block transmission time of approximately 63 seconds. The time framing for GMS
would be:

.. highlight:: none

::

     no-signal carrier          5.0 second   : 5.0 sec
     bit synchronization        2.5          : 7.5
     word synchronization       0.15         : 7.65
     address                    0.31         : 7.96
     first (64*3+16-1)*8/100   16.56         :24.52 (177 bytes)
     second (64*3+16-1)*8/100  16.56         :41.08 (177 bytes)
     last (64*3+16)*8/100      16.64         :57.72 (178 bytes)
     EOT-EOT-EOT                0.24         :57.96

The following table shows time slots assigned to DCPs. Each table line represents 60 seconds,
the station ID is placed at the beginning of a data transmission block, '....' is for the
no-signal (carrier only) period, '- -' is for synchronization sequence, and '==' is for the
data block.

Assigned time slots for the GMS coding would allow 58 seconds per transmission and 7 seconds
guard time. This would allow 11 observatories to transmit every 12 minutes.

.. highlight:: none

::

     min sec0....*....1....*....2....*....3....*....4....*....5....*....
     12*(n) .....--M01================================================__
     +01    _____.....--M02=============================================
     +02    ===_______.....--M03========================================
     +03    ========_______.....--M04===================================
     +04    =============_______.....--M05==============================
     +05    ==================_______.....--M06=========================
     +06    =======================_______.....--M07====================
     +07    ============================_______.....--M08===============
     +08    =================================_______.....--M09==========
     +09    ======================================_______.....--M10=====
     +10    ===========================================_______.....--M11
     +11    ================================================____________
     12(n+1).....--M01================================================__

Base-44 Coding for GMS
""""""""""""""""""""""


The characters used on the GMS system are: LF CR SP ' ( ) + , - . / 0 1 2 3 4 5 6 7 8 9 : = ?
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z (TOTAL 50). The base-44 character set is
shown in the table below.

Each IMFV2.83 data block is encoded by dividing the data block into 16-bit integers. Signed
integers are represented by 2's complement. Each integer value is converted to 3 base-44
numbers, <n1,-n2,n3>, the most significant being n1 and the least significant n3. Each base-44
number may be represented by a base-44 character from Table 1. Example conversions are shown
below:

.. highlight: none

::

 decimal   base-44     base-44
 number    number      char
      0    < 0, 0, 0>  000
      1    < 0, 0, 1>  001
     43    < 0, 0,43>  00?
     44    < 0, 1, 0>  010
  32767    <16,40,31>  G-V
     -1    <43,43,43>  ???
    -44    <43,43, 0>  ??0
  -1935    <43, 0, 1>  ?01
 -32768    <27, 3,12>  R3C




.. tabularcolumns:: |c|c|c|c|

.. table::
    :widths: auto
    :align: center

    ===== ======= ===== ===========
    DIGIT BASE-44 DIGIT BASE-44
    ===== ======= ===== ===========
    0     0       22    M
    1     1       23    N
    2     2       24    O
    3     3       25    P
    4     4       26    Q
    5     5       27    R
    6     6       28    S
    7     7       29    T
    8     8       30    U
    9     9       31    V
    10    A       32    W
    11    B       33    X
    12    C       34    Y
    13    D       35    Z
    14    E       36    (
    15    F       37    )
    16    G       38    \+
    17    H       39    , (comma)
    18    I       40    \- (hyphen)
    ===== ======= ===== ===========
