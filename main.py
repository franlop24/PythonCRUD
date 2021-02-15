import sys
import csv
import os

CLIENT_TABLE = ".clients.csv"
CLIENTS_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def __initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENTS_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENTS_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the Client\'s list')


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def update_client(client_id):
    global clients
    client_id = int(client_id)

    if client_id > len(clients):
        return
    
    client_to_update = clients[client_id]
    print(f'{client_id}: {client_to_update["name"]}')

    choise = input('Is the cliend do you want to Update? [y/n]')
    
    if choise == 'y':
        choise = input(f"client name: { client_to_update['name'] } \n Update name? [y/n]")
        if choise == 'y':
            client_to_update['name'] = _get_client_field('name')

        choise = input(f"client company: { client_to_update['company'] } \n Update company? [y/n]")
        if choise == 'y':
            client_to_update['company'] = _get_client_field('company')

        choise = input(f"client email: { client_to_update['email'] } \n Update email [y/n]")
        if choise == 'y':
            client_to_update['email'] = _get_client_field('email')

        choise = input(f"client position: { client_to_update['position'] } \n Update position [y/n]")
        if choise == 'y':

            client_to_update['position'] = _get_client_field('position')
    else:
        print('Client is not updated')


def delete_client(client_id):
    global clients
    client_id = int(client_id)

    if client_id > len(clients):
        return

    print(f'{client_id}: {clients[client_id]["name"]}')
    
    choise = input('Is the cliend do you want to delete? [y/n]')
    
    if choise == 'y':
        client_deleted = clients.pop(client_id)
        print(client_deleted)
    else:
        print('Client is not deleted')


def search_client(client_name):
    global clients

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('* '*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    

def _get_client_field(field_name):
    field = None
    while not field:
        field = input(f'What is the client {field_name}? ')
    
        if field == 'exit':
            sys.exit()

    return field

def _get_client_name(client_name):
    pass

if __name__ == '__main__':
    __initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)
    elif command == 'D':
        list_clients()
        id_client = input('What is the client ID do you want to Delete? ')
        delete_client(id_client)
        list_clients()
    elif command == 'U':
        list_clients()
        id_client = input('What is the client ID do you want to Update? ')
        update_client(id_client)
    elif command == 'L':
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the list client\'s')
        else:
            print(f'The client: {client_name} is not in our clients\'s list')
    else:
        print('Invalid command')
    _save_clients_to_storage()