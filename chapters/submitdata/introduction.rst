.. _sub_dat_intro:

Introduction
============

.. include:: ../../appendices/appendices.rst
.. include:: ../../shared/variables.rst


Membership of INTERMAGNET requires observatories to submit
both preliminary data (all types of non-definitive data 
including quasi-definitive) and definitive data. These two
types of data are sent to INTERMAGNET in different ways using
different formats. For both preliminary and definitive data
INTERMAGNET wishes to make data available to users as soon as
possible. The guidelines in this section are designed to
help observatories to achieve that goal.

For preliminary data, each
observatory is assigned to a Geomagnetic Information Node
(GIN). Observatories send their preliminary data to their
assigned GIN in ‘near real-time’. When INTERMAGNET was
formed in the 1990s, this was defined as within 72 hours
of recording. Submission of preliminary data within 72 hours 
is a minimum requirements for INTERMAGNET membership. More 
recently INTERMAGNET has requested observatories to submit 
preliminary data within these limits:

-  1-second data: Submitted and available to users within 30 seconds.
-  1-minute data: Submitted and available to users within 2 minutes.

These are challenging targets, however with modern technologies
and using the best-practice described here, they are achievable.
The process of submitting preliminary data is designed to be 
automated, so that observatories can upload data to INTERMAGNET as 
part of their automatic data recording or processing systems. 
Multiple submissions of preliminary data are possible, where an
observatory is refining the quality of the data shortly after
recording. The GIN is responsible for forwarding this data to
the INTERMAGNET web site for onward distribution to users. The
INTERMAGNET web site is the only place where users have access
to data from INTERMAGNET observatories. 

Observatories are also required to send definitive data to
INTERMAGNET. A ‘call for data’ is issued annually, describing
how data should be submitted and giving a deadline for
submission. Observatories send their definitive data to the 
Paris GIN's ftp site. This process is expected to be manual 
and only done once a year (unless there are problems with the 
data that require resubmission).

.. _sub_dat_intro_df:

Data Formats
------------

A number of data formats are in use in INTERMAGNET. In some
cases this diversity exists to support handling of different
types of data, in other cases a new format has superseded (or
partially superseded) an older one.

.. tabularcolumns:: |p{3cm}|p{3cm}|p{5cm}|p{3cm}|

.. table::
    :widths: auto
    :align: center

    +---------------------+---------------------+-----------------------------------------------+-------------------+
    | Data format         | Type of data        | Notes                                         | Reference         |
    |                     | supported           |                                               |                   |
    +=====================+=====================+===============================================+===================+
    | ImagMQTT            | Minute or second    | The preferred format for submission of        | TODO              |
    |                     | values              | preliminary data, using MQTT.                 |                   |
    +---------------------+---------------------+-----------------------------------------------+-------------------+
    | IAGA-2002           | Any regular time-   | An alternative format for submission of       | |app_iaga_2002|   |
    |                     | series geomagnetic  | preliminary data using a web service          |                   |
    |                     | data                | (MQTT is preferred).                          |                   |
    +---------------------+---------------------+-----------------------------------------------+-------------------+
    | INTERMAGNET Archive | Definitive and      | The required format for submission of         | |app_iaf|         |
    | Format              | quasi-definitive    | all cadences of definitive data except        | NOTE:             |
    |                     | minute, hourly,     | 1-second. Primarily used in the annual        | Several versions  |
    |                     | daily values and    | INTERMAGNET Reference Data Set (IRDS).        | of the format     |
    |                     | K-indices           | Although quasi-definitive data can be held in | are described.    |
    |                     |                     | this format, it is most commonly submitted to | When submitting   |
    |                     |                     | Intermagnet in IAGA-2002 format.              | data              |
    |                     |                     |                                               | observatories     |
    |                     |                     | INTERMAGNET has published data in this format | should use        |
    |                     |                     | since 1991.                                   | version 2.11.     |
    +---------------------+---------------------+-----------------------------------------------+-------------------+
    | IYF INTERMAGNET     | Annual mean values  | Primarily used for submission of definitive   | |app_iyf|         |
    | Year-Mean File      |                     | annual mean data to the IRDS.                 |                   |
    +---------------------+---------------------+-----------------------------------------------+-------------------+
    | IBF INTERMAGNET     | Baseline values and | Primarily used for submission of baseline     | |app_imag_ibf|    |
    | Baseline File       | absolute            | observation data to the IRDS.                 |                   |
    +---------------------+---------------------+-----------------------------------------------+-------------------+
    | ImagCDF             | High precision      | A required format for submission of 1-second  | |app_cdf|         |
    |                     | 1-second data       | definitive data.                              |                   |
    |                     |                     |                                               |                   |
    |                     |                     | Unlike IAGA-2002, this format has sufficient  |                   |
    |                     |                     | resolution for data that conforms to the      |                   |
    |                     |                     | INTERMAGNET one second data standard          |                   |
    +---------------------+---------------------+-----------------------------------------------+-------------------+
    | IMFV1.23 GIN        | Minute mean values  | GINs continue to support this format, but     | |app_imag_imfv_1| |
    | Dissemination       |                     | INTERMAGNET no longer recommends it.          |                   |
    | Format              |                     |                                               |                   |
    |                     |                     | Observatories are encouraged to use           |                   |
    |                     |                     | the IAGA-2002 format instead.                 |                   |
    +---------------------+---------------------+-----------------------------------------------+-------------------+
    | IMFV2.83 Satellite  | Minute mean values  | A format designed to transport compressed     | |app_imag_imfv_2| |
    | Transmission Format |                     | data via GOES and METEOSAT satellites.        |                   |
    +---------------------+---------------------+-----------------------------------------------+-------------------+


.. _sub_dat_intro_dt:

Data Types
----------

Geomagnetic data is refined over time as the various sources
from which it is composed are recorded, combined and verified.
Data type in this context describes the state that a set of
data values have reached in the process of being published,
from raw data which is read directly from one or more sensors
to definitive data which is the final product of an observatory
to which no further changes are expected. In some places the
term ‘publication level’ is used as an alternative to ‘data
type’. The data formats used with time-series geomagnetic 
data include (or imply) a data type field in their metadata. 
This data type field is explained below.

.. tabularcolumns:: |p{3cm}|p{6cm}|p{6cm}|

.. table::
    :widths: auto
    :align: center

    +------------------+------------------------+------------------------+
    | Data type        | Formats where it can   | What it means          |
    |                  | be used                |                        |
    +==================+========================+========================+
    | Reported         | IMFV1.23               | Preliminary data from  |
    |                  | (as a metadata field)  | an observatory that    |
    |                  |                        | has not had any        |
    |                  | IMFV2.83 (implied –    | baseline corrections   |
    |                  | data in this format    | applied. It may        |
    |                  | can only be            | contain spikes and may |
    |                  | ‘Reported’).           | have missing values.   |
    |                  |                        |                        |
    +------------------+------------------------+------------------------+
    | Variation        | IAGA-2002 (as a        | The data type is not   |
    |                  | metadata field)        | defined in the format  |
    |                  |                        | definition. It is      |
    |                  |                        | assumed to contain     |
    |                  |                        | data to the same       |
    |                  |                        | definition as the      |
    |                  |                        | ‘Reported’ data type.  |
    +------------------+------------------------+------------------------+
    | Adjusted         | IMFV1.23 (as a         | Adjusted data may have |
    |                  | metadata field)        | modifications made to  |
    |                  |                        | raw data to apply      |
    |                  |                        | baselines, remove      |
    |                  |                        | spikes or fill gaps.   |
    +------------------+------------------------+------------------------+
    | Provisional      | IAGA-2002 (as a        | The data type is not   |
    |                  | metadata field)        | defined in the format  |
    |                  |                        | definition. It is      |
    |                  |                        | assumed to contain     |
    |                  |                        | data to the same       |
    |                  |                        | definition as the      |
    |                  |                        | ‘Adjusted’ data type.  |
    +------------------+------------------------+------------------------+
    | Quasi-definitive | IMFV1.23, IAGA-2002    | Quasi-definitive data  |
    |                  | and IAFV2.11           | are defined as data    |
    |                  |                        | that have been         |
    |                  |                        | corrected using        |
    |                  | (as a metadata field)  | provisional baselines. |
    |                  |                        | Produced soon after    |
    |                  |                        | data acquisition,      |
    |                  |                        | their accuracy is      |
    |                  |                        | intended to be very    |
    |                  |                        | close to that of an    |
    |                  |                        | observatory’s          |
    |                  |                        | definitive data        |
    |                  |                        | product. 98% of the    |
    |                  |                        | differences between    |
    |                  |                        | quasi- definitive and  |
    |                  |                        | definitive data        |
    |                  |                        | monthly mean values    |
    |                  |                        | should be less than    |
    |                  |                        | 5nT in (X, Y, Z)       |
    |                  |                        | orientation.           |
    +------------------+------------------------+------------------------+
    | Definitive       | IMFV1.23, IAGA-2002    | Observatory data which |
    |                  | and IAFV2.11 (as a     | have been corrected    |
    |                  | metadata field) and    | for baseline           |
    |                  | IAF version prior to   | variations, have had   |
    |                  | V2.11 (implied - data  | spikes removed and     |
    |                  | in this format can     | gaps filled where      |
    |                  | only be ‘Definitive’). | possible. No further   |
    |                  |                        | change is expected and |
    |                  |                        | the quality of the     |
    |                  |                        | data is such that they |
    |                  |                        | would be used for      |
    |                  |                        | inclusion in           |
    |                  |                        | observatory year books |
    |                  |                        | and for input to the   |
    |                  |                        | World Data Centers and |
    |                  |                        | the IRDS.              |
    +------------------+------------------------+------------------------+

Where software is used to convert between formats (e.g. at GINs):

- The Reported data type is assumed to be interchangeable with
  the Variation data type.
- The Adjusted data type is assumed to be interchangeable with
  the Provisional data type.

The use of data types to describe more than the state of data
in the publication process is prone to error. INTERMAGNET is
moving to a system of describing the standard that a data set
meets and including this description alongside the data to
which it applies.


.. _sub_dat_intro_gin:

Geomagnetic Information Nodes
-----------------------------

INTERMAGNET has a two stage approach to collection and
dissemination of preliminary data. Observatories send their
data to one of 5 Geomagnetic Information Nodes (GINs). The GINs
then forward data to the INTERMAGNET web site for distribution
to users, where it is made available via web services and a data
visualisation and download application on the web site. GINs may make
provision for observatories to access their own data once it
has been sent to the GIN, but there is no public access to data
at the GINs – all public access to data is via the INTERMAGNET
web site. Both GINs and the web site keep a permanent copy of
all data sent to them – no data is deleted (though it may be
overwritten if an observatory sends an update).

INTERMAGNET will not edit any data that an observatory has
sent, though it may contact an observatory if problems are
detected and may also remove spikes for the purposes of
plotting the data. GINs will send monthly reports of the
‘completeness’ of the data received from observatories. The
INTERMAGNET web site creates daily and monthly reports 
on the numbers of requests that users have made for data
from each individual observatory. These reports are available
for everyone to see in the ‘statistics’ section of the web site. 
The manager at each GIN acts as a point of contact for IMOs to 
resolve any data transmission and formatting problems.


INTERMAGNET GIN Types
`````````````````````

The five INTERMAGNET GINs can be classified into two types,
depending on the observatories they handle and the services
they offer.

.. tabularcolumns:: |p{2cm}|p{8cm}|p{4cm}|

.. table::
    :widths: auto
    :align: center

    +-----------------------+-----------------------+-----------------------+
    | Type                  | Description           | GIN                   |
    +=======================+=======================+=======================+
    | 1                     | -  Handles data from  | Golden, Ottawa        |
    |                       |    observatories run  |                       |
    |                       |    by its own         |                       |
    |                       |    institute (and     |                       |
    |                       |    maybe a few others |                       |
    |                       |    with which it has  |                       |
    |                       |    close              |                       |
    |                       |    relationship).     |                       |
    |                       | -  Uses its own       |                       |
    |                       |    mechanisms to      |                       |
    |                       |    collect data from  |                       |
    |                       |    observatories      |                       |
    +-----------------------+-----------------------+-----------------------+
    | 2                     | -  Handles data from  | Edinburgh, Kyoto,     |
    |                       |    many IMOs not      | Paris                 |
    |                       |    associated with    |                       |
    |                       |    its own institute. |                       |
    |                       | -  Uses INTERMAGNET   |                       |
    |                       |    defined mechanisms |                       |
    |                       |    to collect data    |                       |
    |                       |    from               |                       |
    |                       |    observatories.     |                       |
    +-----------------------+-----------------------+-----------------------+

New observatories not run by USGS or GSC would normally be
assigned to one of the Type 2 GINs.


.. _sub_dat_intro_gin_mans:

GIN Managers
````````````

Any enquiries to about an individual GIN should be made to the
GIN's Manager. GIN manager contact details are
in |app_imag_addr_ginman|.

