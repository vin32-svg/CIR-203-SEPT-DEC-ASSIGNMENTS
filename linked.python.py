def create_node(name, adm, grades, next_node=None):
    return {
        "name": name,
        "adm": adm,
        "grades": grades, 
        "next": next_node  
    }
def insert(head, name, adm, grades):
    new_node = create_node(name, adm, grades)
    if head is None:
        return new_node
    current = head
    while current["next"] is not None:
        current = current["next"]
    current["next"] = new_node
    return head
def traverse(head):
    current = head
    while current is not None:
        print(f"Name: {current['name']}, Adm: {current['adm']}, Grades: {current['grades']}")
        current = current["next"]
head = None
head = insert(head, "sharon", "CIT/00044/024", [ [80, 75, 90], [70, 85, 88], [92, 89, 95] ])
head = insert(head, "valen", "CIT/00012/024", [ [60, 65, 70], [72, 68, 74], [80, 85, 78] ])
head = insert(head, "anne", "CIT/00034/024", [ [88, 90, 85], [76, 80, 79], [91, 93, 89] ])
traverse(head)

