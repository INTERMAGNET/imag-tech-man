.. _proc_dat_baseline_adopt:

Baseline Adoption
=================

.. include:: ../../appendices/appendices.rst

A number of methods are used in observatory data processing
procedures to adopt baselines from observed baseline values. An
adopted baseline may be fitted to the baseline values by hand
or by a computer algorithm. The baseline values obtained from
the adopted baseline for each day are written to a file in the
INTERMAGNET baseline format IBFV2.00, (|app_imag_ibf|). The
format includes a section for comments pertaining to dates and
times of baseline adjustments or changes in instrumentation.
These files must be transmitted annually to INTERMAGNET along
with 1-minute data for the IRDS production.

Statistics of the difference between the adopted and observed
baseline can be generated to verify that confidence limits for
the adopted baseline meet the INTERMAGNET specifications.

:numref:`proc_dat_baseline_comp_belsk` shows
observed values (circles) and adopted baseline
values (dots) for magnetic field components X, Y, and Z for
Belsk observatory during 2003. The time series of F-P total
field differences, defined in :numref:`proc_dat_tot_f_dif`,
corresponds to the time series of adopted baseline values.

Often the baseline changes smoothly due to seasonal changes in
temperature or humidity, or from ageing of magnetometer
components. The constant segments used to adopt the baseline
shown in :numref:`proc_dat_baseline_comp_belsk`
are just one example for the adoption method.
In order to avoid jumps in the calibrated data (at the times
between segments of constant baselines), the baseline could be
adopted using continuous, linear segments or curves. For the
latter, often polynomials or splines of various degrees are
used, and can be fitted to the observed baselines by automatic
algorithms. Significant jumps in the baseline can still occur
(e.g. during maintenance work at the variometer), and these
should be reflected by the adopted baseline. Then the computer
algorithms for baseline fitting should be used separately to
fit the baselines before and after such a jump. The timing of a
baseline jump caused by maintenance often coincides with
artificially disturbed variometer data. Then the timing of the
baseline jump can conveniently be set into the time interval
where data from the variometer is not used as it is disturbed
during maintenance.

Once the baseline is adopted, the variometer can be calibrated.
To check the quality of the variometer data and the adopted
baseline, it is helpful to plot the total field differences.
For a well-adopted baseline, the total field differences
ideally should be small (e.g. smaller than 0.5 to 1 nT), and
should not depend on the shape of the baseline too much. If
there is an error in the adopted baselines, or in the
subsequent calibration procedure, then this will likely show up
in total field differences. Also, this will show up when you
calculate the differences between the absolute field values
determined in the absolute measurements minus the calibrated
data from the final data product (e.g. from the IAF files, see
|app_iaf| ) at the time of absolute measurements.
