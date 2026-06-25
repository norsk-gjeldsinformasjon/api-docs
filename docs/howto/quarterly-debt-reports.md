---
tags:
  - quarterly-reports
---

# Get sent quarterly debt reports regarding own customers

Norsk Gjeldsinformasjon offers a service for sending financial institutions packaged data of their customer base once every fiscal quarter over SFTP.

## Setup for SFTP server

### Prerequisites

- Contact [post@norskgjeld.no](mailto:post@norskgjeld.no) regarding wanting to use this service
- Having a server setup we could connect to using SFTP

### Onboarding

#### 1. Exchange necessary connection details

Send the following to [post@norskgjeld.no](mailto:post@norskgjeld.no):

- IP-address from which the test connection call will be made
- Complete SFTP URL including specific folder for NIN list and packaged data file
- Authentication config: username/password OR PKC key (recommended)

#### 2. NoGi will onboard your configuration

NoGi will verify that our systems can establish contact with your server.

#### 3. Preparing an NIN list

- File name should be your organisation number with `.txt` extension, e.g. `985815534.txt`
- NIN list must be a CSV text file with valid Norwegian NINs, no duplicates
- The NIN list file(s) must be present on the SFTP server **no later than the last day
    of each quarter** (the day before the quarterly processing run).

### Execution

The following steps are executed on the first date of each quarterly fiscal quarter:

1. NoGi retrieves the NIN list from your server
2. If the NIN list has errors, a **Failure report** is sent back
3. If valid, NoGi begins creating a `.gzip` data package
4. A **Progress report** is delivered while the service works
5. When ready, the data package is delivered to your specified SFTP location

## Additional info

### Failure report

File name format: `ReceiverOrgNumber-OnBehalfOfOrgNumber-month-year-failure-report.txt`

Triggers: NIN list not found, wrong file name, invalid organisation number.

### Progress report

File name format: `ReceiverOrgNumber-OnBehalfOfOrgNumber-month-year-progress-report.txt`

Contains: list of invalid NINs, duplicate NINs, receiver organisation number and timestamp.

### Data package file

Filename: `{organisationnumber}.gzip`. Data follows the standard API delivery specification.

## FAQ

### Why are some NINs' loan arrays empty?

If NoGi does not find any debt linked to a specific NIN in the debt registry, an empty array will be returned for that NIN.

### When can we delete the NIN list?

When the job is complete and the data package is present on your SFTP server, it is safe to remove the NIN list.

### When must the NIN list be ready?
The NIN list must be present on the SFTP server **by the last day of each quarter**
(the day before the quarterly run). For example, for the Q2 run on April 1,
the file must be available by March 31. If the file is missing, a failure report
will be generated indicating "NIN list not found."