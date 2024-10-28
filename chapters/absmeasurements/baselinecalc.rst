.. _abs_mes_bas_calc:

Baseline Calculation
====================

The magnetic field will vary during an absolute observation.
This is unavoidable since an absolute observation may take
several minutes, and the magnetic field may vary tens of nT or
more during that time, especially at high latitudes. To achieve
sub-nT estimation of the instantaneous vector baseline:

-  the timing accuracy of the clock used for the absolute
   measurements should be 1 second and each single observation
   with e.g. the DIM and PPM should be reported with 1 second
   timing accuracy

Generally, use variometer spot-readings or one-second means or
means over a few seconds (and not minute means) for reducing
the absolute measurements.

Accurate formula (as those presented in :numref:`sub_dat_def_calc`) should be
used. If approximate formulas are used, then one has to be
clear about the assumptions they are based on (some formula
currently used at observatories only work under certain
conditions, e.g. for constant geomagnetic field during the
absolute measurement or for variations of the H component being
small compared to the size of the H component, or assume a
certain sign of the vertical component (i.e. depend on
hemisphere)).

Careful synchronization between the absolute measurements and
variometer data, becomes more important as the magnetic field
activity increases.

Ideally all component measurements are made on the same pier.
For various reasons, some observatories measure components on
different piers. For example, D and I may be made on a primary
pier, and total field may be measured on an auxiliary pier;
possibly the variometer F may be used, or a dedicated scalar F
may be used on a separate pier. Some instruments such as a
proton vector magnetometer cannot be moved and the use of an
auxiliary pier is unavoidable.

If more than one pier is used, vector pier correction(s) should
be measured and applied to reduce all measurements to a primary
pier. It may be sufficient to treat scalar component pier
corrections, such as F, as a simple scalar correction, but this
is not always the case as described in :numref:`abs_mes_calc_diff_pill`.

