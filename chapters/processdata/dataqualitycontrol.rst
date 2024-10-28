.. _proc_dat_dqc:

Data Quality Control & Processing Tasks
=======================================

.. include:: ../../shared/variables.rst

Routines and procedures for inspecting and processing
observatory data will vary between observatories and institutes
so there is no set method or list of tasks that precisely
detail how quality control is to be managed. However, to meet
the standards for definitive one-minute and one-second data as
specified by INTERMAGNET, an observatory is best advised to
adopt a routine of data inspection, inter-comparison, data
cleaning and baseline estimation. By regularly performing these
tasks, many data problems can be identified and rectified
quickly, thus maintaining the quality of the near real-time
data published by an observatory, but also the quality of the
definitive data produced at the end of the year. Tasks, such as
baseline fitting on a weekly or monthly basis, will simplify
the production of definitive data as well as improve its
quality. As a general guide, typical quality control tasks have
been listed here according to how often they are performed.

.. _proc_dat_dqc_day_tasks:

Daily Data Quality Tasks
------------------------


Most observatories will have a daily routine for assessing the
performance of instruments and identifying any artificial
signal in the recorded data. Tasks such as collecting data,
applying instrument scale values, filtering to
one-second/one-minute and plotting magnetograms are normally
performed automatically, leaving the observer to:

- Manually inspect magnetograms (and optionally power spectra)
  to identify both natural signal and artificial disturbance
- Plot inter-comparisons between instruments
- Plot inter-comparisons with data from nearby observatories
- Perform cross-correlation between instruments to detect
  timing inconsistencies
- Identify noise (steps, spikes, etc.) and correct by either
  flagging, filling or performing an interim baseline
  adjustment
- Record observatory changes and events in the observatory diary
- Transmit reported data within 72 hours of recording with
  approximate adopted baselines
- Optionally transmit observatory indices

Instrument comparisons (both vector-vector comparisons and the
vector-scalar comparisons described in :numref:`proc_dat_tot_f_dif` )
are a very useful quality control tool, particularly when all
data are corrected to a common point i.e. the absolute pillar. In
comparing two or more instruments, the observatory is operating
a magnetic gradiometer that is very sensitive to instrument
problems or changes in the measuring environment. In comparing
three or more systems, it is often possible to detect problems
and also identify the source of the problem. In a similar way,
inter-comparisons with nearby observatories are a convenient
way to detect localised problems, particularly over long time
series.

Observatories are advised to maintain a detailed observatory
diary, recording significant events and changes that may have
an influence on data quality. Similarly, any manual changes to
the data, such as removing spikes or filling data of one
instrument from another, should be logged for future reference.
Procedures for editing data vary between observatories, but it
is considered good practice to preserve all original data in an
unedited state, with edits applied either on a copy of the data
or using a separate flagging system. Either way, maintaining an
edit log and version control should allow information on data
edits to be preserved and edits rolled back where required.

.. _proc_dat_dqc_week_tasks:

Weekly Data Quality Tasks
-------------------------

Observatories will have specific tasks associated with making
and processing absolute observations and baseline modelling
that are performed at least weekly. This is an opportune time
to make a more accurate assessment of the applied baselines and
to optionally transmit adjusted data with an improved level of
data quality to the reported data. Weekly tasks typically
include:

- Performing absolute observations
- Making a scalar site difference measurement between the
  scalar instrument and the absolute pillar
- Reducing the absolute observations and the variometer data
  to observed baselines
- Plotting and inspecting observed baselines, identifying and
  evaluating steps and drifts
- Approximately modelling the adopted baseline for application
  to reported and adjusted data
- Transmitting adjusted data with approximate adopted
  baselines (plus spikes removed and gaps filled) within 7
  days of recording


.. _proc_dat_dqc_month_tasks:

Monthly Data Quality Tasks
--------------------------

It is also good practice to re-evaluate data after a period of
time when there are a number of observed baselines available
before and after that data point. This allows for a more
accurate adopted baseline to be calculated at a time when
outlying observations can more easily be identified and removed
and when there is a clearer view of instrument drifts or steps.
If this process is performed within three months of the data
being recorded, then these improvements to baselines (and
therefore the resulting data) may be sufficient to re-submit
the data to INTERMAGNET as quasi-definitive as described in
:numref:`proc_dat_qdef` .

An additional data quality task than can be a useful reference
for definitive data processing is the production of monthly
bulletins i.e. a catalogue daily magnetograms plus a record of
the approximate baselines adopted at that time. Monthly
bulletins can also be used to log information that is of use to
annual definitive data processing such as significant
observatory events and natural signal identified in the data
during the month.

.. _proc_dat_dqc_an_tasks:

Annual Data Quality Tasks
-------------------------

Following the end of each calendar year, observatories are
required to finalise baselines and produce a definitive data
set to submit to INTERMAGNET, including observatory metadata
and derived data products (such as hourly, daily, annual means
and optionally K-indices). This process is typically scheduled
at least a month into the following year to allow baselines to
be finalised with sufficient absolute observations after the
year boundary. If routine tasks such as data cleaning and
continuous baseline adoption have been maintained throughout
the year, then producing a definitive data set can be
relatively straight forward. Observatories may also consider
publishing data to an observatory yearbook as this provides an
opportunity to preserve additional metadata to those required
by INTERMAGNET. The process for submitting data to INTERMAGNET
(definitive or otherwise) is described in :numref:`Chapter %s <sub_dat>` .

.. _proc_dat_dqc_despike:

Despiking and Removal of Artificially Disturbed Data
----------------------------------------------------

Single data points that are further away from the true signal
than the typical noise of the time series are referred to as
spikes. In the variometer data, their origin are typically
analogue signals that are short compared to the sampling rate, 
e.g. voltages in cables or magnetic fields arising
from lightning strikes) or a single error
in the analogue-digital conversion in the ADC, or single errors
arising in the transmission of digital data. Spikes are best
identified and removed from the original spot readings, in any
subsequently filtered time series (like minute means) they are
smoothed and hence difficult to identify, but still lead to degradation
of the data. Spikes can also occur in absolute scalar
magnetometer (e.g. proton magnetometers) data.

Spikes with an offset from the signal that significantly
exceeds the maximum natural variation between two consecutive
data points can be easily identified by computer algorithms and
automatically removed from the spot-reading time series. For
example, a change of say 100 nT per second will not be reached by
natural geomagnetic field variations and consequently, an
algorithm that removes data points that are more than 100 nT
away from the previous and consecutive data point can safely be
used.

Other short-term artificial disturbances in the data could
arise from magnetic objects passing by the magnetometer sensors
or from interference of the magnetometer
with radio wave or voltage variations in the power supply. Typical
problems of the first type occur if cars get too close to an
observatory or the grass is cut around a magnetometer hut, or
if a magnetometer hut is entered with magnetic objects.

When two magnetometers are operated in an observatory, such spikes usually don’t occur
simultaneously. Also, moving magnetic objects usually affect the
magnetometers differently because of the differences in
distance and/or direction they are with respect to the two
magnetometers. Therefore, spikes and disturbances can best be recognized by looking at
the difference between these two magnetometers, as this will eliminate 
the natural geomagnetic field variations that are identical at both magnetometers, 
but not the signal from moving moving magnetic objects. For two scalar magnetometers, 
calculating the total field difference is simple.  For a vector and a scalar magnetometer,
the total field difference between the two magnetometers can be calculated 
(see :numref:`proc_dat_tot_f_dif` computation of total field differences)
or between two scalar magnetometers. For two vector magnetometers, 
one can calculate the difference between the individual components 
(but note that the sensor orientation might not be identical for the two variometers). 

Another good way to facilitate the visual identification of
spikes and other short term artificial disturbances, especially in
the absence of a second magnetometer, is to plot the first
difference of a time series (e.g. a component of the
variometer, or total field). This acts like a high-pass filter
and the slow natural field changes give almost no signal in the
first difference. Spikes appear always and artificial disturbances
appear often prominently due to their high rate of field change.
Such first differences can be compared with first differences
from observatories many hundreds or thousands of kilometers away.
The time derivative of natural signals appears often as very similar 
(though not identical) over large areas. Thus, spikes and short term 
artificial signals (appearing only at one station) can be distinguished 
from natural signals (appearing at neighboring stations).

Once a spike or artificially disturbed data is identified, it
should not be used for calculating calibrated data. Often, such
corrupted data was deleted and thus removed from the archive. A more
modern approach would be to keep the corrupted raw data in the
archive and to flag it such that it is replaced by data from a
back-up system or flag it such that it is not used for the calculation of
calibrated data (possibly leading to a data gap).

.. _proc_dat_dqc_absq_cont:

Absolute Quality Control
------------------------

Absolute measurement (often also referred to as ‘absolutes’)
quality is important for geomagnetic observatories. Typical
reasons for low quality absolutes are instrument malfunction,
errors by the observer (e.g. misreading, typos, insufficient
levelling, and issues with magnetic cleanliness), timing
errors, and errors in the software used for calculating
results. Here we look especially at the declination and
inclination absolute measurements with a fluxgate theodolite
(DI-flux).

One way to judge the quality of the absolute measurements is to
look at the scatter of the baselines determined from them. This
is very helpful, but the baselines always depend on the quality
of the absolutes and the quality of the variometer, therefore
it is desirable to have quality parameters that are (as much as
possible) independent from the variometer quality.

If an erroneous absolute measurement occurs in a series of
correct absolutes, it can be identified firstly by an erroneous
value in the baseline. Secondly, it often can be identified by
erroneous fluxgate parameters, these are sensor offset and
sensor alignment with the theodolite telescope. More
information on these is given in Jankowski and Sucksdorff
(1996) [#]_, but note the sign error identified by Matzka and Hansen
(2007) [#]_. The fluxgate parameter are largely independent of the
variometer data and are very sensitive to single misreading or
typos. Also, they are indicative for mechanical or magnetic
faults of the DI-fluxgate.

To identify operator problems, you can compare the absolutes
from different observers. To identify instrument problems, one
can test the instrument against other absolute instruments,
like done at IAGA workshops or more regional instrument
comparisons.

Finally, erroneous absolutes should not be reported to
INTERMAGNET and should not be used for the baseline adoption.

.. [#] Jankowski, J. and Sucksdorff, C.: Guide for magnetic
       measurements and observatory practice, IAGA, Warsaw, p. 235,1996:
       |iaga_guide|

.. [#] Matzka, J. and Hansen, T. L.: On the various published
       formulas to determine sensor offset and sensor misalignment
       for the DI-flux, Publs. Inst. Geophys. Pol. Acad. Sci.,
       C-99, 298–303, 2007: |matzka_hansen|


