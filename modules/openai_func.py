import requests
import logging
from modules.presets import (
    timeout_all,
    USAGE_API_URL,
    BALANCE_API_URL,
    standard_error_msg,
    connection_timeout_prompt,
    error_retrieve_prompt,
    read_timeout_prompt
)

from . import shared
from modules.config import retrieve_proxy
import os, datetime

def get_billing_data(openai_api_key, billing_url):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    
    timeout = timeout_all
    with retrieve_proxy():
        response = requests.get(
            billing_url,
            headers=headers,
            timeout=timeout,
        )
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
    

def get_usage(openai_api_key):
    return ""

def get_last_day_of_month(any_day):
    # The day 28 exists in every month. 4 days later, it's always next month
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtracting the number of the current day brings us back one month
    return next_month - datetime.timedelta(days=next_month.day)