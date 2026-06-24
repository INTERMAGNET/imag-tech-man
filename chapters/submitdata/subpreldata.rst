.. _sub_dat_prel_data:

Submission of Preliminary Data
==============================

.. include:: ../../shared/variables.rst
.. include:: ../../appendices/appendices.rst


An observatory sends preliminary (non-definitive) data, including
quasi-defintive data, to its
assigned GIN via MQTT, web upload, email or satellite transmission.
INTERMAGNET encourages observatories to send data as close to
real-time as possible. The best way to achieve this is to use
MQTT, which requires data to be submitted in
ImagMQTT format using MQTT software to publish data to an
MQTT broker at one of INTERMAGNET's GINs.

An alternative is to submit data in IAGA-2002 format using the 
web service at an INTERMAGNET GIN. This method is unlikely
to achieve as good real-time performance as use of MQTT.

The GINs still accept data via email. Whilst this method of
data transfer is not suitable for real-time data transmission,
it can still be useful as a backup transmission method and for
backfilling gaps that might have occured when sending data
via MQTT or the web.

Satellite transmission, which was used extensively in the
times before Internet communications were widely available
at remote observatory sites, is now confined to transmissions
at the Canadian and US observatories for transfer of data
to their own GINs. It is not generally available for
observatory use.

Observatories are also encouraged to make regular submissions
of quasi-definitive data using the same methods for submitting
other types of preliminary data.

.. _sub_dat_prel_go:

Guiding Principles
------------------

The format in which preliminary data should be supplied depends on the
method used to transmit the data, but will most likely be either
ImagMQTT or IAGA-2002 format. Subsequent sub-sections of this section
of the Technical Manual describe the different transmission methods
and provide detailed information on the format that is required for
each method.

Observatories often group recorded data into ‘day files’.
GINs can receive ‘fragments’ of a day file – that is day files
that are incomplete – and recombine the
fragments at the GIN. In this way
observatories can send multiple short data files that contain
only the data from the end of the previous transmission up to
what has been most recently recorded. This allows an
observatory to update the INTERMAGNET web site in near
real-time for the current day as the day progresses.

GINs will overwrite data if they receive data that has
previously been sent. This allows observatories to send data in
close to real-time, then correct that data at a later date
(e.g. after manual gap filling or spike removal).

There are a number of ways that observatories can combine the
different transmission methods that INTERMAGNET offers to
achieve reliable throughput of data in near real-time. Two of
the most successful have been:

#. To use the MQTT method (or, less preferably the web 
   service method) to submit small data fragments to
   the GIN. Both MQTT and the web service allow detection
   of failure to receive data. If failure is detected, the
   observatory can flag that this data was not uploaded and
   attempt to upload it again (along with any new data) on a
   subsequent upload.
#. It is not always easy to keep track of whether data has been
   successfully uploaded (and it is likely to be only a small
   number of occasions where there is a problem). An
   alternative is to submit regular small fragments of a day
   file throughout the day via MQTT or web service, without
   tracking their successful upload, then submit a complete day
   file via email shortly after the day has ended, which will
   have the effect of filling any gaps that occurred from
   unsuccessful transmissions.

Other combinations of data transmission are possible if they
suit an observatory’s working practice. Using MQTT it is
possible to achieve latencies within the INTERMAGNET goal of 
30 second delay for 1-second data and 2 minute delay for
1-minute data.

.. _sub_dat_prel_types:

Types of Preliminary Data
`````````````````````````

In the past INTERMAGNET has collected Reported (or Variometer)
data - preliminary data without a baseline. New observatories
are not allowed to send data of this type and existing
INTERMAGNET observatories are encouraged to stop sending this
data and instead send baseline corrected data using the
Adjusted (or Provisional) data type.

Observatories should send Adjusted (or Provisional) data as
close to real-time as possible.

Observatories are encouraged to send quasi-definitive data to
the GIN as well as adjusted data, unless they are producing
quasi-definitive data in near real-time, in which case it is
sufficient to just send quasi-definitive data. Quasi-definitive
data need not be produced in near real-time – some methods of
producing this type of data do not allow for near real-time
production. However where possible observatories are encouraged
to send quasi-definitive data in near real-time.


.. _sub_dat_prel_mqtt:

Submission via MQTT
-------------------

For the best real-time performance (and least delay) data should be submitted to
Intermagnet using MQTT. With MQTT there is a very small delay (typically less
than a second) between an observatory submitting data and the data becoming
available on the Intermagnet data portal. Delays in data are then mainly due
to the frequency at which observatories transmit data. Observatories are 
encourged to transmit data as soon as it is recorded. This is more easily
accomplished with MQTT than other methods of data transfer.

MQTT (Message Queuing Telemetry Transport) is a messaging protocol that enables 
communication between devices in the Internet of Things. Messages are sent over
MQTT using software that conforms to the MQTT protocol - this software is
responsible for delivering your data to Intermagnet. One of the central
concepts in MQTT is that of the "broker". A broker receives messages from "publishers"
and makes them available to "subscribers". An observatory will publish data to a broker
that Intermagnet manages (and Intermagnet will subscribe to the broker in order to receive
the messages observatories send).

There are a number of suppliers of MQTT software, both commercial and free. There are
interfaces to most popular languages as well as standalone commands that can be
inegrated into scripts or schedulers (such as Unix cron). For standalone MQTT publishing
and subscription programs (as well as broker software) people in the observatory 
community have succesfully used Eclipse Mosquito MQTT (https://mosquitto.org/), which is 
free software. Binary packages are available for Windows, Linux and Mac. 
Eclipse Mosquitto also includes a library that can publish and subscribe messages from
programs written in the C language. For Python and Java programmers, the Paho project 
(https://eclipse.dev/paho/) offers a library that can be easily added to your programs (and
Paho also includes a C library, with other langauge interfaces being developed). 

MQTT at the GINs
````````````````

MQTT brokers are available at the Edinburgh, Kyoto and Paris GINs.

MQTT at the Edinburgh GIN
"""""""""""""""""""""""""

Public MQTT brokers run at the Edinburgh GIN at the following Internet addresses:

- gin-mqtt.bgs.ac.uk - main Intermagnet/BGS MQTT service
- gin-mqtt-staging.bgs.ac.uk - development Intermagnet/BGS MQTT service

Access to MQTT uses TLS, to ensure that all traffic is securely encrypted. 
Connections to these services are received on the default MQTT TLS port, port 8883.
All connections to these servers require authentication and a username and
password will be set up for each observatory. Be sure to use these in a way that
ensures that any user can connect only once at a time to the brokers, as the
brokers are configured to only allow a single connection per user (and to
log off any previously existing connections).

MQTT at the Kyoto GIN
"""""""""""""""""""""

TODO - get details from Shun

MQTT at the Paris GIN
"""""""""""""""""""""

MQTT is not yet available at the Paris GIN.


Submitting data using MQTT
``````````````````````````

MQTT data is transmitted to Intermagnet by connecting to an Intermagnet 
MQTT broker and "publishing" data messages. Before starting, please contact
the manager of the GIN that you will use in order to get a username and
password to access the MQTT broker (see :ref:`sub_dat_prel_mqtt_auth`).
MQTT messages have a topic and a payload. Topics are used to identify
and group messages. Payloads contain the message's data. To send data to
Intermagnet topics and payloads must conform to the Intermagnet MQTT topic 
and payload format descriptions that are described in |app_imag_mqtt|.

Software is needed to send MQTT messages. One simple approach is to use
the 'mosquitto_pub' command from the Mosquitto MQTT package. This is
a command line program that enables publication of a single MQTT
message. The command can be used to test access to an MQTT broker, or
can be integrated into scripts or scheduled operations on a data logger.
Here is an example of publishing a message to the Edinburgh GIN MQTT broker
using the user "esk_w" for data in the file "data-file" from the 
Eskdalemuir observatory::

   mosquitto_pub -h gin-mqtt.bgs.ac.uk \
      -p 8883 -u esk_w -P <password> -i "esk_w" \
      -t 'impf/esk/pt1m/2/xyzs' \
      -q 1 -f <data-file>

The 'mosquitto_sub' command, also from the Mosquitto MQTT pacakge, can
be used to view the transmitted message. Unlike 'mosquitto_pub' which
publishes a single message, 'mosquitto_sub' will run continuously until
it is stopped, displaying messages as they are received. Here is an
example command

   mosquitto_sub -h gin-mqtt.bgs.ac.uk -p 8883 -u esk_r -P <password> -c -t '#' -q 0 -i "test_r"

It is expected that 'mosquitto_sub' will be used by observatories to test 
receipt of MQTT messages, not as part of regular operations. Note the use
of different user IDs for publishing and subscribing (see :ref:`sub_dat_prel_mqtt_id`).

MQTT software is also available as libraries for most computer languages.
Using these libraries, transmission of data via MQTT can be closely
integrated into data loggers or data processing software.

MQTT Quality of Service
"""""""""""""""""""""""

When publishing and subscribing to MQTT, one of the parameters that needs to be set is the
"quality of service" (QoS). For a description of QoS see here: 
https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels/.

GINs will subscribe to their MQTT brokers with a QoS of 2. Observatories
are recommended to publish with a QoS of 1, which reduces the overhead needed to manage
the message stream (since the lower of the two QoS levels is used between publisher and
subsriber). However, if there is a reason why it's important to guarantee that messages
are delivered in the same order they are sent, observatories can publish using a QoS of 2.
GINs are able to handle out of sequence messages from observatories.

To enable QoS level 2 and to ensure messages are not missed, the GINs
subscribe to their MQTT brokers with a 
[persistant session](https://www.hivemq.com/blog/mqtt-essentials-part-7-persistent-session-queuing-messages/).


.. _sub_dat_prel_mqtt_id:

Importance of the MQTT Client ID
""""""""""""""""""""""""""""""""

In MQTT, publication and subscription is associated with the subscriber's and publisher's client ID,
not the username. Only one client ID may be connected to an MQTT broker at at time. If a duplicate
client ID attempts to connect to a broker, the broker will disconnect the earlier connection. For these
reasons it is important that client IDs are selected so that there can never be any duplicate IDs.

The MQTT broker allows the username (used in authenticating with the broker) to be used as the
client ID. The only way to enforce unique client IDs is to allocate unique usernames to each
client (ie each observatory) and force clients to use the username as their client ID. This is
the approach used by the Intermagnet MQTT service.


.. _sub_dat_prel_mqtt_auth:

MQTT Authentication and authorization
"""""""""""""""""""""""""""""""""""""

Each observatory wishing to send data will be assigned connection details that will be 
needed to publish data on the Intermagnet MQTT service:

- A publication username. The username will be unique to the observatory and should not be shared.
  This username is used for publishing data.
- A publication password. The publication password is linked to the publication username.
- A subscription username. The username will be unique to the observatory and should not be shared.
  This username is used for subscribing to data, to allow an observatry to check that its
  data is being received.
- A subscription password. The subscription password is linked to the subscription username.

The usernames given to each observatory will define which topics (and so which observatories)
they can publish and subscribe to.

An observatory will be allowed to subscribe to the topics that it can publish to. Because
the client ID (specified by the username) can only connect once to a broker, it is
not possible to use one username to publish and subscribe at the same time. The username 
assigned for publication must be used only for publishing. A second username and password 
allows subscription at the same time as publication.

From a client perspective it isn’t easy to know if MQTT access control is being applied, as restrictions 
aren’t notified to the client (at least in MQTT v3.1.1). The way around this for a client wanting to
verify successful publication of data is to subscribe to a topic as well publishing and check whether 
any published messages are received through the subscription.

Secure MQTT transport
"""""""""""""""""""""

Only secure (TLS) connections will be accepted by the Intermagnet MQTT service. Open
(unecrypted) connections expose the authentication and authorization credentials used
to connect to the service, thereby risking publication of data from unauthorized sources,
and so will not be accepted. The default port (8883) is used for MQTT over TLS.


.. _sub_dat_prel_ws:

Submission via WEB Service
--------------------------

Data can be submitted to INTERMAGNET GINs using a web service.
The http: ‘file upload’ mechanism is used, as
described in RFC1867 "Form-based File Upload in HTML" - see
|rfc1867|. Data should be uploaded in IAGA-2002 format 
(|app_iaf|). Observatories upload their data to the web service,
which indexes and caches the data, making it
available for download and ingestion into the GIN.
The responses which the web service makes to these actions
are standardised, making it easy to automate the processes
of uploading data. One of the primary goals of the web service
is to allow data to be safely imported from the public
Internet into the private networks where the GINs operate.
This process introduces a short delay between transmission
of the data and ingestion into the GIN, which is the reason
MQTT is preffered for transmission of preliminary data with
minimum delay.

Observatories connect to the web service in one of three ways:

#. Manually using a standard web browser. Once connected the
   file upload is very simple, similar to the method used by
   online mail services to upload files as attachments when
   sending mail. This is useful for testing the system, but
   can also be used if a large volume of data needs to be
   submited manually (e.g. sending quasi-definitive data).
#. Automatically using a command line based tool that supports
   file upload. One such tool is CURL |curl| .
   which is available for SUN Solaris, Linux and Windows.
#. Automatically using their own software. File upload to a web
   server is supported by Java and other languages.

The web service will accept data in the following formats:

#. One-second data in IAGA 2002 format.
#. One-minute data in IAGA 2002 format.
#. One-minute data in IMF V1.23 (but this format is not
   recommended for new systems).

Data files may contain a maximum of 24 hours data. 
Smaller ‘fragments’ of data may be sent (an hour, or even a 
few minutes) and are encouraged to allow an observatory to 
send updates more than once a day. In this case, the GIN is
responsible for reassembling the data fragments into a day
file. The smallest ‘fragment’ of
data that should be encoded into an IAGA-2002 file is 2
samples, since some software using this format calculates the
sample rate from time difference between the first pair of
samples in the file. An IMO may not make more than
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
ingest it into the GIN data store. This may take a few seconds
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
#. One-minute data in IMF V1.23 (but this format is not
   recommended for new systems).

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

The email address when sending data to a GIN is:

GIN Email Addresses
```````````````````

-  Ottawa: TODO
-  Paris: TODO
-  Golden: TODO
-  Edinburgh: e_gin@mail.nmh.ac.uk
-  Kyoto: TODO


.. _sub_dat_prel_sat:

Satellite Transmission
----------------------

Satellite transmission is no longer widely used in Intermagnet.
Details of satellite transmission have been retained for
historic purposes and can be found in |app_sat_trans| along
with the data format in |app_imag_imfv_2| and some coding examples 
in |app_sat_cod|.


.. _sub_dat_prel_transfer:

Transferring Data from GINs to WEB Site
---------------------------------------

GINs receive preliminary data from observatories. They forward 
this to the INTERMAGNET web site. Data is transmitted between the
GINs using a variety of technologies (Seedlink, MQTT and Rsync), some
of which may introduce a delay (e.g. Rsync transfers are typically
made every 5 minutes). The GINs and the Intermagnet web site
take care of any format conversions needed so that data is
available to web site users in a number standard formats
such as IAGA-2002 as well as being served through web
services.

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

One simple method the check whether your data has been received
is to look for the data at the INTERMAGNET web site. The delay
time from receipt of data at the GIN to data becoming available
at the web site can be as much as 10 minutes, so you need to
allow time for the data to arrive. If your data does not
arrive, contact the manager of the GIN you have sent data to
and they will investigate where the problem lies.

The Edinburgh GIN provides a ‘handshake’ for incoming data. An
email can be sent from the GIN to the observatory contact at
the start of each day describing the amount of data sent the
previous day (or a longer time back if the observatory is not
sending in near real-time). This allows the observatory to fill
in any gaps dues to transmission problems. For more information
and to set up a handshake, contact the Edinburgh GIN manager.

GINs send statistics describing the amount of data received
from all observatories registered on the GIN. These statistics
are sent out to the observatory email contact once a month,
shortly after the 72 hour period following the end of the month
to which they refer (72 hours after the end of the month, all
data should have been received). They contain summary
information on the completeness of the previous month’s data.

The INTERMAGNET web site keeps data that describes, on a
minute by minute basis, the difference between the current time
and the time stamp of the most recently received data from each
observatory – the observatory’s lag time. These files are
useful for analysing an observatory’s near real-time
performance. The INTERMAGNET web site also holds monthly
lists of data received from observatories. These files are 
available from the "statistics" section of the web site.

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

Another problem with email transmission is modern email
clients use of formatting. GINs require email in plain text.
Email clients often add formatting (such as Rich Text or HTML)
to an email. It if often difficult to detect whether this
formatting has been added. If there is concern that this
problem may be occuring, try to view the email in a "raw"
view, which should show the formatting along with the
email text.

.. _sub_dat_prel_embargoes:

Data Embargoes
--------------

INTERMAGNET understands that some institutes would like to
restrict their data from public use within a defined time
period. Although INTERMAGNET requires institutes to deliver
their data within 72 hours, and more rapidly if possible,
the INTERMAGNET website can enforce an embargo on data, to
prevent it being made available until a set time after recording.

By default, if the institute does not request an embargo, data
will be published once received by INTERMAGNET.

Two embargoes can be requested:

-  **Plotting embargo**

   The INTERMAGNET website offers online plotting utilities.
   |download_plot_data| . A delay (in hours) can be added to prevent the user from
   plotting the data.

-  **Download embargo**

   Data can be download via the website.
   |download_plot_data| . A delay (in hours) can be added to prevent the user from
   downloading the data.

For example, an institute can request that their data be
plotted (image) as soon as received by INTERMAGNET but prevent
the data files from being downloaded until the following day.

To request an embargo, the institute can contact the Edinburgh GIN.
GIN manager contact details are in |app_imag_addr_ginman|.
