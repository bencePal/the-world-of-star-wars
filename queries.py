import config


def save_user(username, password):
    cursor = config.get_connection().cursor()
    cursor.execute("""
        INSERT INTO swuser (username, password)
        VALUES (%s, %s); """, (username, password))
    # cursor.close() ???


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













    # rows = list(cursor.fetchall())
    # print(rows)
    # cursor.close()


# def nickname_miskolc_mentors(cursor):
#     cursor.execute("""
#         SELECT nick_name FROM mentors
#         WHERE city = 'Miskolc'
#         ;""")
#     return common.print_query_table(cursor, "")
# def firstname_lastname_mentors():
#     cursor = config.connection().cursor()
#     cursor.execute("""SELECT first_name, last_name FROM mentors;""")
#     return ui.print_query_table(cursor, "")

# def carol_and_her_hat(cursor):
#     cursor.execute("""
#         SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
#         WHERE first_name = 'Carol'
#         ;""")
#     return common.print_query_table(cursor, "")


# def another_girl_hat(cursor):
#     cursor.execute("""
#         SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
#         WHERE email LIKE '%@adipiscingenimmi.edu'
#         ;""")
#     return common.print_query_table(cursor, "")


# def add_new_applicant(cursor):
#     cursor.execute("""
#         INSERT INTO applicants (id, first_name, last_name, phone_number, email, application_code)
#         VALUES (11, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823)
#         ;""")
#     cursor.execute("""
#         SELECT * FROM applicants
#         WHERE application_code = 54823
#         ;""")
#     return common.print_query_table(cursor, "")


# def change_phonenumber(cursor):
#     cursor.execute("""
#         UPDATE applicants
#         SET phone_number = '003670/223-7459'
#         WHERE first_name = 'Jemima' AND last_name = 'Foreman'
#         ;""")
#     cursor.execute("""
#         SELECT phone_number FROM applicants
#         WHERE first_name = 'Jemima' AND last_name = 'Foreman'
#         ;""")
#     return common.print_query_table(cursor, "")


# def del_arsiano_and_his_friend(cursor):
#     cursor.execute("""
#         DELETE FROM applicants
#         WHERE email LIKE '%@mauriseu.net'
#         ;""")
#     all_data_applicants()


# def all_data_mentors(cursor):
#     cursor.execute("""SELECT * FROM mentors ORDER BY id;""")
#     return common.print_query_table(cursor, "All the mentors")


# def all_data_applicants(cursor):
#     # run the query
#     cursor.execute("""SELECT * FROM applicants ORDER BY id;""")
#     # return in table format
#     return common.print_query_table(cursor, "All the applicants")


# '''
# app process part 2
# '''


# def mentors_and_schools(cursor):
#     cursor.execute("""
#         SELECT mentors.first_name, mentors.last_name, schools.name AS school_name, schools.country
#         FROM mentors
#         LEFT JOIN schools ON mentors.city = schools.city
#         ORDER BY mentors.id;
#         """)
#     return cursor


# def all_school(cursor):
#     cursor.execute("""
#         SELECT mentors.first_name, mentors.last_name, schools.name AS school_name, schools.country
#         FROM mentors
#         RIGHT JOIN schools ON mentors.city = schools.city
#         ORDER BY mentors.id;
#         """)
#     return cursor


# def mentors_by_country(cursor):
#     cursor.execute("""
#         SELECT schools.country, COUNT(mentors.id) AS count_mentors
#         FROM mentors
#         RIGHT JOIN schools ON mentors.city = schools.city
#         GROUP BY schools.country
#         ORDER BY schools.country;
#         """)
#     return cursor


# def contacts(cursor):
#     cursor.execute("""
#         SELECT schools.name AS school_name, mentors.first_name, mentors.last_name
#         FROM mentors
#         JOIN schools ON schools.contact_person = mentors.id
#         ORDER BY schools.name;
#         """)
#     return cursor


# def applicants(cursor):
#     cursor.execute("""
#         SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
#         FROM applicants
#         JOIN applicants_mentors ON applicants_mentors.applicant_id = applicants.id
#         WHERE applicants_mentors.creation_date > '2016-01-01'
#         ORDER BY applicants_mentors.creation_date DESC;
#         """)
#     return cursor


# def applicants_and_mentors_(cursor):
#     cursor.execute("""
#         SELECT applicants.first_name AS applicant_first_name,
#             applicants.application_code,
#             mentors.first_name AS mentor_first_name,
#             mentors.last_name AS mentor_last_name
#         FROM applicants
#         LEFT JOIN applicants_mentors ON applicants_mentors.applicant_id = applicants.id
#         LEFT JOIN mentors on applicants_mentors.mentor_id = mentors.id
#         ORDER BY applicants.id;
#         """)
#     return cursor

