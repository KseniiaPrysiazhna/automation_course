import app

def test_connection():
    conn = app.get_connection()
    assert conn is not None
    conn.close()

def test_insert_and_select():
    app.create_table()
    user_id = app.insert_user("Alice", 25)
    users = app.select_users()
    assert any(u[0] == user_id for u in users)

def test_update():
    user_id = app.insert_user("Bob", 30)
    app.update_user(user_id, 35)
    users = app.select_users()
    updated_user = [u for u in users if u[0] == user_id][0]
    assert updated_user[2] == 35

def test_delete():
    user_id = app.insert_user("Charlie", 28)
    app.delete_user(user_id)
    users = app.select_users()
    assert all(u[0] != user_id for u in users)