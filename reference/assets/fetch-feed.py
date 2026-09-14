#!/usr/bin/env python

# Demo implemetation of reading consent events from Norsk Gjeldsinformasjon preprod
# This script will read events for a given client id and keep track of state in the file 'fetch-feed-seqnr.txt'
#
# Running the script requires setting your client id and secret as environment variables to authenticate against the api.
# You can do this in a script like so:
#
# #!/bin/bash
# export NOGI_CLIENT_ID='YOUR CLIENT ID HERE'
# export NOGI_CIENT_SECRET='YOU CLIENT SECRET HERE'
# ./fetch-feed.py
#
# The script will keep track of the latest sequence number read in a file 'fetch-feed-seqnr.txt' in the working directory when running the script.
# This is used to only need new events since our last request.
#
# Tip: You can use jq (https://jqlang.github.io/jq/) to format the json output of this script better

import base64
import json
import os.path
import urllib.error
import urllib.parse
import urllib.request
import uuid

# Environment/config variables for script

access_token_url = os.environ.get("NOGI_ACCESS_TOKEN_URL") or 'https://access-preprod.norskgjeld.no/oauth2/token'
fetch_feed_url = os.environ.get("NOGI_FETCH_FEED_URL") or 'https://api-preprod.norskgjeld.no/feed/v1/consent'

scope = 'client.access.consent.events'

# File to store the latest seen sequence number
local_latest_seqnr_file = 'fetch-feed-seqnr.txt'

client_id = os.environ.get("NOGI_CLIENT_ID")
if client_id is None:
    raise Exception("NOGI_CLIENT_ID environment variable must be set")

client_secret = os.environ.get("NOGI_CLIENT_SECRET")
if client_secret is None:
    raise Exception("NOGI_CLIENT_SECRET environment variable must be set")


# utility functions for making requests

def fetch_access_token(scope, audience):
    access_token_req_data = {
        'scope': scope,
        'grant_type': 'client_credentials',
        'audience': audience,
    }

    req_data = urllib.parse.urlencode(access_token_req_data, doseq=True).encode(
            'utf-8')

    auth_header = base64.b64encode(
            f'{client_id}:{client_secret}'.encode()).decode()

    access_token_request = urllib.request.Request(
            access_token_url,
            method='POST',
            data=req_data,
            headers={
                'Authorization': f'Basic {auth_header}'
            }
    )

    try:
        with urllib.request.urlopen(access_token_request) as response:
            auth_response = json.loads(response.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"""
Received error while fetching access token for client '{client_id}', with secret '{client_secret}'
with parameters:
{access_token_req_data}
status code: {e.code}
Error description:
{error_body}
        """)
        exit(1)

    return auth_response['access_token']


def send_json_request(url, data, method, access_token):
    auth_header = f'Bearer {access_token}'

    request = urllib.request.Request(
            url,
            method=method,
            data=json.dumps(data).encode('utf-8') if data is not None else None,
            headers={
                'Authorization': auth_header,
                'Content-Type': 'application/json'
            }
    )

    try:
        with urllib.request.urlopen(request) as response:
            response_data = json.loads(response.read())

            return response_data
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"""
Received error
status code: {e.code}
Error description:
{error_body}
        """)
        exit(1)


def read_local_seqnr():
    if os.path.exists(local_latest_seqnr_file):
        f = open(local_latest_seqnr_file, "r")
        seqnr = int(f.read())
        f.close()
        return seqnr
    else:
        return 1

def store_local_seqnr(seqnr):
    f = open(local_latest_seqnr_file, "w")
    f.write(str(seqnr))
    f.close()



##
# Demo implementation of reading events
##

# Fetch access token to create consent
access_token = fetch_access_token(
        scope='client.access.consent.events',
        audience='https://api-preprod.norskgjeld.no/feed/v1/consent')


# read the last sequence number we have seen last run of the program
local_latest_seqnr = read_local_seqnr()

# we can ask for the first available sequence number, this is optional,
# as passing '1' will start fetching from the beginning of available events
first_seqnr_response = send_json_request(
        url=f"{fetch_feed_url}/firstSequenceNr",
        data=None,
        method='GET',
        access_token=access_token
)

# print for demo purposes
print(f"""
{json.dumps(first_seqnr_response)}
""")

# ask for the latest sequence number
last_seqnr_response = send_json_request(
        url=f"{fetch_feed_url}/lastSequenceNr",
        data=None,
        method='GET',
        access_token=access_token
)

last_available_seqnr = last_seqnr_response['lastSequenceNr']

# print for demo purposes
print(f"""
{json.dumps(last_seqnr_response)}
""")


# if last_available_seqnr is greater than the latest we've read then we should read more events
if last_available_seqnr > local_latest_seqnr:
    # read all events since the last event we've seen, up to 500
    feed_data = send_json_request(
            url=f"{fetch_feed_url}?fromSequenceNr={local_latest_seqnr + 1}&limit=500",
            data=None,
            method='GET',
            access_token=access_token
    )

    # print for demo purposes
    print(f"""
    {json.dumps(feed_data)}
    """)

    events = feed_data['result']

    last_seen_seqnr = feed_data['endSequenceNr']

    # store last sequence number
    store_local_seqnr(last_seen_seqnr)

    # do something with events here, store in a db, process, etc...
