.. _sub_dat_prel_data:

Submission of Preliminary Data
==============================

.. include:: ../../shared/variables.rst

.. include:: ../../appendices/appendices.rst


An observatory sends preliminary (non-definitive) data to its
assigned GIN via email, web upload or satellite transmission.
INTERMAGNET encourages observatories to send data as close to
real-time as possible. The best way to achieve this is using
the web interface to submit data in IAGA-2002 format.
Observatories are also encouraged to make regular submissions
of quasi-definitive data using the same methods for submitting
data.

.. _sub_dat_prel_upf:

Update Frequencies and Formats for Preliminary Data
---------------------------------------------------

GINs can receive data in IAGA-2002 and IMFV1.23 formats. These
formats are fully defined and described in |app_imag_imfv_1| and
|app_iaga_2002|. GINs also support IMFV2.83 format, but only where
an observatory is transmitting via satellite. IMFV2.83 is
defined in |app_imag_imfv_2|. Preliminary data cannot be accepted by
GINs in other formats (expect where a GIN makes arrangements to
receive data from its own observatories in a private format –
in these cases the data must be converted to IAGA-2002 before
forwarding to the INTERMAGNET web site).

GINs can receive ‘fragments’ of a day file – that is day files
that are incomplete – in any of these formats and recombine the
fragments into a day file in IAGA-2002 format. In this way
observatories can send multiple short data files that contain
only the data from the end of the previous transmission up to
what has been most recently recorded. This allows an
observatory to update the INTERMAGNET web site in near
real-time for the current day as the day progresses.

GINs will overwrite data if they receive data that has
previously been sent. This allows observatories to send data in
close to real-time, then correct that data at a later date
(e.g. after manual gap filling or spike removal).

IAGA-2002 is the preferred format for observatories to send
data to INTERMAGNET. The format is flexible enough to allow
very small fragments of day files to be transmitted easily,
whereas IMFV1.23 format requires a minimum of 1-hour of data to
be encoded in a file (though where a fragment is smaller than
an hour, the remainder of the 1-hour block could be coded as
missing values). Observatories sending data in IMFV1.23 should
be aware that the GIN will convert their data to IAGA-2002
format. INTERMAGNET intends to stop supporting the IMFV1.23
format at some point in the future. The smallest fragment of
data that should be encoded into an IAGA-2002 file is 2
samples, since some software using this format calculates the
sample rate from time difference between the first pair of
samples in the file.

There are a number of ways that observatories can combine the
different transmission methods that INTERMAGNET offers to
achieve reliable throughput of data in near real-time. Two of
the most successful have been:

#. To use the web interface to submit small data fragments to
   the GIN. The web interface returns a code indicating
   successful upload of data. If this code is not received, the
   observatory can flag that this data was not uploaded and
   attempt to upload it again (along with any new data) on a
   subsequent upload.
#. It is not always easy to keep track of whether data has been
   successfully uploaded (and it is likely to be only a small
   number of occasions where there is a problem). An
   alternative is to submit regular small fragments of a day
   file throughout the day via the web interface, without
   tracking their successful upload, then submit a complete day
   file via email shortly after the day has ended, which will
   have the effect of filling any gaps that occurred from
   unsuccessful transmission via the web interface.

Other combinations of data transmission are possible if they
suit and observatory’s working practice. As at 2016, the
fastest rate at which data is being sent using these techniques
is every 3 minutes (i.e. files of 1-minute data with 3 samples
per file).

.. _sub_dat_prel_types:

Types of Preliminary Data
-------------------------

In the past INTERMAGNET has collected Reported (or Variometer)
data - preliminary data without a baseline. New observatories
are not allowed to send data of this type and existing
INTERMAGNET observatories are encouraged to stop sending this
data and instead send baseline corrected data using the
Adjusted (or Provisional) data type.

Observatories should send Adjusted (or Provisional ) data as
close to real-time as possible.

Observatories are encouraged to send quasi-definitive data to
the GIN as well as adjusted data, unless they are producing
quasi-definitive data in near real-time, in which case it is
sufficient to just send quasi-definitive data. Quasi-definitive
data need not be produced in near real-time – some methods of
producing this type of data do not allow for near real-time
production. However where possible observatories are encouraged
to send quasi-definitive data in near real-time.

.. _sub_dat_prel_ws:

Submission via WEB Service
--------------------------

Data can be submitted to INTERMAGNET GINs using a web service.
The web was chosen as a delivery medium because it provides the
best chance of avoiding issues with firewalls between two
institutes. The http: ‘file upload’ mechanism is used, as
described in RFC1867 "Form-based File Upload in HTML" - see
|rfc1867|. The web service responsible for receiving data
from INTERMAGNET observatories works as follows:

#. Observatories upload their data to the web service.
#. The web service indexes and caches the data, making it
   available for download by the GIN.
#. The web service provides a search mechanism by which a GIN
   can find out what data is in the cache.
#. The web service provides a download form which allows the
   GIN to download data files that observatories have uploaded
   to the cache.
#. The responses which the web service makes to these actions
   are standardised, making it easy to automate the processes
   of uploading and downloading data.

In this way, issues with firewalls are avoided, since both
observatories and the GIN access the web service using a
standard http: connection.

Observatories connect to the web service in one of three ways:

#. Manually using a standard web browser. Once connected the
   file upload is very simple, similar to the method used by
   online mail services to upload files as attachments when
   sending mail.
#. Automatically using a command line based tool that supports
   file upload. One such tool is CURL |curl| .
   which is available for SUN Solaris, Linux and Windows.
#. Automatically using their own software. File upload to a web
   server is supported by Java and other languages.

The web service will accept data in the following formats:

#. One-second data in IAGA 2002 format.
#. One-minute data in IAGA 2002 format.
#. One-minute data in IMF V1.23.

Data files may contain a maximum of 24 hours data. There is no
minimum quantity of data, but an IMO may not make more than
1440 uploads per day. The same file may not be uploaded more
than once. These limits are imposed to help prevent Denial Of
Service (DOS) attacks.

The first operation that the web service performs when a file
is uploaded is to parse the file to check that the file name
and contents are correct and that the file conforms to the
maximum data size and maximum number of file upload rules. Once
a file has been verified it is assigned a unique ID number
(implemented as a 64-bit integer to ensure it cannot ‘run
out’). The ID number increments for each new file uploaded. The
ID number never gets smaller. ID numbers can be used to sort
files by their time of arrival on the server.

The web service will respond to an attempt to upload a file
using a formatted response in either HTML or plain text (the
format is under control of the user). The HTML response is
designed to be easy for an interactive user to understand, the
plain text response is designed to be easy to process from
software. The first line of the response indicates whether the
attempt was successful. It will contain one of the following
words:

.. tabularcolumns:: |p{2cm}|p{14cm}|

.. table::
    :widths: 2, 2
    :align: center



    +-------------+-------------------------------------------------------+
    | Word        | Description                                           |
    +=============+=======================================================+
    | Success     | The operation succeeded.                              |
    +-------------+-------------------------------------------------------+
    | Information | The operation succeeded and there is some additional  |
    |             | information.                                          |
    +-------------+-------------------------------------------------------+
    | Warning     | The operations succeeded, but there was a problem     |
    |             | with a peripheral part of the system.                 |
    +-------------+-------------------------------------------------------+
    | Error       | The operation failed.                                 |
    +-------------+-------------------------------------------------------+
    | Exception   | The operation failed with an unforeseen problem. A    |
    |             | full description of the software fault is included.   |
    +-------------+-------------------------------------------------------+
    | Fatal       | The entire web service is not working.                |
    +-------------+-------------------------------------------------------+

The second line of the response is a message further describing
what happened. The response may include subsequent lines with
further detail.

On successful upload, the following message will be returned:

   | Success
   | Data loaded OK, data file id = <ID>

Capturing the ID of the transaction from the response allows
you to confirm that the upload was successful and to download
and view the file that you uploaded at a later date. Note that
successful delivery of data to the web service does not mean
that the data has been loaded to the GIN. The GIN’s operating
software needs to download the data from the web service and
insert it into the GIN data store. This may take a few seconds
to minutes following the upload. In exceptional circumstances a
file may be successfully loaded to the web service, but fail to
load on the GIN – these occurrences are very rare.

An example of the web service (as implemented at the Edinburgh
GIN) can be seen here:

    |gin_edin_up|

Detailed descriptions of the interface to the web service along
with some example software to upload data to the web service
are available here:

    |gin_edin_up_help|

Note that this web site is password protected – for access
apply to the GIN manager.

For more detailed information see INTERMAGNET Technical Note 9: |tn_9|.

.. _sub_dat_prel_email:

Submission via Email
--------------------

All GINs support receipt of data by email. An entire day of
data may be sent by email, or a smaller ‘fragment’ of data may
be sent (an hour, or even a few minutes) if an observatory is
sending updates more than once a day. In this case, the GIN is
responsible for reassembling the data fragments into a day
file.

Data may be sent by email in the following formats:

#. One-second data in IAGA 2002 format.
#. One-minute data in IAGA 2002 format.
#. One-minute data in IMF V1.23.

Whatever format is used, data may be submitted in one of two
ways:

#. The data may be put directly into the body of the email. In
   this case the ‘subject’ field for the mail message must
   contain the filename for the data, formatted according to
   the filename rules for the data format used. So, for
   example, if data is sent in the IMFV1.23 format for Boulder
   observatory on 15th March 1992, the mail subject line would
   be:

   Subject: MAR1592.BOU

   For 1-minute provisional Canberra data on 1st January 2002
   in IAGA2002 format the subject line would be:

   Subject: bou20020101pmin.min

   The body of the mail message should contain the data,
   formatted according to the rules of the format used. The
   body of the message should not contain anything else (e.g.
   automatic signatures) - there must be no additional text
   before or after the data. The data must be in ‘plain text’
   with no formatting. The requirement for plain text
   transmission is becoming increasingly problematic, as
   modern email clients don’t make it easy to guarantee that
   email is not formatted using HTML or Rich Text. If the
   email client you use makes it difficult to guarantee
   sending plain text emails, consider sending the data as an
   attachment instead.

#. The data may be attached to a mail message. The data must be
   contained in a file, correctly formatted for the chosen data
   format and attached to the mail message using the MIME
   (Multipurpose Internet Mail Extensions) standard. The
   attached file must be named according to the filename rules
   for the chosen data format. When data is attached to an
   email, the subject field and body of the mail message are
   ignored.

A list of GIN Internet addresses can be found in :numref:`sub_dat_intro_gin_addr`

.. _sub_dat_prel_sat:

Satellite Transmission
----------------------

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

.. _sub_dat_prel_transfer:

Transferring Data from GINs to WEB Site
---------------------------------------

GINs receive non-definitive data from observatories in either
IAGA-2002, IMFV1.23 or IMFV2.83 format. They forward this to
the INTERMAGNET web site in IAGA-2002 format only (data in
other formats will be converted to IAGA-2002 format at the
GIN). Data is transmitted frequently (e.g. every 5 minutes)
between GINs and the web site using the rsync protocol. It is
received into a ‘staging area’ at the web site, and then copied
to the data store (so not available to the public until a short
while after it has been received).

Different GINs have different practices over how far back in
time to go when transferring data to the web site, since
transferring the entire data set would be a time consuming
operation. There may be different rules for transferring the
different data types. For example a GIN may transfer
Quasi-Definitive data less frequently than Adjusted or Reported
data, but over a longer time span, since Quasi-Definitive data
is not required to be delivered within 72 hours. If there are
problems with the transfer of data from your observatory to the
INTERMAGNET web site, contact your GIN manager.


.. _sub_dat_prel_check:

How to Check if Your Data Has Been Received
-------------------------------------------


The web interface to the GIN provides a mechanism to verify
that your data has been successfully delivered (via the
‘Success’ code response to a file upload and the transaction ID
that goes with it). Email and satellite transmission, although
generally reliable, do not guarantee delivery and do not
provide a mechanism for verifying the arrival of your data.

One simple method the check whether your data has been received
is to look for the data at the INTERMAGNET web site. The delay
time from receipt of data at the GIN to data becoming available
at the web site can be as much as 20 minutes, so you need to
allow time for the data to arrive. If your data does not
arrive, contact the manager of the GIN you have sent data to
and they will investigate where the problem lies.

The Edinburgh GIN provides a ‘handshake’ for incoming data. An
email can be sent from the GIN to the observatory contact at
the start of each day describing the amount of data sent the
previous day (or a longer time back if the observatory is not
sending in near real-time). This allows the observatory to fill
in any gaps dues to transmission problems.

GINs send statistics describing the amount of data received
from all observatories registered on the GIN. These statistics
are sent out to the observatory email contact once a month,
shortly after the 72 hour period following the end of the month
to which they refer (72 hours after the end of the month, all
data should have been received). They contain summary
information on the completeness of the previous month’s data.

The INTERMAGNET web site keeps CSV files that describe, on a
minute by minute basis, the difference between the current time
and the time stamp of the most recently received data from each
observatory – the observatory’s lag time. These files are
useful for analysing an observatory’s near real-time
performance. These files are available via the ftp service on
the INTERMAGNET web site – for more information contact the web
manager.

.. _sub_dat_prel_probs:

Common Problems with Data Transmission
--------------------------------------

The two most common problems are in incorrectly implemented
data formats and missing email.

When you first connect to INTERMAGNET your observatory will be
assigned a GIN. The GIN manager will work with you to set up
regular transmissions of data from your observatory. It is
helpful if you can supply a sample of the data you will submit.
This will give the GIN manager a chance to check the format you
are using before you start regular transmissions.

An increasing problem with email transmission is the filtering
of emails for unwanted and malicious messages. Whilst these
filtering systems are necessary to protect users of email
systems, they do frequently block data messages of the type
exchanged in INTERMAGNET. Getting to the bottom of this type of
problem may take a little time as GIN managers do not have
direct control of mail filtering systems. When investigating
this type of problem you will need to provide the GIN manager
with the full email address that you send mail from and the
date and time of a message that was sent. This will allow the
administrators of the filtering system to track your message
and describe what happened to it.

.. _sub_dat_prel_delays:

Data Publication Delays
-----------------------

INTERMAGNET understands that some institutes would like to
restrict their data for the public within a defined time
period. Although INTERMAGNET encourages institutes to deliver
their data within 72 hours, the INTERMAGNET website and FTP can
enforce these rules to secure their data.

By default, if the institute does not request a data
publication delay, it will be published once received by
INTERMAGNET.

Two data publications delays can be requested:

-  Plotting delay
-  Download delay

For example, an institute can request that their data be
plotted (image) as soon as received by INTERMAGNET but prevent
the data files from being downloaded until the following day.

| To request a data delay, the institute can contact the webmaster at
| nrcan.geomag-webmaster-geomag-webmaster.rncan@canada.ca .


-  **Plotting delay**

   The INTERMAGNET website offers online plotting utilities.
   |download_plot_data| . A delay (in days) can be added to prevent the user from
   plotting the data.

-  **Download delay**

   Data can be download via the website.
   |download_plot_data| . A delay (in days) can be added to prevent the user from
   downloading the data.

-  **Exception**

   There is, however, an exception to this feature. No matter
   the delay requested by the institute, INTERMAGNET will
   generate hourly range values from the data and will use
   these values for the INTERMAGNET Geomagnetic Activity Map.
   It was determined by INTERMAGNET that hourly range
   values are too low resolution to be of any use.
