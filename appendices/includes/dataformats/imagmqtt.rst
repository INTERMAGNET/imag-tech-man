.. _app_imag_mqtt:

Intermagnet MQTT format
-----------------------

This section describes how to format topics and payloads when
sending data over MQTT.


.. _app_imag_mqtt_topic:

Intermagnet MQTT topics
```````````````````````

Topics in MQTT are strings used to identify and route messages. Topics allow
publishers to identify messages and subscribers to choose which types of message
to receive. Topics for the Intermagnet MQTT service have been designed to allow
the contents of the message to be easily identified. Observatories publishing data 
through the Intermagnet MQTT service must use the topic::

    impf/<iaga-code>/<cadence>/<publication-level>/<elements-recorded>

Where:

- "impf" stands for Intermagnet MQTT Payload Format and is included in the topic
  to allow alternative topic and payload formats to be used on the same MQTT
  brokers in the future.
- "iaga-code" is the IAGA registered code of the observatory sending data.
- "cadence" is the sample period for the data as an ISO8601 duration (for data
  with sampling rate of 1Hz or below) or the sample rate with the suffix "hz" (for
  data with sampling rate of 1Hz or above). Valid cadences are:

  - "pt1s" or "1hz" for 1-second data.
  - "pt1m" for 1-minute data.
- "publication-level" is a number indicating the level of processing applied to the data:

  - 1 = The data is unprocessed and as recorded at the observatory with no changes made.
  - 2 = Some edits have been made such as gap filling and spike removal and a preliminary baseline added.
  - 3 = The data is at the level required for production of an initial bulletin or for quasi-definitive publication.
  - 4 = The data has been finalised and no further changes are intended.

- "elements-recorded" lists the geomagnetic elements that will be in the message. All 4 elements must
  be specified, even if the payload includes fewer elements. "elements-recorded" must be one of:

  - "XYZS" - XYZ vector orientation with an independent Scalar F
  - "HDZS" - HDZ vector orientation with an independent Scalar F
  - "DIFS" - DIF vector orientation with an independent Scalar F

Note that topics are case-sensitive. All topic values for the Intermagnet MQTT service
must be in lower case.

### Examples ###

The topic for Eskdalemuir observatory's 1-minute "reported" HDZ data (straight from the observatory with no processing)
would be::

    impf/esk/pt1m/1/hdzs

The topic for Lerwick observatory's 1-second quasi-definitive XYZS data would be either of the following::

    impf/ler/pt1s/3/xyzs
    impf/ler/1hz/3/xyzs


.. _app_imag_mqtt_payload:

Intermagnet MQTT payload format
```````````````````````````````

Intermagnet MQTT messages are formatted in JSON. A [JSON schema](ImagMQTTSchema.json)
describes the valid contents of an MQTT message. Messages must consist
of JSON documents conforming to the schema and no other content.

The JSON schema consists of three sections:

1. Mandatory metadata
2. Mandatory geomagnetic field data
3. Optional extra metadata

The mandatory metadata consists of a single field which must be present in every
JSON data message:

1. "startDate": The date and time of the first data sample, in ISO8601 format. The
   string is truncated to the appropriate precision for the data cadence (ie. all
   fields except milli-seconds for 1-second data, all fields except seconds and
   milli-seconds for 1-minute data).

The topic used to publish data to the MQTT broker includes 4 further pieces of metadata
(IAGA code, cadence, publication level and geomagnetic orientation) that are also used 
to describe the data being transmitted.

The mandatory geomagnetic field data consists of anything between 1 and 4 arrays 
corresponding to the elements recorded (as described in the topic). Individual elements of the geomagnetic 
field may be sent together in a message or in separate messages, so that, for 
example, data from a vector instrument and a separate scalar instrument do not 
need to be combined into a single message to be sent. An entirely missing scalar 
element does not need to be sent at all. The arrays sent in a single message must 
all be the same length and contain only numbers or the value "null", which is used
to indicate a missing sample. Valid arrays are:

- "geomagneticFieldX": Magnetic field vector strength in nT, x component, geographic coordinates.
- "geomagneticFieldY": Magnetic field vector strength in nT, y component, geographic coordinates.
- "geomagneticFieldZ": Magnetic field vector strength in nT, z component, geographic coordinates.
- "geomagneticFieldH": Magnetic field vector strength in nT, in the horizontal plane along the magnetic meridian.
- "geomagneticFieldD": Angle between the magnetic vector and true north, in minutes of arc, positive east.
- "geomagneticFieldI": Angle between the magnetic vector and the horizontal, in minutes of arc, positive below the horizontal.
- "geomagneticFieldF": Geomagnetic field strength in nT, calculated from and consistent with XYZ or HDZ field elements.
- "geomagneticFieldS": Geomagnetic field strength in nT, measured by an independent scalar instrument.

Only arrays corresponding with the "elements-recorded" in the message topic may be used.

The optional extra metadata may be completely missing, or any part of parts may be included.
The purpose of this metadata is to allow the data provider to supply metadata values that the Intermagnet
data portal will use when creating IMF, IAGA-2002 and ImagCDF data files for users. The data portal
stores a metadata file for each day and publication level of data. Thus it is only neccessary
for a data provider to send one message per day / publication level, containing the optional metadata that
they require to be distributed with their data. Subsquent messages for the same day / publication level
do not require any optional metadata. If data provider's follow this advice, it is best
to provide the optional metadata along with the first data of the day, to ensure that data and
metadata are always consistent.

If the optional metadata is not supplied, default values will be used by the portal (from static
metadata that the Edinburgh GIN holds)).

The following optional metadata fields are available - the names in brackets after each of the
fields describes which data distribution format(s) the metadata field is used in:

- "ginCode": (IMF)
- "decbas": (IMF)
- "latitude": (IMF, IAGA-2002, ImagCDF)
- "longitude": (IMF, IAGA-2002, ImagCDF)
- "elevation": (IAGA-2002, ImagCDF)
- "institute": (IAGA-2002, ImagCDF - called "Source of data" in IAGA-2002)
- "name": (IAGA-2002, ImagCDF - called "ObservatoryName" in ImagCDF)
- "sensorOrientation": (IAGA-2002, ImagCDF - called "VectorSensOrient in CDF)
- "digitalSampling": (IAGA-2002)
- "dataIntervalType": (IAGA-2002)
- "publicationDate": (IAGA-2002, ImagCDF)
- "standardLevel": (ImagCDF)
- "standardName": (ImagCDF)
- "standardVersion": (ImagCDF)
- "partialStandDesc": (ImagCDF)
- "source": (ImagCDF)
- "termsOfUse": (ImagCDF)
- "uniqueIdentifier": (ImagCDF)
- "parentIdentifiers": (ImagCDF)
- "referenceLinks": (ImagCDF)
- "comments": (IAGA-2002)

For details of each of these fields, see the [JSON schema](ImagMQTTSchema.json).

Data sets created for this schema can be checked at the JSON Schema verfier:
https://json-schema.hyperjump.io/. Reference material for JSON Schema is here:
https://json-schema.org/learn/getting-started-step-by-step. The Schema for 
Intermagnet MQTT JSON is [here](ImagMQTTSchema.json).


.. _app_imag_mqtt_example:

Example IMPF data
`````````````````

The first example is a minimum viable data file for 1-minute data. Three  
3-component samples are presented along with mandatory metadata::

    {
        "startDate": "2023-01-01T00:00",
        "geomagneticFieldX": [ 17595.02, null, 17594.99 ],
        "geomagneticFieldY": [ -329.19, -329.18, -329.21 ],
        "geomagneticFieldZ": [ 46702.70, 46703.01, 46703.24 ]
    }


An expanded example shows how to add "comment" metadata, to set the "comments" 
section that will be included with the data when it is distributed from the
Intermagnet web site in IAGA-2002 format. This example also 
shows how the startDate should be modified for 1-second data::

    {
        "startDate": "2023-01-01T00:00:00",
        "comments": [ "This data file was created using INTERMAGNET data",
                      "from the Edinburgh GIN. These data were acquired",
                      "from an INTERMAGNET quasi-def data file.",
                      "Final data will be available on the INTERMAGNET DVD",
                      "Go to www.intermagnet.org for details on obtaining this product.",
                      "CONDITIONS OF USE: The conditions of use for data provided",
                      "through INTERMAGNET and acknowledgement templates can be found",
                      "at www.intermagnet.org" ],
        "geomagneticFieldS": [ 49000.00, 49000.21, 49000.34 ]
    }

JSON Schema
```````````

The following schema can be used to verify that a JSON document conforms to the
IMPF specification::

    {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        
        "$id": "https://intermagnet.org/mqtt_exchange.schema.json",
        "title": "Intermagnet MQTT Exchange Format",
        "description": "A format for exchanging geomagnetic data in Intermagnet using MQTT",
        "type": "object",
    
        "properties": {
            "startDate": {
                "type": "string",
                "format": "datetime",
                "description": "Date and time of the first data sample, in ISO8601 format, to appropriate precision for the data cadence" 
            },
        
            "ginCode": {
                "type": "string",
                "enum": [ "edi", "gol", "kyo", "ott", "par" ],
                "description": "Optional: Code for the GIN that this observatory reports to" 
            },
            "decbas": {
                "type": "integer",
                "minimum": -10800,
                "maximum": 21600,
                "description": "Optional: DECBAS (declination baseline) field from IMF format" 
            },
            "latitude": {
                "type": "number",
                "minimum": -90.0,
                "maximum": 90.0,
                "description": "Optional: Observatory location: latitude" 
            },
            "longitude": {
                "type": "number",
                "minimum": -180.0,
                "maximum": 360.0,
                "description": "Optional: Observatory location: east longitude"
            },
            "elevation": {
                "type": "number",
                "minimum": -10000.0,
                "maximum": 10000.0,
                "description": "Optional: Observatory location: elevation in metres"
            },
            "institute": {
                "type": "string",
                "description": "Optional: Institute that the observatory belongs to"
            },
            "name": {
                "type": "string",
                "description": "Optional: Name of the observatory"
            },
            "sensorOrientation": {
                "type": "string",
                "description": "Optional: Orientation of the vector magnetic field sensor"
            },
            "digitalSampling": {
                "type": "string",
                "description": "Optional: Rate (in seconds) of the data sampling of the vector magnetic field sensor"
            },
            "dataIntervalType": {
                "type": "string",
                "description": "Optional: Mean or instantaneous time interval of the data"
            },
            "publicationDate": {
                "type": "string",
                "format": "date",
                "description": "Optional: Date of publication of the data, in ISO8601 format, date only (no time)" 
            },
            "standardLevel": {
                "type": "string",
                "enum": [ "None", "Partial", "Full" ],
                "description": "Optional: Describe whether the data conforms to a standard"
            },
            "standardName": {
                "type": "string",
                "enum": [ "INTERMAGNET_1-Second", "INTERMAGNET_1-Minute", "INTERMAGNET_1-Minute_QD" ],
                "description": "Optional: The name of the standard this data conforms to (if any)" 
            },
            "standardVersion": {
                "type": "string",
                "description": "Optional: The version of the standard this data conforms to (if any)" 
            },
            "partialStandDesc": {
                "type": "string",
                "description": "Optional: A comma separated list describing the parts of the standard this data conforms to (if any), for use when the standard level is partial" 
            },
            "source": {
                "type": "string",
                "enum": [ "Institute", "Intermagnet", "WDC" ],
                "description": "Optional: Where the data came from" 
            },
            "termsOfUse": {
                "type": "string",
                "description": "Optional: The terms of use for the data" 
            },
            "uniqueIdentifier": {
                "type": "string",
                "description": "Optional: A string that can be used to uniquely identify this data, e.g. a DOI" 
            },
            "parentIdentifiers": {
                "type": "array",
                "items": { "type": "string" },
                "description": "Optional: The unique identifer(s) of the parent data set" 
            },
            "referenceLinks": {
                "type": "array",
                "items": { "type": "string" },
                "description": "Optional: URLs pointing to information about the data, one URL per element" 
            },
            "comments": {
                "type": "array",
                "items": { "type": "string" },
                "description": "Optional: Use these to record important information not contained in the defined fields" 
            },
        
            "geomagneticFieldX": {
                "type": "array",
                "items": { "type": ["number", "null"] },
                "minimum": -99999.0,
                "maximum": 99999.0,
                "description": "Magnetic field vector strength in nT, x component, geographic coordinates" 
            },
            "geomagneticFieldY": {
                "type": "array",
                "items": { "type": ["number", "null"] },
                "minimum": -99999.0,
                "maximum": 99999.0,
                "description": "Magnetic field vector strength in nT, y component, geographic coordinates" 
            },
            "geomagneticFieldZ": {
                "type": "array",
                "items": { "type": ["number", "null"] },
                "minimum": -99999.0,
                "maximum": 99999.0,
                "description": "Magnetic field vector strength in nT, z component, geographic coordinates" 
            },
            "geomagneticFieldH": {
                "type": "array",
                "items": { "type": ["number", "null"] },
                "minimum": -99999.0,
                "maximum": 99999.0,
                "description": "Magnetic field vector strength in nT, in the horizontal plane along the magnetic meridian" 
            },
            "geomagneticFieldD": {
                "type": "array",
                "items": { "type": ["number", "null"] },
                "minimum": -180.0,
                "maximum": 99999.0,
                "description": "Angle between the magnetic vector and true north, in degrees of arc, positive east" 
            },
            "geomagneticFieldI": {
                "type": "array",
                "items": { "type": ["number", "null"] },
                "minimum": -180.0,
                "maximum": 99999.0,
                "description": "Angle between the magnetic vector and the horizontal, in degrees of arc, positive below the horizontal" 
            },
            "geomagneticFieldF": {
                "type": "array",
                "items": { "type": ["number", "null"] },
                "minimum": 0.0,
                "maximum": 99999.0,
                "description": "Geomagnetic field strength in nT, calculated from and consistent with XYZ or HDZ field elements" 
            },
            "geomagneticFieldS": {
                "type": "array",
                "items": { "type": ["number", "null"] },
                "minimum": 0.0,
                "maximum": 99999.0,
                "description": "Geomagnetic field strength in nT, measured by an independent scalar instrument" 
            }
        },
        
        "allOf": [
            { "required": [ "startDate" ] },
            { "oneOf": 
                [
                    { "allOf": [ { "required": [ "geomagneticFieldX", "geomagneticFieldY", "geomagneticFieldZ", "geomagneticFieldS" ] },
                                { "not": { "required": [ "geomagneticFieldH" ] } },
                                { "not": { "required": [ "geomagneticFieldD" ] } },
                                { "not": { "required": [ "geomagneticFieldI" ] } }
                    ] },
                    { "allOf": [ { "required": [ "geomagneticFieldX", "geomagneticFieldY", "geomagneticFieldZ" ] },
                                { "not": { "required": [ "geomagneticFieldH" ] } },
                                { "not": { "required": [ "geomagneticFieldD" ] } },
                                { "not": { "required": [ "geomagneticFieldI" ] } },
                                { "not": { "required": [ "geomagneticFieldS" ] } }
                    ] },
                    { "allOf": [ { "required": [ "geomagneticFieldH", "geomagneticFieldD", "geomagneticFieldZ", "geomagneticFieldS" ] },
                                { "not": { "required": [ "geomagneticFieldX" ] } },
                                { "not": { "required": [ "geomagneticFieldY" ] } },
                                { "not": { "required": [ "geomagneticFieldI" ] } }
                    ] },
                    { "allOf": [ { "required": [ "geomagneticFieldH", "geomagneticFieldD", "geomagneticFieldZ" ] },
                                { "not": { "required": [ "geomagneticFieldX" ] } },
                                { "not": { "required": [ "geomagneticFieldY" ] } },
                                { "not": { "required": [ "geomagneticFieldI" ] } },
                                { "not": { "required": [ "geomagneticFieldS" ] } }
                    ] },
                    { "allOf": [ { "required": [ "geomagneticFieldD", "geomagneticFieldI", "geomagneticFieldF", "geomagneticFieldS" ] },
                                { "not": { "required": [ "geomagneticFieldX" ] } },
                                { "not": { "required": [ "geomagneticFieldY" ] } },
                                { "not": { "required": [ "geomagneticFieldH" ] } }
                    ] },
                    { "allOf": [ { "required": [ "geomagneticFieldD", "geomagneticFieldI", "geomagneticFieldF" ] },
                                { "not": { "required": [ "geomagneticFieldX" ] } },
                                { "not": { "required": [ "geomagneticFieldY" ] } },
                                { "not": { "required": [ "geomagneticFieldH" ] } },
                                { "not": { "required": [ "geomagneticFieldS" ] } }
                    ] },
                    { "allOf": [ { "required": [ "geomagneticFieldS" ] },
                                { "not": { "required": [ "geomagneticFieldX" ] } },
                                { "not": { "required": [ "geomagneticFieldY" ] } },
                                { "not": { "required": [ "geomagneticFieldZ" ] } },
                                { "not": { "required": [ "geomagneticFieldH" ] } },
                                { "not": { "required": [ "geomagneticFieldD" ] } },
                                { "not": { "required": [ "geomagneticFieldI" ] } }
                    ] }
                ]
            }
        ],
        "additionalProperties": false
    }
  
