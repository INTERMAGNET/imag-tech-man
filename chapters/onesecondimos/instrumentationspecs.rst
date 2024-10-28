.. _1sec_imo_instspec:

Instrumentation/Specifications
==============================

The parameters listed below describe the specifications of a
complete observatory system for a one-second vector data set
including recording environment, magnetometer, and data
processing procedure. INTERMAGNET does not specify the type of
magnetometer that must be used (although a list of instrument
suppliers can be provided on request), however a 1s-IMO must
meet the specifications listed below. These specifications are
used by INTERMAGNET as a guideline for reviewing data quality
when data are either submitted for an IMO application, or when
definitive data are submitted for inclusion in the archive. A
scalar magnetometer is mandatory as well as temperature
measurements of the vector magnetometer electronics and sensor
with a resolution of 0.1°C.

.. _1sec_imo_instspec_dd:

Definitive Data
---------------

Due to advances in instrumentation and observatory practice,
the INTERMAGNET requirements for one-second definitive data are
more stringent (and defined more comprehensively) than those
for one-minute data described in :numref:`Chapter %s <1min_imo>`.
The parameters listed below describe the specifications of a complete
observatory system for a one-second vector data set including
recording environment, magnetometer, and data processing
procedure. These specifications are designed such that
definitive one-minute data may be derived from definitive
one-second data by means of a suitable filter.

The absolute accuracy of one-second definitive data is
specified below as a maximum offset error of ±2.5 nT. This is
the maximum low frequency error between absolute observations.
In general, the largest source of offset error is instrumental
or thermal drift of the variometer, therefore the frequency of
absolute observations can be determined by the observer based
on the stability of the variometer, its operating environment
and its baselines.

The definitive one-second data standard is
described in more detail in INTERMAGNET
Technical Note TN6.

.. _1sec_imo_instspec_am:

Absolute Measurements
---------------------

The requirements are the same as for 1 minute
data. See :numref:`Chapter %s <abs_mes>`


.. _1sec_imo_instspec_vm:

Vector Magnetometer
-------------------



General Specifications
``````````````````````

.. tabularcolumns:: |l|l|

.. table::
    :widths: auto
    :align: center

    +-----------------------------------+-----------------------------------+
    | Time-stamp accuracy               | 0.01s centered on UTC second      |
    +-----------------------------------+-----------------------------------+
    | Phase response                    | Maximum group delay ±0.01s        |
    +-----------------------------------+-----------------------------------+
    | Maximum filter width              | 25 seconds                        |
    +-----------------------------------+-----------------------------------+
    | Dynamic Range                     | ±4000nT High Latitude             |
    |                                   |                                   |
    |                                   | ±3000nT Mid/Equatorial Lat.       |
    +-----------------------------------+-----------------------------------+
    | Data resolution                   | 1pT                               |
    +-----------------------------------+-----------------------------------+
    | Pass band                         | DC to 0.2Hz                       |
    +-----------------------------------+-----------------------------------+
    | Thermal stability                 | 0.25nT/°C                         |
    +-----------------------------------+-----------------------------------+
    | Long term stability               | 5nT/year                          |
    +-----------------------------------+-----------------------------------+



Pass Band Specifications [DC to 8mHz (120s)]
````````````````````````````````````````````
.. tabularcolumns:: |l|l|

.. table::
    :widths: auto
    :align: center

    +-----------------------------------------+---------------------------+
    | Noise level                             | 100pT RMS over 10 min     |
    +-----------------------------------------+---------------------------+
    | Maximum offset error (cumulative error  | ±2.5nT                    |
    | between absolute observations)          |                           |
    +-----------------------------------------+---------------------------+
    | Maximum component scaling & linearity   | 1%                        |
    | error                                   |                           |
    +-----------------------------------------+---------------------------+
    | Maximum component orthogonality error   | 2mrad                     |
    +-----------------------------------------+---------------------------+
    | Maximum Z-component verticality error   | 2mrad                     |
    +-----------------------------------------+---------------------------+

Pass Band Specifications [8mHz (120s) to 0.2Hz]
```````````````````````````````````````````````

.. table::
    :widths: auto
    :align: center

    ======================== =================
    Noise level              10pT/ Hz at 0.1Hz
    Maximum gain/attenuation 3dB
    ======================== =================

Stop Band Specifications [0.5 Hz]
`````````````````````````````````

.. table::
    :widths: auto
    :align: center

    ============================================= =====
    Minimum attenuation in the stop band (0.5 Hz) 50 dB
    ============================================= =====



.. _1sec_imo_instspec_sm:

Scalar Magnetometer
-------------------

.. table::
    :widths: auto
    :align: center

    ============= ================
    Resolution    0.01nT
    Accuracy      1nT
    Sampling rate 0.033Hz (30 sec)
    ============= ================



.. _1sec_imo_instspec_aux_mes:

Auxiliary Measurements
----------------------

Compulsory vector magnetometer electronics and sensor
temperature measurements with a resolution of 0.1°C at a
minimum sample period of one minute.


.. _1sec_imo_instspec_rec:

Recorder
--------

An on-site recorder is necessary so data are not lost as a
result of data transmission outages.

.. _1sec_imo_instspec_trans:

Transmission
------------

Transmission by electronic means to a Geomagnetic Information
Node (GIN) must be within 72 hours of acquisition or sooner
(see :numref:`sub_dat_intro_rtpd`).



.. _1sec_imo_instspec_other:

Other
-----

.. tabularcolumns:: |l|l|

.. table::
    :widths: auto
    :align: center

    +-----------------+---------------------------------------------------+
    | Data format     | IAGA2002 or ImagCDFV1.10 (or later)               |
    +-----------------+---------------------------------------------------+
    | Definitive data | to be submitted for inclusion in the INTERMAGNET  |
    |                 | archive                                           |
    +-----------------+---------------------------------------------------+
    | Baseline data   | each component to be submitted for inclusion in   |
    |                 | the INTERMAGNET archive                           |
    +-----------------+---------------------------------------------------+
    | Filtering       | to INTERMAGNET standard                           |
    |                 | ( :numref:`1sec_imo_sampling` )                   |
    +-----------------+---------------------------------------------------+

.. centered:: For more information see :numref:`sub_dat_intro_df` for Data Formats and :numref:`sub_dat_intro_dt` for Data Types.

The consensus of the scientific community survey was that
one-second data should be accurately timestamped and the
instruments should have linear phase response. Hence, a maximum
time-stamp error has been specified and the phase response
quoted in terms of a maximum group delay, which limits the
non-linearity of the phase. Data samples may be time-shifted to
correct for latency (e.g. instrument response and filter delay)
provided that the system phase response is met. The quoted
instrument ranges are inherited from the INTERMAGNET one-minute
specification, while a data format resolution is specified to
reduce quantization noise and a maximum filter width is set to
minimize the time extent of the system response to a step input
i.e. filter ringing.

Observatories moving from one-minute recordings to one-second
recordings having definitive data quality will need to monitor
over both a larger frequency band and, due to the spectrum of
the natural magnetic field, a larger dynamic range. To meet
these stringent measurement requirements while ensuring that
the instrumentation standards are realistic, the pass band has
been split into two bands with different specifications:

#. the existing INTERMAGNET one-minute data band (DC to 120s) and
#. the extended high frequency band (8mHz to 0.2Hz)

For the low frequency band (DC to 120s), there is a higher
system noise level limit than for the high frequency band, but
more constraints on parameters affecting the absolute accuracy,
such as sensor orthogonality errors, scale and offset errors.
The offset error is expressed as a maximum error from all
sources (including instrument and thermal drift) between
absolute observations.

In the high frequency band of the pass band (8mHz to 0.2Hz),
the noise level is set at a lower level to ensure sufficient
resolution of low amplitude fluctuations in the geomagnetic
field that may occur in this frequency range. Since absolute
signal amplitude is not as critical in this band as it is in
the low frequency band, and to allow for instrument roll-off
with sufficient attenuation in the stop band, the maximum
signal gain/attenuation is specified at a less stringent 3dB in
the high frequency band.

The stop band starts at the Nyquist frequency, allowing for a
sufficiently wide transition band to set a high stop band
attenuation. This is necessary to attenuate typical natural
signals in order to avoid errors due to aliased signal in the
pass band and meet the noise specification. However, this
specification alone will not sufficiently attenuate large
amplitude artificial signals, such as 50/60 Hz mains
interference. Hence it is recommended to separately attenuate
non-natural, large-amplitude signals above the Nyquist
frequency.