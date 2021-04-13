# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 12:27:01 2018

@author: yaswanth kumar
"""
import datetime
from contextlib import contextmanager
from psycopg2.pool import SimpleConnectionPool
#import time
try:
    dbConnection = "dbname='postgres' user='postgres' host='localhost' password='root' port = '5432'"
    connectionpool = SimpleConnectionPool(1, 10, dsn=dbConnection)
except StopIteration:
    print(StopIteration)
@contextmanager
def getcursor():
    """get cursor"""
    con = connectionpool.getconn()
    try:
        yield con.cursor()
        con.commit()
    finally:
        connectionpool.putconn(con)
def owner_name1_storage(registration_number, bot_pickup_time, owner_name):
    """insertion of failure records"""
    try:
        query = '''INSERT INTO t_echallan_mp(registration_number,
        bot_pickup_time, owner_name, status, bot_completion_time)
        VALUES(%s, %s, %s, %s, %s);'''
        with getcursor() as cur:
            bot_completion_time = str(datetime.datetime.now())
            status = "Record not found"
            cur.execute(query, (registration_number,
                                bot_pickup_time, owner_name, status, bot_completion_time))
            updated_rows = cur.rowcount
        return updated_rows
    except StopIteration:
        print("Exception during Query execution", StopIteration)

def captcha_failure_record(registration_no, bot_pickup_time):
    '''captcha_failure_record'''
    try:
        query = '''INSERT INTO public.t_echallan(registration_no,
        bot_pickup_time, status, bot_completion_time)
        VALUES(%s, %s, %s, %s);'''
        with getcursor() as cur:
            bot_completion_time = str(datetime.datetime.now())
            status = "captcha not corrected"
            cur.execute(query, (registration_no, bot_pickup_time, status, bot_completion_time))
            updated_rows = cur.rowcount
        return updated_rows
    except StopIteration:
        print("Exception during Query execution", StopIteration)

def failure_record(registration_no, bot_pickup_time):
    """insertion of failure records"""
    try:
        query = '''INSERT INTO public.t_echallan(registration_no,
        bot_pickup_time, status, bot_completion_time)
        VALUES(%s, %s, %s, %s);'''
        with getcursor() as cur:
            bot_completion_time = str(datetime.datetime.now())
            status = "Record not found"
            cur.execute(query, (registration_no, bot_pickup_time, status, bot_completion_time))
            updated_rows = cur.rowcount
        return updated_rows
    except StopIteration:
        print("Exception during Query execution", StopIteration)
def insert_record1(registration_no, bot_pickup_time, challanNumber, voilation_reasonDate, offenceplace_of_offence, ownerName, drivingLicenceNumber, challan_paid_Status, fineAmmount):
    """insertion of records"""
    try:
        status = "Completed"
        query = '''INSERT INTO public.t_echallan(registration_no, bot_pickup_time,
        challanNumber, voilation_reasonDate, offenceplace_of_offence, ownerName, drivingLicenceNumber,
        challan_paid_Status, fineAmmount, status, bot_completion_time)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        with getcursor() as cur:
            bot_completion_time = str(datetime.datetime.now())
            cur.execute(query, (registration_no, bot_pickup_time, challanNumber, voilation_reasonDate, offenceplace_of_offence, ownerName, drivingLicenceNumber, challan_paid_Status, fineAmmount, status, bot_completion_time))
            updated_rows = cur.rowcount
        return updated_rows
    except StopIteration:
        print("Exception during Query execution", StopIteration)
        
def insert_record(registration_no, bot_pickup_time, offence_date, challan_notice_number, challan_transaction_ammount, place_of_offence, voilation_reason):
    """insertion of records"""
    try:
        status = "Completed"
        query = '''INSERT INTO public.t_echallan(registration_no, bot_pickup_time,
        offence_date, challan_notice_number, challan_transaction_ammount, place_of_offence, voilation_reason, status, bot_completion_time)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        with getcursor() as cur:
            bot_completion_time = str(datetime.datetime.now())
            cur.execute(query, (registration_no, bot_pickup_time, offence_date, challan_notice_number, challan_transaction_ammount, place_of_offence, voilation_reason, status, bot_completion_time))
            updated_rows = cur.rowcount
        return updated_rows
    except StopIteration:
        print("Exception during Query execution", StopIteration)        


def fetchrecords2():
    """fetching Records"""
    try:
        query = "select registration_number from public.regostration_number"
        with getcursor() as cur:
            cur.execute(query)
            result_set = cur.fetchall()
        return result_set
    except StopIteration:
        print("Exception during Query execution", StopIteration)
def request_approved(proposal_no):
    """request Aprroved"""
    try:
        query = '''update digit_bots.t_vespa_break_in_temp set status = %s,
        data_updation_time = %s WHERE proposal_no  = %s '''
        with getcursor() as cur:
            bot_completion_time = str(datetime.datetime.now())
            cur.execute(query, ('Approved', bot_completion_time, proposal_no))
            updated_rows = cur.rowcount
        print('Request Completed')
        return updated_rows
    except RuntimeError:
        print("Exception during Query execution")
def update_ticket(proposal_no, ticket):
    """updation of ticket"""
    try:
        query = '''update digit_bots.t_vespa_break_in_temp set ticket_no = %s,
        status = %s, data_updation_time = %s WHERE proposal_no  = %s and status = %s'''
        with getcursor() as cur:
            bot_completion_time = str(datetime.datetime.now())
            cur.execute(query, (ticket,
                                'Ticket Created', bot_completion_time, proposal_no, "Approved"))
            updated_rows = cur.rowcount
        print('ticket Completed')
        return updated_rows
    except RuntimeError:
        print("Exception during Query execution")
def fetchrecords():
    """fetching the records"""
    try:
        query = '''select * from public.t_parivahan where registration_no like 'GJ%'
        and (status = '' or status is null or status = 'bot in process')  order by random() limit 1'''
        with getcursor() as cur:
            cur.execute(query)
            result_set = cur.fetchall()
        return result_set
    except StopIteration:
        print("Exception during Query execution", StopIteration)
def update(sr_id):
    """updating records"""
    try:
        bot_pickup_time1 = str(datetime.datetime.now())
        query = '''UPDATE public.regostration_number SET bot_pickup_time = %s,
        status = %s , sr_id = %s where  sr_id = %s'''
        #bot_pickup_time = str(datetime.datetime.now())
        with getcursor() as cur:
            bot_pickup_time1 = str(datetime.datetime.now())
            status = 'bot in process'
            cur.execute(query, (bot_pickup_time1, status, sr_id))
            updated_rows = cur.rowcount
        return updated_rows
    except RuntimeError:
        print("Exception during Query execution")
def update2(sr_id):
    """updateing the completion time"""
    try:
        #bot_completion_time = str(datetime.datetime.now())
        query = '''UPDATE public.t_parivahan SET bot_completion_time = %s,
        status = %s  where  registration_no = %s'''
        #bot_pickup_time = str(datetime.datetime.now())
        with getcursor() as cur:
            bot_completion_time = str(datetime.datetime.now())
            status = 'completed'
            cur.execute(query, (bot_completion_time, status, sr_id))
            updated_rows = cur.rowcount
        return updated_rows
    except RuntimeError:
        print("Exception during Query execution")
def update1(sr_id):
    """updateing the pick up time"""
    try:
        #bot_pickup_time1 = str(datetime.datetime.now())
        query = '''UPDATE public.t_parivahan SET bot_pickup_time = %s,
        status = %s  where  registration_no = %s'''
        #bot_pickup_time = str(datetime.datetime.now())
        with getcursor() as cur:
            bot_pickup_time = str(datetime.datetime.now())
            status = 'bot in process'
            cur.execute(query, (bot_pickup_time, status, sr_id))
            updated_rows = cur.rowcount
        return updated_rows
    except RuntimeError:
        print("Exception during Query execution")
