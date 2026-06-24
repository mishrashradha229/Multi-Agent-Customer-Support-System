from database.database import get_connection
def create_ticket(
    customer,
    query,
    category,
    priority,
    status="Open",
    resolution="",
    language="English"
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tickets (
            customer,
            query,
            category,
            priority,
            status,
            resolution,
            language
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        customer,
        query,
        category,
        priority,
        status,
        resolution,
        language
    ))

    conn.commit()

    ticket_id = cursor.lastrowid
    conn.close()

    return ticket_id

def get_all_tickets():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tickets
        ORDER BY ticket_id DESC
    """)

    tickets = cursor.fetchall()
    conn.close()

    return [dict(ticket) for ticket in tickets]

def get_ticket(ticket_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tickets
        WHERE ticket_id = ?
    """, (ticket_id,))

    ticket = cursor.fetchone()
    conn.close()

    return dict(ticket) if ticket else None


def update_ticket(ticket_id, resolution):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tickets
        SET resolution = ?,
            status = 'Resolved'
        WHERE ticket_id = ?
    """, (resolution, ticket_id))

    conn.commit()
    conn.close()

def close_ticket(ticket_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tickets
        SET status = 'CLOSE'
        WHERE ticket_id = ?
    """, (ticket_id,))

    conn.commit()
    conn.close()

def delete_ticket(ticket_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tickets
        WHERE ticket_id = ?
    """, (ticket_id,))

    conn.commit()
    conn.close()