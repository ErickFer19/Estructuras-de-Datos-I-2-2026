import time

class TaskNode:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description
        self.estado = 'pendiente'  # 'pendiente' o 'completada'
        self.siguiente = None      # Puntero al siguiente nodo

class TaskLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, title, description):
        new_id = int(time.time() * 1000)
        new_node = TaskNode(new_id, title, description)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.siguiente:
                current = current.siguiente
            current.siguiente = new_node
        self.size += 1

    def toggle_status(self, task_id):
        current = self.head
        while current:
            if current.id == task_id:
                current.estado = 'completada' if current.estado == 'pendiente' else 'pendiente'
                return True
            current = current.siguiente
        return False

    def delete(self, task_id):
        if not self.head:
            return False

        if self.head.id == task_id:
            self.head = self.head.siguiente
            self.size -= 1
            return True

        current = self.head
        while current.siguiente:
            if current.siguiente.id == task_id:
                current.siguiente = current.siguiente.siguiente  # O(1) lógico
                self.size -= 1
                return True
            current = current.siguiente
        return False

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append({
                'id': current.id,
                'title': current.title,
                'description': current.description,
                'estado': current.estado
            })
            current = current.siguiente
        return elements

task_list_db = TaskLinkedList()