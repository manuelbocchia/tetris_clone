
#my_piece = {'shape':'L', 'place':0, 'size' : 20, 'color' : 'black', 'loc':[[0,0],[0,0],[0,0],[0,0]], "full_size":0}

def change_shape(self):
        self["loc"] = [[self["place"],self["size"]],[self["place"],self["size"]],[self["place"],self["size"]],[self["place"],self["size"]]]
        if self["shape"] == 'L':
            self["loc"][0] = self["loc"][0]
            self["loc"][1][1] += self["size"]
            self["loc"][2][1] += self["size"]*2
            self["loc"][3][0] += self["size"]
            self["loc"][3][1] += self["size"]*2
        if self["shape"] == 'O':
            self["loc"][0] = self["loc"][0]
            self["loc"][1][0] += self["size"]
            self["loc"][2][1] += self["size"]
            self["loc"][3][0] += self["size"]
            self["loc"][3][1] += self["size"]
        if self["shape"] == 'S':
            self["loc"][0] = self["loc"][0]
            self["loc"][1][1] += self["size"]
            self["loc"][2][0] += self["size"]
            self["loc"][2][1] += self["size"]
            self["loc"][3][0] += self["size"]
            self["loc"][3][1] += self["size"]*2
        if self["shape"] == 'SR':
            self["loc"][0][0] += self["size"]
            self["loc"][1][0] += self["size"]
            self["loc"][1][1] += self["size"]
            self["loc"][2][0] += self["size"]*2
            self["loc"][3][0] += self["size"]
            self["loc"][3][1] += self["size"]*2
        if self["shape"] == 'LR':
            self["loc"][0][0] += self["size"]
            self["loc"][1][0] += self["size"]
            self["loc"][1][1] += self["size"]
            self["loc"][2][1] += self["size"]*2
            self["loc"][3][0] += self["size"]
            self["loc"][3][1] += self["size"]*2
        if self["shape"] == "I":
            self["loc"][0] = self["loc"][0]
            self["loc"][1][1] += self["size"]
            self["loc"][2][1] += self["size"]*2
            self["loc"][3][1] += self["size"]*3
        
        self["full_size"] = self["loc"][3][1]

def fall(self):
    self["loc"][0][1] += self["size"]
    self["loc"][1][1] += self["size"]
    self["loc"][2][1] += self["size"]
    self["loc"][3][1] += self["size"]
def m_right(self):
    self["loc"][0][0] += self["size"]
    self["loc"][1][0] += self["size"]
    self["loc"][2][0] += self["size"]
    self["loc"][3][0] += self["size"]
def m_left(self):
    self["loc"][0][0] -= self["size"]
    self["loc"][1][0] -= self["size"]
    self["loc"][2][0] -= self["size"]
    self["loc"][3][0] -= self["size"]


#print(my_piece)
#
#change_shape(my_piece)
#
#print(my_piece)
#
#my_piece['shape'] = 'LR'
#
#change_shape(my_piece)
#
#print(my_piece)
#
#fall(my_piece)
#
#print(my_piece)