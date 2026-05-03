import sqlite3
from sqlite3 import Error


def create_connection(path:str) -> sqlite3.Connection:
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection established")
    except Error as e:
        print(e)
    return connection


def execute_query(connection:sqlite3.Connection, query:str) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed")
    except Error as e:
        print(e)
        connection.rollback()
        print("Rollback executed")

def select_query(connection:sqlite3.Connection, query:str) -> list | None:
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(e)



if __name__=="__main__":
    connection = create_connection('../database.db')

    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT,
        location TEXT
    );
    """
    execute_query(connection, create_users_table)

    create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        body TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """
    execute_query(connection, create_posts_table)

    create_comments_table ="""
    CREATE TABLE IF NOT EXISTS comments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        post_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (post_id) REFERENCES posts (id)
        FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """
    execute_query(connection, create_comments_table)
    create_likes_table = """
    CREATE TABLE IF NOT EXISTS likes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        post_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
        FOREIGN KEY (post_id) REFERENCES posts (id)
        )
    """
    execute_query(connection, create_likes_table)


    create_users = """
    INSERT INTO users (name, age, gender, location)
    VALUES
        ('Vladyslav',20,'male','Poland'),
        ('Liubomyr',25,'male','Ukraine'),
        ('Anton',30,'male','Ukraine'),
        ('Serhiy',35,'male','Ukraine'),
        ('Olga',40,'female','Ukraine');
    """
    # execute_query(connection, create_users)
    update_name = """
    UPDATE users
    SET name = 'Vlad'
    WHERE id = 1;
    """

    # execute_query(connection, update_name)

    create_posts = """
    INSERT INTO posts (title, body, user_id),
    VALUES
        ('first post','my first post',1),
        ('second post','my second post',2),
        ('third post','my third post',3),
        ('fourth post','my fourth post',4),
        ('fifth post','my fifth post',5),
        ('second post','my second post',1):
    """
    # execute_query(connection, create_posts)
    create_comments = """
    INSERT INTO comments (text, post_id, user_id),
    VALUES
        ('first comment',1,2),
        ('second comment',2,3),
        ('third comment',3,4),
        ('fourth comment',4,5),
        ('fifth comment',5,6),
    """
    # execute_query(connection, create_comments)

    create_likes="""
    INSERT INTO likes (user_id, post_id),
    VALUES
        (1,6),
        (2,3),
        (3,5);
    """

    # execute_query(connection, create_likes)

    # select_users = "SELECT * FROM users WHERE age = 18 OR age = 20;"
    # result= select_query(connection, select_users)
    # for row in result:
    #     print(row)
    #     print('-'*80)

    select_users_posts="""
    SELECT users_name, posts.body FROM posts 
    INNER JOIN users on users.id = posts.user_id
    WHERE users.name= 'Vladyslav'
    """
    # select_posts = "SELECT * FROM posts WHERE body LIKE '%second%';"
    # result = select_query(connection, select_posts)
    # for row in result:
    #     print(row)
    #     print('-' * 80)

    select_posts_comments_users = """
    SELECT
        posts.body
        comments.text,
        users.name
    FROM posts
        INNER JOIN comments ON posts.id = comments.post_id
        INNER JOIN users ON users.id = comments.user_id
    """
    # result = select_query(connection, select_posts_comments_users)
    # for row in result:
    #     print(row)
    #     print('-' * 80)


    select_posts_likes = """
    SELECT
        posts.body,
        COUNT(likes.id) AS likes_count
    FROM likes
    INNER JOIN posts ON posts.id = likes.post_id
    GROUP BY posts.body    
    """
    # result = select_query(connection, select_posts_likes)
    # for row in result:
    #     print(row)
    #     print('-' * 80)

    delete_comment = "DELETE FROM comments WHERE id = 2"
    # execute_query(connection, delete_comment)

    connection.close()

