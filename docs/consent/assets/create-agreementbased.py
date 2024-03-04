#!/usr/bin/env python

import base64
import json
import urllib.error
import urllib.parse
import urllib.request
import uuid

access_token_url = 'https://access-preprod.norskgjeld.no/oauth2/token'
create_consent_url = 'https://api-preprod.norskgjeld.no/v1/consent/agreement'

client_id = '<your-client-id>'
client_secret = '<your-client-secret>'
nin = '14842249091'
ex_consent_id = uuid.uuid4()

scope_of_consent = 'debt.unsecured.presentation'
consent_duration_days = '100'


def format_headers(headers):
    return "\n".join([f"{name}: {value}" for (name, value) in headers.items()])


def format_request(request):
    return f"""{request.method} {request.full_url}
{format_headers(request.headers)}

{request.data.decode('utf-8') if request.data else ""}"""


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

    print(f"""
Sending request:
{format_request(access_token_request)}
    """)

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

    print(f"""
Sending request:
{format_request(request)}
    """)

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


# Fetch access token to create consent

access_token = fetch_access_token(
        scope='consent.create',
        audience='https://api-preprod.norskgjeld.no/v1/consent/agreement')

# Create consent

create_consent_req_data = {
    'nin': nin,
    'scope_of_consent': scope_of_consent,
    'consent_duration_days': consent_duration_days,
    'our_consent_id': str(ex_consent_id),
}

created_consent = send_json_request(
        url=create_consent_url,
        data=create_consent_req_data,
        method='PUT',
        access_token=access_token)

print(f"""
Created consent:
{created_consent}
""")

# Fetch access token to fetch debt

access_token = fetch_access_token(
        scope='debt.unsecured.presentation',
        audience='https://api-preprod.norskgjeld.no/v1/debt')

# Fetch debt using newly created consent

created_consent_id = created_consent['consent']['id']

get_debt_response = send_json_request(
        url=f'https://api-preprod.norskgjeld.no/v1/debt/{created_consent_id}',
        data=None,
        method='GET',
        access_token=access_token
)

print(f"""
Fetched debt using consent:
{get_debt_response}
""")
