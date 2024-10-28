.. _app_imag_term:

INTERMAGNET Terminology
=======================

.. include:: ./appendices.rst



.. glossary::

    ADJUSTED Data
        Each observatory or its parent institute is allowed to
        modify REPORTED data files to produce ADJUSTED data, with a
        goal of 7 days after transmission. These adjustments may be
        to modify baselines, remove spikes, fill gaps etc. on any
        day file. When data are missing from an ADJUSTED data file,
        these data may be input to a GIN in a later message. This
        new message file can be transmitted to a GIN with the 'A'
        flag set in byte 25 of each hourly block header ( |app_imag_imfv_1| ).
        ADJUSTED data are maintained online until the annual
        INTERMAGNET Reference Data Set (IRDS) is available.
        They are then archived by the GIN and only
        available thereafter by special arrangement.

    DEFINITIVE Data
        This describes observatory data which have been corrected
        for baseline variations and which have had spikes removed
        and gaps filled where possible. DEFINITIVE data have each
        block header byte 25 set to 'D' (|app_imag_imfv_1|), and the
        quality of the data is such that in this form they would be
        used for inclusion into Observatory Year Books, input to
        World Data Centers and included in the INTERMAGNET Reference
        Data Set (IRDS).

    Flags
        Two bytes "Flags #1" and "Flags #2" (bytes 8 and 9) of
        Format IMFV2.83, are reserved for IMO status information
        (see |app_imag_imfv_2|).

    GIN
        Geomagnetic Information Nodes are data centers, organized on
        a regional basis, which INTERMAGNET observatories send their
        provisional data to. GINs forward this data to the
        INTERMAGNET web site. GIN managers will help INTERMAGNET
        observatories with the technical details of establishing
        reliable data flow. GINs do not distribute data to users –
        this task is done by the INTERMAGNET web site.

    IMO
        An INTERMAGNET Magnetic Observatory (IMO) is a magnetic
        observatory equipped with magnetometers, clock, control
        electronics, transmitting equipment and a data collection
        platform (DCP), residing at the magnetic observatory site.
        The operation and equipment must meet INTERMAGNET standards
        and specifications.

    IPM
        INTERMAGNET Physical Media, this term collectively
        describes the INTERMAGNET CDs, INTERMAGNET DVDs
        and INTERMAGNET USBs.

    IRDS
        INTERMAGNET Reference Data Set contains all definitive
        data and metadata from the first Intermagnet publication
        in 1991 up to the current year, including any corrections
        that have been made. Published with a DOI, for example
        the INTERMAGNET Reference Data Set, 2015:
        https://doi.org/10.5880/INTERMAGNET.1991.2015.


    Magnetic observatory
        A permanent installation of magnetometers capable of
        providing magnetic field values with an absolute accuracy of
        better than 5 nT over a period ranging from DC to
        approximately 1 Sec.

    NESS binary
        For GOES users, each 16-bit binary word is encoded as 3
        pseudo ASCII bytes, so that the 126 bytes of IMFV2.83 data
        are encoded as 189 bytes NESS binary (see |app_sat_cod|).

    Offset
        The component offset values determined by the INTERMAGNET
        coding algorithm that has been applied to recorded data for
        coding data stored in the "minute value" section of Format
        IMFV2.83 (see |app_imag_imfv_2|).

    QUASI-DEFINITIVE Data
        As the name implies, the data should be close to the
        expected definitive value, but is to be delivered more
        rapidly than an observatory’s annual definitive data. This
        initiative will be useful for a number of scientific
        activities, where timely and close-to-definitive data is
        essential. For example, quasi-definitive data will be
        particularly useful in joint analyses of geomagnetic and
        other phenomena, together with data measured by satellites.
        Quasi-definitive data are 1-minute or 1-second data
        (observatories are encouraged to produce both minute and
        second data) that can be submitted to INTERMAGNET as (H, D, Z)
        or (X, Y, Z) and have the following properties:

            A. Corrected using temporary baselines
            B. Made available less than 3 months after their acquisition
            C. Such that the difference between the quasi-definitive and
               definitive (X, Y, Z) monthly means are less than 5 nT in
               any component for every month of the year

        Point C is checked a posteriori by comparing
        quasi-definitive and definitive data from the previous year.
        Observatories are strongly encouraged to submit
        quasi-definitive data that is thoroughly controlled, i.e.
        de-spiked, free from corrupted data, data gaps filled in
        from back-up systems, and with the best possible baseline at
        the time of submission. Submission of quasi-definitive data
        should not be seen as having satisfied the requirements for
        definitive data. The annual definitive data, again
        thoroughly controlled and with a baseline based on a full
        year of absolute measurements, shall be submitted in the
        formats for definitive data at latest by the deadline agreed
        by INTERMAGNET.

    Reference Measurement (RM)
        Values provided automatically by an IMO using 2 independent
        instruments for inter-comparison. Reference Measurements are
        provided by the institute operating the observatory site
        using satellite communications to INTERMAGNET GINs using the
        Format IMFV2.83. The RMs are applied to reported data to
        produce adjusted data and to supplement baseline control.

    REPORTED Data
        Data as output by an observatory, transmitting through a
        satellite or using email. REPORTED data have not had any
        baseline corrections applied, may contain spikes and may
        have missing values. When ADJUSTED data are available,
        REPORTED data are removed from online access.

    Time stamp
        The time of the first sample of the data block:

        -  Greenwich day 1 through 366 encoded as a 12-bit binary
           number.
        -  Minute of the Greenwich day : 0 through 1439 encoded as a
           12-bit binary number (see |app_imag_imfv_2| and |app_sat_cod|).

