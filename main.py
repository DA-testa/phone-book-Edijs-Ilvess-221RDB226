# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(query):
    print('\n'.join(result))
    
def add_contact(contacts, cur_query):
    contacts[cur_query.number]=cur_query.name
def del_contact(contacts, cur_query):
    contacts.pop(cur_query.number,None)
def find_contact(contacts, cur_query, result):
    if cur_query.number in contacts:
        return contacts[cur_query.number]
    else:
        return "not found"
def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    case = {
        'add':add_contact,
        'del':del_contact,
        'find':find_contact
    }
    for cur_query in queries:
        if cur_query.type in case:
            case[cur_query.type](contacts,cur_query,result)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

