import config
import datetime


def save_user(username, password):
    cursor = config.get_connection().cursor()
    cursor.execute("""
        INSERT INTO swuser (username, password)
        VALUES (%s, %s); """, (username, password))


def get_userdata(username):
    cursor = config.get_connection().cursor()
    cursor.execute("""
        SELECT username, password
        FROM swuser
        WHERE username = %s; """, (username, ))
    return cursor.fetchall()


def get_user_id(username):
    cursor = config.get_connection().cursor()
    cursor.execute("""
        SELECT id
        FROM swuser
        WHERE username = %s; """, (username, ))
    return cursor.fetchall()


def insert_vote(planet_id, user_id, planet_name):
    cursor = config.get_connection().cursor()
    date_time = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    cursor.execute("""
        INSERT INTO planet_votes (planet_id, user_id, submission_time, planet_name)
        VALUES (%s, %s, %s, %s); """, (planet_id, user_id, date_time, planet_name))


def get_vote_statistics():
    cursor = config.get_connection().cursor()
    cursor.execute("""
        SELECT planet_name, COUNT(planet_name)
        FROM planet_votes
        GROUP BY planet_name
        ORDER BY COUNT(planet_name)
        ;""")
    return cursor.fetchall()
