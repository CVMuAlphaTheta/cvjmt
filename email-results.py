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

context = ssl.create_default_context()

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls(context=context)
    server.login(from_email, password)
    with open(args.results_file) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            msg = email.message.EmailMessage()
            msg['Subject'] = f'CVJMT Results For {row["first_name"]} {row["last_name"]}'
            msg['From'] = from_email
            msg['To'] = row['email']
            body = (
                f'First name: {row["first_name"]}\n'
                f'Last name: {row["last_name"]}\n'
                f'School: {row["school"]}\n'
                f'Grade: {row["grade"]}\n'
                f'Division: {"Middle School" if row["division"] == "" else row["division"]}\n\n'
                f'Points for each problem:\n'
            )
            for i in range(1, 26):
                body += f'Problem {i}: {row[str(i)]}\n'
            body += (
                f'Score: {row["score"]}\n\n'
                f'The answer keys and solutions are available on our website at https://cvhsmath.weebly.com/cvjmt.html. '
                f'If we made any mistakes, please email us by Friday, February 12th. '
                f'We will announce the winners after this date. '
                f'Thank you for participating!\n\n'
                f'(This is an automated message.)'
            )
            msg.set_content(body)
            server.send_message(msg)
