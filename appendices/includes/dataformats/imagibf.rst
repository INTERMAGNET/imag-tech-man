.. _app_imag_ibf:

INTERMAGNET Baseline Format : IBF
---------------------------------

.. _app_imag_ibf_v2:

IBFV2.00 (2009 and after)
`````````````````````````

This file format is to be used to provide baselines for use in examining
equipment and environmental quality (mainly thermal stability of the
variometers). This
format makes room for all published components, including a baseline to
scalar data. After a one-line header, the first section contains the
observed baseline values on the days when they are measured.
Consequently the number of entries will depend upon the schedule for
absolute measurements at the observatory. The second section contains
adopted baseline values, representing each day of the year. The third
section for comments is mandatory. This comment section must include a
brief description of the baseline adoption method.

.. highlight:: none

::

    COMP_HHHHH_FFFFF_IDC_YEARCrLf
    DDD_aaaaaa.aa_bbbbbb.bb_zzzzzz.zz_ssssss.ssCrLf
    . . .
    . . .
    . . .
    DDD_aaaaaa.aa_bbbbbb.bb_zzzzzz.zz_ssssss.ssCrLf
    *CrLf
    001_AAAAAA.AA_BBBBBB.BB_ZZZZZZ.ZZ_SSSSSS.SS_DDDD.DD_mCrLf
    002_AAAAAA.AA_BBBBBB.BB_ZZZZZZ.ZZ_SSSSSS.SS_DDDD.DD_mCrLf
    003_AAAAAA.AA_BBBBBB.BB_ZZZZZZ.ZZ_SSSSSS.SS_DDDD.DD_mCrLf
    . . .
    . . .
    . . .
    366_AAAAAA.AA_BBBBBB.BB_ZZZZZZ.ZZ_SSSSSS.SS_DDDD.DD_mCrLf
    *CrLf
    Comments:CrLf
    .....................................................CrLf
    .....................................................CrLf

Component values are coded as signed float numbers, right justified with
format (1X,F9.2). DeltaF values (denoted as DDDD.DD) are coded as signed
float numbers, right justified with format (1X,F7.2). The field widths
must be maintained, either through zero-filling or space-filling in
order to have records of fixed length: every line is 43 characters long
in section one, and 53 characters long in section two excluding
terminator CrLf or Lf. Comment lines should not exceed 53 characters
long.

.. tabularcolumns:: |p{3cm}|p{12cm}|

.. table::
    :widths: auto
    :align: center

    ========= ==========================================================================
    Field     Description
    ========= ==========================================================================
    COMP      Order of components XYZF, DIF\_, HDZF, UVZF (see Note 1).
    HHHHH     Annual mean value of H component in nT.
    FFFFF     Annual mean value of F component in nT.
    IDC       Official IAGA three-letter station code in capital letters.
    YEAR      4-digit Year: eg, 2009.
    DDD       Day of the year.
    aaaaaa.aa Observed baseline of X, D, H or U in nT or minutes (absolute - variometer)
    bbbbbb.bb Observed baseline of Y, I, D or V in nT or minutes (absolute - variometer)
    zzzzzz.zz Observed baseline of Z or F in nT (absolute - variometer)
    ssssss.ss Observed baseline of Scalar F in nT (absolute - scalar, See Note 5)
    AAAAAA.AA Adopted baseline value of X, D, H or U in nT or minutes.
    BBBBBB.BB Adopted baseline value of Y, I, D or V in nT or minutes.
    ZZZZZZ.ZZ Adopted baseline value of Z, or F in nT.
    SSSSSS.SS Adopted baseline value of Scalar F in nT. (absolute - scalar, See Note 5)
    DDDD.DD   Representative value of Delta F for this day (see Note 2).
    m         Discontinuity marker (valid values c or d - see Note 3).
    \*        Section separator.
    \_        Space character.
    CrLf      Indicates Carriage Return and Line Feed.
    ========= ==========================================================================

File name convention is IAGYEAR.BLV e.g. BFE2008.BLV where:

-  IAG = 3-letter observatory IAGA code
-  YEAR = 4-digit year

.. note::

    #. The codes XYZF, DIF\_, HDZF, UVZF are the only supported codes of the
       components which must be listed in specified order within sections
       one and two.

    #. Delta F is defined as:

       Delta F = F(v) - F(s).

       Where F(v) represents the total field value calculated from the main
       observatory instrument ('vector F') and F(s) represents the total
       field from an independent instrument ('scalar F'). Both F(v) and F(s)
       must be corrected to the location in the observatory where
       geomagnetic absolute observations are made.

    #. Discontinuity marker: c indicates that the baselines for all
       components form a continuous series with the previous day, d
       indicates a discontinuity in the baseline of one or more components
       (i.e. step) between the current day and the preceding one. This is to
       allow the baselines to be plotted at an appropriate scale. A
       discontinuity is defined as a known operational change such as an
       instrument re-alignment.

    #. Missing values must be replaced by 99999.00 for D, H, X, Y, Z, F and
       by 999.00 for Delta F. Components that are not observed, which may
       include Scalar F (SSSSSS.SS) and Delta F (DDDD.DD), must be coded
       88888.00 and 888.00 respectively.

    #. The observed and adopted F baselines represent the DIFFERENCE in the
       F component between the absolute position and the continuously
       recording scalar instrument. Pier corrections are not applied to the
       data before computing the baselines.

.. _app_imag_ibf_v1_20:

IBFV1.20 (2008 and before)
``````````````````````````

This format is to be used to provide baselines for use in examining
equipment performance and for inclusion on the INTERMAGNET DVD. The
first section contains the observed baseline values on those days on
which they were measured. Consequently the number of entries will depend
upon the schedule for absolute measurements at that observatory. The
second section contains adopted baseline values representing each day of
the year. A comment section is also provided.

.. highlight:: none

::

   COMP_HHHHH_IDC_YEARCrLf
   DDD_AAAAAAA_BBBBBBB_ZZZZZZZ CrLf.
   . . . . .
   . . . . .
   . . . . .
   DDD_AAAAAAA_BBBBBBB_ZZZZZZZ CrLf.
   *
   001_AAAAAAA_BBBBBBB_ZZZZZZZ_FFFFF CrLf.
   002_AAAAAAA_BBBBBBB_ZZZZZZZ_FFFFF CrLf.
   003_AAAAAAA_BBBBBBB_ZZZZZZZ_FFFFF CrLf.
   ...
   366_AAAAAAA_BBBBBBB_ZZZZZZZ_FFFFF CrLf.
   *
   Comments:

Component values are coded as signed integers, right-justified with a
field width of 7. Total field (Delta F) values are coded as signed
integers, right-justified with a field width of 5. The field widths must
be maintained, either through zero-filling or space-filling. The '+'
sign for positive values is optional.

.. tabularcolumns:: |p{3cm}|p{12cm}|

.. table::
    :widths: auto
    :align: center

    ======= =======================================================================================================================
    Field   Description
    ======= =======================================================================================================================
    COMP    Order of components HDZF, XYZF, DIF, UVZF
    HHHHH   Annual mean value of H component in nT.
    IDC     IAGA three-letter observatory ID code eg: BOU for Boulder, OTT for Ottawa, LER for Lerwick, etc.
    YEAR    4-digit Year: for example, 1991.
    DDD     Day of the year.
    AAAAAAA Signed value of H, D, U or X in 0.1 nT
    BBBBBBB Signed value of D, I, V or Y in 0.1 nT or 0.1 min of arc for D
    ZZZZZZZ Signed value of Z or F in 0.1 nT
    FFFFF   Signed value of Delta F, the difference between calculated and observed value of F (by a proton magnetometer) in 0.1 nT
    \*      Section separator.
    \_      Space character.
    CrLf    Indicates Carriage Return and Line Feed.
    ======= =======================================================================================================================


Missing values must be replaced by 999999 for D, H, X, Y, Z and by 9999
for F.

File name convention is IAGYR.BLV where:

-  IAG = 3-letter observatory IAGA code
-  YR = 2-digit year



