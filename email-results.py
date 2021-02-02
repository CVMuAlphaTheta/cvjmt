#!/usr/bin/env python3

'''Email CVJMT results to participants.'''

import csv
import ssl, smtplib, email
import argparse, getpass

parser = argparse.ArgumentParser(description='Email CVJMT results.')
parser.add_argument('results_file', help='path of the CSV file containing the results')
args = parser.parse_args()

from_email = input('Email: ')
password = getpass.getpass('Password: ')

with open(args.results_file) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        msg = email.message.EmailMessage()
        msg['Subject'] = f'CVJMT Results For {row["first_name"]} {row["last_name"]}'
        msg.set_content(
            f'foo'
        )
