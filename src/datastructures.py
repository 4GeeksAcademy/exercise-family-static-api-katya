
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = "Jackson"
        self._next_id = 1
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        }, {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        }, {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        
        first_name = member['first_name']
        age = member['age']
        lucky_numbers = member['lucky_numbers']

        member = {
            'first_name': first_name,
            'age': age,
            'lucky_numbers': lucky_numbers
        }

        member['id'] = self._generateId()
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member['id'] == id:
                del self._members[i]
        return self._members

    def get_member(self, id):
        for i, member in enumerate(self._members):
            if member['id'] == id:
                return self._members[i]
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
