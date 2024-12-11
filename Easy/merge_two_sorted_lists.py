# São fornecidos os cabeçalhos de duas listas encadeadas classificadas list1e list2.

# Mescle as duas listas em uma lista ordenada . A lista deve ser feita juntando os nós das duas primeiras listas.

# Retorna o cabeçalho da lista vinculada mesclada .

# Entrada: lista1 = [1,2,4], lista2 = [1,3,4]
#  Saída: [1,1,2,3,4,4]
# Exemplo 2:

# Entrada: lista1 = [], lista2 = []
#  Saída: []
# Exemplo 3:

# Entrada: lista1 = [], lista2 = [0]
#  Saída: [0]

# list1 = [1,2,4]
# list2 = [1,3,4]

# def mergeTwoLists(list1, list2):
#   final_list = []
#   final_list = list1 + list2
#   final_list.sort()
#   return final_list
        

# merged_list = mergeTwoLists(list1,list2)

# print(merged_list)

from locale import currency
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      values1 = self.extract_values(list1)
      values2 = self.extract_values(list2)
      
      all_values = values1 + values2
      all_values.sort()
      
      return self.create_linked_list_from_values(all_values)
    
    def extract_values(self, list_node):
      values = []
      current = list_node
      while current:
        values.append(current.val)
        current = current.next
      return values
    
    def create_linked_list_from_values(self, values):
      prehead = ListNode(-1)
      current = prehead
      for val in values:
        current.next = ListNode(val)
        current = current.next
      return prehead.next