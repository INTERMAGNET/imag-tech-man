.. _1min_imo_instspec:

Instrumentation/Specifications
==============================

.. include:: ../../shared/variables.rst

INTERMAGNET does not specify the type of magnetometer that must
be used (although a list of instrument suppliers can be
provided on request), however an IMO must try to meet the
recommendations listed below. These specifications are used by
INTERMAGNET as a guideline for reviewing data quality when data
are either submitted for an IMO application, or when definitive
data are submitted for inclusion in the INTERMAGNET archive. A
scalar magnetometer is not mandatory, but is recommended for
data quality monitoring.

.. _1min_imo_instspec_dd:

Definitive Data
---------------

.. table::
    :widths: auto
    :align: center

    ======== ====
    Accuracy ±5nT
    ======== ====

.. _1min_imo_instspec_am:

Absolute Measurements
---------------------

See :numref:`Chapter %s <abs_mes>`


.. _1min_imo_instspec_vm:

Vector Magnetometer
-------------------
.. tabularcolumns:: |l|l|

.. table::
    :widths: auto
    :align: center

    +-----------------------------------+-----------------------------------+
    | Resolution                        | 0.1nT                             |
    +-----------------------------------+-----------------------------------+
    | Dynamic Range                     | ±4000nT High Latitude             |
    |                                   |                                   |
    |                                   | ±3000nT Mid/Equatorial Latitude   |
    +-----------------------------------+-----------------------------------+
    | Band pass                         | D.C. to 0.1Hz                     |
    +-----------------------------------+-----------------------------------+
    | Sampling rate                     | 1Hz                               |
    +-----------------------------------+-----------------------------------+
    | Thermal stability                 | 0.25nT/°C                         |
    +-----------------------------------+-----------------------------------+
    | Long term stability               | 5nT/year                          |
    +-----------------------------------+-----------------------------------+


.. _1min_imo_instspec_sm:

Scalar Magnetometer
-------------------
.. tabularcolumns:: |l|l|

.. table::
    :widths: auto
    :align: center

    ============= ================
    Resolution    0.1nT
    Accuracy      1nT
    Sampling rate 0.033Hz (30 sec)
    ============= ================


.. _1min_imo_instspec_ct:

Clock Timekeeping
-----------------

.. tabularcolumns:: |l|l|

.. table::
    :widths: auto
    :align: center

    +-----------------------------------+-----------------------------------+
    | Observatory data logger           | 5 seconds centered on UTC minute  |
    |                                   | (mm:00)                           |
    +-----------------------------------+-----------------------------------+
    | Data collection platform          | ±1.5 sec GOES, GMS                |
    |                                   |                                   |
    |                                   | ±1.0 sec METEOSAT                 |
    +-----------------------------------+-----------------------------------+

.. _1min_imo_instspec_rec:

Recorder
--------

An on-site recorder is necessary so data are not lost as a result of data
transmission outages.


.. _1min_imo_instspec_trans:

Transmission
------------

Transmission to a Geomagnetic Information Node (GIN) must be
over the Internet or by satellite, within 72 hours of
acquisition or sooner (see :numref:`sub_dat_intro_rtpd` ).

 .. note::

    Keeping within the time slot for satellite transmission
    is an important duty of an IMO operator. When advised by a GIN
    of a time drift, the IMO operator must make the necessary
    corrections within 24 hours.


.. _1min_imo_instspec_other:

Other
-----

.. tabularcolumns:: |l|l|

.. table::
    :widths: auto
    :align: center

    +--------------------------+------------------------------------------+
    | Preliminary data         | transmitted in IAGA2002 format (IMFV2.83 |
    |                          | for satellite)                           |
    +--------------------------+------------------------------------------+
    | Definitive data          | to be submitted annually for inclusion   |
    |                          | in the IRDS in IAFV2.11 format           |
    +--------------------------+------------------------------------------+
    | Instrument baseline data | to be submitted annually for inclusion   |
    |                          | in the IRDS in IBFV2.00 format           |
    +--------------------------+------------------------------------------+
    | Annual means             | to be submitted annually for inclusion   |
    |                          | in the IRDS in IYFV1.02 format           |
    +--------------------------+------------------------------------------+
    | Filtering                | to INTERMAGNET standard                  |
    |                          | (:numref:`1min_imo_sampling` )           |
    +--------------------------+------------------------------------------+

.. centered:: For more information see :numref:`sub_dat_intro_df` for Data Formats and :numref:`sub_dat_intro_dt` for Data Types.

.. _1min_imo_instspec_pgr:

Proton Gyromagnetic Ratio
-------------------------

In 2009, INTERMAGNET adopted the new proton gyromagnetic ratio (for H\ :sub:`2`\ O, sphere, 25°C) 
published by the CODATA group in 2006 (see |codata_2006_proton_gr| ):

.. math::

   g_p = 2.675153362*10^8 . T^{-1}S^{-1}

This ratio divided by 2 pi relates the magnetic field strength in T to the output frequency (Larmor frequency) of a proton magnetometer in Hz. For example, a field strength of 50000.00 nT gives a Larmor frequency of 2128.819 Hz.
