.. _1min_imo_sampling:

Data Sampling and Filtering
===========================

.. include:: ../../appendices/appendices.rst


In its Resolution 12 from the 1979 Assembly in Canberra, IAGA
noted the desirability of digital magnetic observatories using
a sampling rate no slower than once every 10 seconds. In that
resolution, IAGA also stated that the one-minute means must be
centered on the minute (mm:00).

To minimize aliasing of higher frequency signals into the
pass-band of the final minute data series, anti-aliasing
filters should be included in the analogue portions of
magnetometers before analogue-to-digital conversion. The filter
responses should be matched to the chosen primary digital
sampling rate. Subsequent to the digital sampling, INTERMAGNET
requires that a numerical filter be applied in order to obtain
the final minute data series.

One digital filter that is widely used by INTERMAGNET can be
achieved by applying the following coefficients (for a Gaussian
filter) to a series of 19 samples of 5-second data :

.. tabularcolumns:: |l|l|

.. table:: filter 5 sec
    :widths: auto
    :align: center

    === ==========
    C0  0.00229315
    C1  0.00531440
    C2  0.01115655
    C3  0.02121585
    C4  0.03654680
    C5  0.05702885
    C6  0.08061140
    C7  0.10321785
    C8  0.11972085
    C9  0.12578865
    C10 0.11972085
    C11 0.10321785
    C12 0.08061140
    C13 0.05702885
    C14 0.03654680
    C15 0.02121585
    C16 0.01115655
    C17 0.00531440
    C18 0.00229315
    === ==========

For a filter output value to be centered on the minute,
coefficient C0 is applied 45 seconds before this minute and
coefficient C18 is applied 45 seconds after the minute.

In addition to the attenuation provided by the numerical
filter, a “natural filter” applies, estimated at -9 to -18
dB/Octave typically, caused by the decrease in energy of the
natural field with increasing frequency.

Examples of other acceptable sets of filter coefficients, for
use with various sampling rates of properly anti-aliased
signals are presented in |app_1min_filter|.

A scalar magnetometer must provide a sample centered on the
same time as the output of the digital filter used with the
vector magnetometer. INTERMAGNET recommends that the scalar
magnetometer is sampled at the highest possible rate and that
the data are filtered to one-minute values using the filter
specified in this section.

