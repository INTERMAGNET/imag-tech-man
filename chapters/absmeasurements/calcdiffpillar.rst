.. _abs_mes_calc_diff_pill:

Calculation of the Difference Between F Pillar and Absolute Pillar
===================================================================

If :math:`F_v` is the magnetude of the magnetic vector at the
primary absolute pillar, and :math:`p = F_v-F_s` is the
constant magnetic vector difference between the primary pillar
and auxiliary pillar used to measure scalar F, then:

.. math::

    F_v^2 - F_s^2 = (F_s + p) . (F_s+p) - F_s.F_s = 2 F_s . p + p.p


If we set :math:`F_s = F_s^0 +  \delta` , where :math:`F_s^0`
is constant typical value and the :math:`\delta` is time-dependent variation

.. math::

    F_v^2 - F_s^2 &=  2 F_s^0 . p + p.p + 2 \delta.p\\  &or \\
   (F_v - F_s)(F_v + F_s) &= (2 F_s^0.p + p.p) + 2  \delta.p


:math:`F_v-F_s` is the scalar pier difference at any
moment in time. The variable terms are :math:`(F_v+F_s)` and :math:`2\delta.p`.
In some situations, such
as auroral observatories on highly-magnetic volcanic rock, :math:`\delta`
and/or p may be large, and :math:`F_v-F_s` may show a
measureable variation. In this case a simple scalar pier
correction is not sufficient. This can be tested by measuring
the total field at both locations for some time with some
variation in :math:`\delta`. If there is no variation in
:math:`F_v-F_s` outside the measurement noise then a
simple scalar correction is acceptable. Otherwise a vector pier
correction needs to be determined and applied. The simplest
determination of p is by direct vector measurement using
variometer corrections. If this is not possible or convenient,
then it may be possible to determine p by a multi-linear
regression of :math:`(F_v^2 - F_s^2)` against :math:`\delta` as measured by a variometer.

The application of this vector pier correction then requires
reasonably calibrated variometer data to remove the first order
changes in :math:`F_v-F_s`.

