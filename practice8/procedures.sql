--upsert (правильный вариант без IF EXISTS)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO contacts(name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (phone)
    DO UPDATE SET name = EXCLUDED.name;
END;
$$;
--insert_many_contacts (безопасный batch insert)
CREATE OR REPLACE PROCEDURE insert_many_contacts(p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    len INT;
BEGIN
    len := LEAST(array_length(p_names, 1), array_length(p_phones, 1));

    FOR i IN 1..len LOOP
        IF p_phones[i] ~ '^[0-9]+$' THEN
            CALL upsert_contact(p_names[i], p_phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone skipped: %', p_phones[i];
        END IF;
    END LOOP;
END;
$$;
--delete_contact
CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;