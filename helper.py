from flask import request
import pandas as pd
import os

def check_language(content_type, lang):
    '''
    Function to check language and choose correct table in database
    Args: content_type = str; the content that should be queried from the databases
          lang = str; language
    Returns: df_row = contains results from sql query
    '''

    # connect to database
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    # select everything from the titles database
    if lang == 'de':
        if content_type == 'title':
            cur.execute("SELECT content FROM titles")
            db_row = cur.fetchall()
            # close database connection
            conn.close()
        elif content_type == 'portfolio':
            cur.execute("SELECT * FROM portfolio")
            db_row = cur.fetchall()
            # close database connection
            conn.close()
        elif content_type == 'skills':
            cur.execute("SELECT * FROM skills")
            db_row = cur.fetchall()
            # close database connection
            conn.close()

    elif lang == 'en':
        if content_type == 'title':
            cur.execute("SELECT content FROM titles_en")
            db_row = cur.fetchall()
            # close database connection
            conn.close()
        elif content_type == 'portfolio':
            cur.execute("SELECT * FROM portfolio_en")
            db_row = cur.fetchall()
            # close database connection
            conn.close()
        elif content_type == 'skills':
            cur.execute("SELECT * FROM skills_en")
            db_row = cur.fetchall()
            # close database connection
            conn.close()

    return db_row


def get_title_content(page):
    '''
    Function to get the relevant content for the html page
    Args: page = str; name of the html page
    Returns: title_text = str; content for the html page
    '''

    # assign content to variable
    if page == 'index':
        title_text = '''
        Hi, my name is Nathan.

        I'm a data scientist, musician, dancer, and amatuer crocheter.

        I worked as a firmware designer for a musical instrument design company, 
        and later as a photovoltaic systems researcher in the renewable energy industry 
        before taking an educational sabbatical to pivot to the healthcare industry.
        
        Please scroll down to find out a little bit more about my experience and what skills I can bring to the table.
        '''
    elif page == 'portfolio':
        title_text = 'portfolio'
    elif page == 'about':
        title_text = 'about'

    return title_text


def get_portfolio_content():
    '''
    Function to get the portfolio projects from the database
    Args: lang = str; specifies language selected by user
    Returns: projects = list; list of dictionaries containing project metadata.
    '''

    projects_db = pd.read_csv('projects_db.csv', header=0)
    projects_db['date'] = pd.to_datetime(projects_db['date']).dt.date
    projects_db = projects_db.sort_values(by='date', ascending=False) # latest first
    projects = projects_db.to_dict(orient='records')
    return projects 
    

def get_skill_content(lang):
    '''
    Function to get the skills from the database
    Args: lang = str; specifies language selected by user
    Returns: skill_list
    '''

    db_row = check_language('skills', lang)

    # instantiate a dict to save all projects in
    skill_dict = {}

    # iterate through all the skills in the database
    for skill in db_row:
        if skill[1] in skill_dict.keys():
            skill_dict[skill[1]].append(list(skill[2:5]))
        else:
            skill_dict[skill[1]] = [list(skill[2:5])]

    return skill_dict

def get_privacy_legal_notice():
    '''
    Function to get variables necessary for privacy and legal notice pages
    Args: None
    Returns: address_one, address_two, email = str
    '''

    try:
        import config
        address_one = config.address_one
        address_two = config.address_two
        email = config.email

    except:
        address_one = os.environ['ADDRESS_ONE']
        address_two = os.environ['ADDRESS_TWO']
        email = os.environ['EMAIL']

    return address_one, address_two, email
