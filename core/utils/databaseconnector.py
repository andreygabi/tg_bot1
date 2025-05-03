import asyncpg

class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_user(self, user_id, contact_name, contact_tag, contact_info):
        query = f"INSERT INTO contacts_data_table (user_id, contact_name, contact_tag, contact_info) VALUES ({user_id}, '{contact_name}', '{contact_tag}', '{contact_info}')"
        await self.connector.execute(query)

    async def delete_contact(self, user_id, contact_tag):
        query = f"DELETE FROM contacts_data_table WHERE (user_id = {user_id}) AND (contact_tag = '{contact_tag}')"
        await self.connector.execute(query)

    async def reg_user_id(self, user_id):
        query = f"INSERT INTO users_id (users_id) VALUES ({user_id})"
        await self.connector.execute(query)

    async def view_contacts(self, user_id):
        con = await asyncpg.connect(user='postgres')
        types = await con.fetch(f'SELECT * FROM contacts_data_table WHERE (user_id = {user_id})')
        return types