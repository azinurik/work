# phonebook.py

from connect import get_connection

conn = get_connection()

if conn:
    cur = conn.cursor()

    # Вставка контактов
    cur.execute("CALL upsert_contact(%s, %s);", ("Alisher", "1234567890"))
    cur.execute("CALL upsert_contact(%s, %s);", ("Body", "9876543210"))
    
    # Вставка нескольких контактов
    names = ["Karlik", "Diana"]
    phones = ["111222333", "abc123"]  # второй телефон неверный
    cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))
    
    # Поиск по шаблону
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s::text);", ("A",))
    print("Поиск по шаблону 'A':")
    for row in cur.fetchall():
        print(row)
        
    # Пагинация
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (2, 0))
    print("Пагинация (limit 2, offset 0):")
    for row in cur.fetchall():
        print(row)
        
    # Удаление контакта
    cur.execute("CALL delete_contact(%s);", ("Alice",))
    conn.commit()
    cur.close()
    conn.close()
    
    
    
    #cur.execute("CALL delete_contact(%s);", ("Alice",)
    #cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (2, 0))
    #cur.execute("SELECT * FROM get_contacts_by_pattern(%s::text);", ("A",))
    #cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))
    #cur.execute("CALL upsert_contact(%s, %s);", ("Alice", "1234567890"))