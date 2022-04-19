class Paciente:
    def __init__(self):
        self.nome = [0]
        self.tipo_sang = ''
        self.data_nasc = ''


class MaxHeap:
    def __init__(self):
        self.heap = [1]
        self.cont = 999
        self.pacientes = []

    def put(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)
        self.cont -= 1

    def get(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right
        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)


fila = MaxHeap()
p = Paciente()

while True:

    menu = int(input('''

        [ 1 ] - Adicionar novo paciente.
        [ 2 ] - Chama próximo paciente.
        [ 3 ] - Mostrar próximo paciente.
        [ 4 ] - Listar os últimos 5 pacientes.
        [ 5 ] - Parar programa.

    '''))

    if menu == 1:
        nome = input('Digite o nome: ')
        tipo_sang = input('Tipo sanguineo: ')
        data_nasc = input('Data nascimento: ')

        p.nome = nome
        p.tipo_sang = tipo_sang
        p.data_nasc = data_nasc
        novo_paciente = (fila.cont, (p.nome, p.tipo_sang, p.data_nasc))

        fila.put(novo_paciente)
    elif menu == 2:
        print("ID: ", fila.get())
    elif menu == 3:
        print("O próximo paciente é: ", fila.heap[-1])
    elif menu == 4:
        print("Os últimos 5 pacientes são: ")
        for i in range(5):
            i += -5
            print(fila.heap[i])

    elif menu == 5:
        break
