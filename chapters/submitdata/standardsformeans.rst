.. _sub_dat_mean_std:

Standards for Calculating Hourly, Daily and Annual Means
========================================================

INTERMAGNET requires that all mean values be calculated using
the rules described in the next sections.

.. _sub_dat_mean_std_hour:

Hourly Mean Values
------------------

The hourly mean values must be produced following the IAGA
rules:

- Arithmetic average of the 1-minute data
- Centered on the center of the hour (HH:29:30, HH=hour) using
  1-minute data 00-59 of the hour

.. _sub_dat_mean_std_day:

Daily Mean Values
-----------------

The daily mean values must be produced using the following
rules:

- Arithmetic average of the 1-minute data
- Centered on the center of the day (11:59:30) using 1-minute
  data 00:00-23:59 of the day

.. _sub_dat_mean_std_year:

Annual Mean Values
------------------

The annual mean values must be produced using the following
rules:

- Arithmetic average of the 1-minute data
- Centered on the center of the year (02 July 11:59:30 for a
  regular year, 01 July 23:59:30 for a leap year) using
  1-minute data 01 January 00:00- 31 December 23:59 of the
  year

.. _sub_dat_mean_std_missing:

Rule for Missing 1-minute Values
--------------------------------

When mean values are to be calculated the question of how to
handle missing data arises. For a number of reasons it is
difficult to devise a simple objective rule that can be applied
to all cases. INTERMAGNET recommends a simple and
pragmatic approach: mean or filtered values may be calculated when 90% or
more of the values required for calculation are
available.  This can be interpreted as either 90% of the values or 90% of the 
weight of the filter. When fewer than 90% of the required values are
available the value should be assigned the value used to
flag missing data.

