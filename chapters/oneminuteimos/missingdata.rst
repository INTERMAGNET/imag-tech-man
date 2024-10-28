.. _1min_imo_missing:

Missing Data
============

When mean or filtered values are to be calculated, the question
of how to handle missing data arises. For a number of reasons
it is difficult to devise a simple objective rule that can be
applied to all cases. INTERMAGNET recommends a simple and
pragmatic approach: mean or filtered values may be calculated when 90% or
more of the values required for calculation are
available.  This can be interpreted as either 90% of the values or 90% of the 
weight of the filter. When fewer than 90% of the required values are
available the value should be assigned the value used to
flag missing data. INTERMAGNET recommends adoption of this rule
for both simple mean and weighted mean calculations. For
example, a simple daily mean value may be computed when 1296 or
more one-minute values are available for the day. Similarly, if
a one-minute value is constructed from one-second samples, the
one-minute value may be computed when 54 or more one-second
samples are available. In either case the weights applied to
each sample in the mean or the filter must be re-normalized to
account for the reduced number of samples available. In
practice, this means dividing the sum of samples by the number
of available samples in the case of a simple mean or
normalizing to unity those coefficients that have been used in
a filter calculation. INTERMAGNET observatories are expected to
provide high levels of data continuity, so this rule is
expected to be applied only rarely. To avoid the propagation of
missing values into higher level means, it is recommended to
calculate all higher level means using the method described in
:numref:`sub_dat_mean_std`.
