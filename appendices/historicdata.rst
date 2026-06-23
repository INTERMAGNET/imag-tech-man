.. _app_hist_data:

Historic Data Formats
=====================

Over time some data formats used in Intermagnet have fallen
out of use or become limited in their application. This
appendix lists and documents formats that are no longer
actively used, so that any historic data that is still
available in these formats can be decoded.


.. _app_sat_trans:

Data Transmission via Satellite
-------------------------------

In the early years, Intermagnet used satellites for data transmission
because computer networks were not available at observatories.
Typically communication would take place using a data channel on
a weather satellite which had very limited bandwidth (e.g. Meteosat
which allowed 649 bytes per transmission, 1 transmission per hour). 
This required the use of a compressed data format with low resolution. 
Since that time Internet access at observatories has become common. 
Satellite transmission, which was used by many observatories and was 
received at all Intermagnet GINs, is (in 2026) only used internally at 
the Golden and Ottawa GINs for transport of USGS and NRCan data.

What follows is the description from earlier versions of the
Intermagnet Technical Manual of preparing data for transmission
via satellite.

In preparation for transmitting data to one of several possible
satellites, an IMO will first prepare its data in INTERMAGNET
format IMFV2.83 or later. This format, which is fully described
in |app_imag_imfv_2|, imposes a common structure on the data files,
ensuring that all necessary information is included so that the
data may be properly decoded at a GIN. Once data are in
IMFV2.83, a supplementary encoding step is applied to make the
data stream, as transmitted to satellites, exactly compatible
with the requirements of the satellite operators. |app_sat_cod|
shows the supplementary encoding steps for the GOES and
Meteosat satellites along with examples using a specific data
set.|app_sat_cod| also provides provisional information about
encoding for the GMS satellite.

Geostationary Satellites
````````````````````````

Orbiting the earth, 36,000 km above the equator with
approximately 72E of longitude between them are four
geostationary satellites, METEOSAT, GOESEast, GOES-West, and
GMS. The primary function of these satellites is to provide
regular updates, to meteorological agencies, of cloud and
infra-red image data which they use to produce forecasts of
weather conditions worldwide. Along with these imaging
facilities the satellites can, at regular time intervals, relay
data collected from remote ground based transmitters to users
equipped with suitable receiving and decoding equipment.

METEOSAT
````````
Each Data Collection Platform (DCP) that transmits through
METEOSAT is allocated a one-minute transmission slot every
hour. During this time, the DCP encodes and transmits to the
satellite any data input to it during the previous 60 minutes.
From the satellite, the data are relayed to the EUMETSAT
operations center at Darmstadt, Germany, where they are checked
and temporarily stored. The GIN automatically collects the data
from the EUMETSAT web site. For more information please contact
the Paris GIN manager.

GOES
````

Observatories transmitting through the GOES East/West
satellites output their data every 12 minutes to the satellite;
there is no secondary retransmission stage, as is the case with
METEOSAT. In the GOES system, the data are transmitted directly
to a receiving GIN where they are transferred to the
INTERMAGNET web site. This form of communication is simpler,
but the GOES link does require a much larger receiving antenna
as signals transmitted directly from a geostationary satellite
are at a very much lower power than those relayed using the
METEOSAT retransmission facility. To overcome the necessity for
a large 3-5m receiving dish antenna, users in or near the
United States may also access GOES East and West transmissions
using a DOMSAT (DOMestic SATellite) receiving station. This is
a retransmission facility similar to that used with METEOSAT,
providing users with a much stronger signal and hence a
considerable reduction in the size of the receiving antenna
required (1.2 - 1.8m in diameter).

Transmission Access
```````````````````

The use of satellites and the timed-transmission slots on any
of the geostationary satellites is very closely controlled.
Before an observatory can transmit data using a satellite, an
application must be made to the relevant controlling body. All
transmission equipment used must be checked and certified to be
of an acceptable standard before a licence and a transmission
slot can be granted. Also, although it may be possible to gain
free access to geostationary satellites, depending on the
institute and the use to which the data is being put, the
satellite operators may charge users for access.

Two different types of transmission authority may be necessary
before an observatory can transmit its data through a satellite
to a GIN:

#. Authority to transmit to an Earth orbiting apparatus. This
   is a licence issued by the government of a particular
   country which gives an institute permission to operate radio
   transmission equipment. This type of licence may not be
   necessary, but prospective participants should check with
   the appropriate regulatory authorities in their country to
   ensure that they are not contravening any transmission laws
   in force in their country.
#. Application must be made to the operators of whichever
   satellite is accessible from the observatory. |app_obs|
   shows the footprints of geostationary satellites and from
   this users can decide which satellite should provide the
   best transmission path. Since satellite positions are
   sometimes changed, those intending to operate an IMO near
   the edge of a footprint should contact the satellite
   operators for more detailed information concerning the
   satellite accessibility. Most satellite operators have a
   standard application form. A prospective user should write
   to the operator giving details of the proposed use to which
   the transmitted data is to be put, a brief description of
   the project and a request for a transmission slot
   application form.

If an application form has to be completed, it may include many
questions about the operator, site location, and technical
questions about the type of DCP, transmission power and whether
or not the proposed DCP has been certified for use on this
satellite by the satellite operators. To answer these
questions, it is usually necessary to contact the DCP supplier.

The completed form is then sent to the respective satellite
operator, who, after due deliberation will hopefully issue the
applicant with a satellite identification number, a
transmission frequency/channel and a specific time slot on the
allocated channel.

Alternatively, if the user or the organization to which the
user belongs is a member of the World Meteorological
Organization (WMO), access to a specific satellite and a
transmission slot may be granted simply by quoting an
identification number which has been issued by the respective
satellite operators to the member state or country.

The length of the time slots allotted to the applicant depends
on the satellite which is being accessed. A METEOSAT time slot
is 1 minute every hour. On GMS it is 90 seconds every 12
minutes and on GOES, 20 seconds every 12 minutes. During these
times users transmit their data. It is essential that the DCP
clocks maintain accurate timing, as any transmission outside
the allocated time slot will result not only in corruption of
the data being transmitted, but also of data transmitted by
users on adjacent time slots.

Satellite Operators
```````````````````

| **METEOSAT**
| EUMETSAT
| AM Kavalleriesand 31
| D-64295
| Darmstadt
| Germany
| Telephone: 49 61 51 80 77
| Fax: 49 61 51 80 75 55
| Internet: ops@eumetsat.de
| Web: www.eumetsat.de

Those whose potential IMOs would be serviced by METEOSAT are
advised to first contact the PARIS GIN operators for timely
information on access to METEOSAT.

| **GOES East and West**
| Letecia Reeves
| NOAA Satellite Operations Facility
| (NSOF), RM 1646
| 1315 East West Hwy
| Silver Spring, MD 20746
| USA
| Telephone: 1-301-817-4563
| Fax: 1-301-817-4569
| Internet: GOES.DCS@noaa.gov

Those whose potential IMOs would be serviced by GOES are
advised to first contact the GOLDEN GIN operators for timely
information on access to GOES.

Satellite Services
``````````````````

Other methods of obtaining permission to transmit via METEOSAT
and GOES East and West are:

#. Through MAEDS (Multisatellite Applications Extended
   Dissemination Service), which is a commercial organization
   based in France. This company undertakes to arrange a
   satellite transmission slot on METEOSAT and GOES.

   | CLS Service MEADS
   | 18, Av. Edouard Belin
   | Toulouse Cedex 31055
   | FRANCE

#. Through North American Collection and Location Service
   (NACL), which is a company providing similar services to
   those provided by MAEDS.

   | Mr. Peter Griffith
   | North American Collection & Location by
   | Satellite
   | 9200 Basil Court, Suite 306
   | Landover, MD 20785
   | USA
   | Telephone: 1-301-341-1814
   | Fax: 1-301-341-2130

These companies have been given the right by EUMETSAT to market
environmental data gathering services.


.. raw:: latex

    \newpage

.. include:: ./includes/dataformats/imagimfv2.rst

.. raw:: latex

    \newpage

.. include:: ./includes/dataformats/satcoding.rst




