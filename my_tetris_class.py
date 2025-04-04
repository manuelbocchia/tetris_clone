def change_shape(self, placex=0,placey=0):

        self["loc"] = [[placex,placey],[placex,placey],[placex,placey],[placex,placey]]
        if self["shape"] == 'L' and self["rotate"] == 1:
            self["loc"][1][1] -= self["size"]
            self["loc"][2][1] -= self["size"]*2
            self["loc"][3][0] += self["size"]

        if self["shape"] == 'L' and self["rotate"] == 2:
            self["loc"][1][0] += self["size"]
            self["loc"][2][0] += self["size"]*2
            self["loc"][2][1] -= self["size"]
            self["loc"][3][0] += self["size"]*2

        if self["shape"] == 'L' and self["rotate"] == 3:

            self["loc"][1][0] += self["size"]
            self["loc"][2][0] += self["size"]
            self["loc"][2][1] += self["size"]
            self["loc"][3][1] += self["size"]*2
            self["loc"][3][0] += self["size"]
        if self["shape"] == 'L' and self["rotate"] == 4:
            self["loc"][0] = self["loc"][0]
            self["loc"][1][1] += self["size"]
            self["loc"][2][0] += self["size"]
            self["loc"][3][0] += self["size"]*2
        if self["shape"] == 'O':
            self["loc"][0] = self["loc"][0]
            self["loc"][1][0] += self["size"]
            self["loc"][2][1] += self["size"]
            self["loc"][3][0] += self["size"]
            self["loc"][3][1] += self["size"]
        if self["shape"] == 'S' and self["rotate"] == 1:

            self["loc"][1][1] += self["size"]
            self["loc"][2][0] += self["size"]
            self["loc"][2][1] += self["size"]
            self["loc"][3][0] += self["size"]
            self["loc"][3][1] += self["size"]*2
        if self["shape"] == 'S' and self["rotate"] == 2:

            self["loc"][3][0] += self["size"]
            self["loc"][1][1] -= self["size"]
            self["loc"][1][0] += self["size"]
            self["loc"][2][1] -= self["size"]
            self["loc"][2][0] += self["size"]*2
        if self["shape"] == 'Z' and self["rotate"] == 1:

            self["loc"][1][0] += self["size"]
            self["loc"][1][1] -= self["size"]
            self["loc"][2][0] += self["size"]
            self["loc"][3][1] += self["size"]
        if self["shape"] == 'Z' and self["rotate"] == 2:

            self["loc"][1][0] += self["size"]
            self["loc"][2][0] += self["size"]
            self["loc"][2][1] += self["size"]
            self["loc"][3][1] += self["size"]
            self["loc"][3][0] += self["size"]*2
        if self["shape"] == 'J' and self["rotate"] == 1:

            self["loc"][3][0] += self["size"]
            self["loc"][1][0] += self["size"]
            self["loc"][1][1] -= self["size"]
            self["loc"][2][0] += self["size"]
            self["loc"][2][1] -= self["size"]*2

        if self["shape"] == 'J' and self["rotate"] == 2:
            self["loc"][0] = self["loc"][0]
            self["loc"][1][1] += self["size"]
            self["loc"][2][0] += self["size"]
            self["loc"][2][1] += self["size"]
            self["loc"][3][0] += self["size"]*2
            self["loc"][3][1] += self["size"]
        if self["shape"] == 'J' and self["rotate"] == 3:

            self["loc"][1][0] += self["size"]
            self["loc"][2][1] += self["size"]
            self["loc"][3][1] += self["size"]*2
        if self["shape"] == 'J' and self["rotate"] == 4:

            self["loc"][1][0] += self["size"]
            self["loc"][2][0] += self["size"]*2
            self["loc"][3][0] += self["size"]*2
            self["loc"][3][1] += self["size"]
        if self["shape"] == "I" and self["rotate"] == 1:

            self["loc"][1][1] -= self["size"]
            self["loc"][2][1] += self["size"]
            self["loc"][3][1] += self["size"]*2
        if self["shape"] == "I" and self["rotate"] == 2:

            self["loc"][1][0] -= self["size"]
            self["loc"][2][0] += self["size"]
            self["loc"][3][0] += self["size"]*2
        
        self["full_size"] = self["loc"][3][1]

def fall(self):
    self["place"] = self["loc"][0][0]
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