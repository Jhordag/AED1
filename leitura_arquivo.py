
class Arquivo():
    def __init__(self,nome):
        self.nome = nome
        self.list = []

    def lerArquivo(self):
        with open(self.nome) as f:
            for line in f:
                if(line.strip() != ''): 
                    line_spl = line.split(' ') 
                    cols = line_spl[:] 
                    self.list.append([cols[2].strip(),cols[0],cols[1]]) 
        return self.list


