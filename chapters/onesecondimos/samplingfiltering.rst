.. _1sec_imo_sampling:

Data Sampling and Filtering
===========================

.. include:: ../../appendices/appendices.rst


INTERMAGNET requires that the one-second filtered data values
be centered on the second. To minimize aliasing of higher
frequency signals into the pass-band of the final second data
series, anti-aliasing filters should be included in the
analogue portions of magnetometers before analogue-to-digital
conversion. The filter responses should be matched to the
chosen primary digital sampling rate. Subsequent to the digital
sampling, INTERMAGNET requires that a numerical filter be
applied in order to obtain the final one-second data series.
INTERMAGNET does not specify the use of a particular filter
although the chosen filter must provide adequate attenuation to
meet the required specifications in :numref:`1sec_imo_instspec`.

Examples of acceptable sets of filter coefficients, for use
with various sampling rates of properly anti-aliased signals
are presented in |app_1sec_filter|.

A scalar magnetometer must provide a sample centered on the
same time as the output of the digital filter used with the
vector magnetometer.

