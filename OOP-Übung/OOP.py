class firma():
    
    def __init__(self, name, abteilungen):
        self.name = name
        self.abteilungen = abteilungen
        self.anz_abteilungsleiter = len(abteilungen)
    
    def getMitarbeiterAnz(self):
        anz = 0
        for a in self.abteilungen:
            anz += a.anz_mitarbeiter
        return anz
    
    def getAbteilungsleiterAnz(self):
        return len(self.abteilungen)
    
    def getAbteilungenAnz(self):
        return len(self.abteilungen)
    
    def getHighestAbteilung(self):
        anz = 0
        ab = None
        for a in self.abteilungen:
            if a.anz_mitarbeiter > anz:
               anz = a.anz_mitarbeiter
               ab = a
        return ab.name
    
    def getGenderRatio(self):
        dic = {'mann': 0, 'frau': 0}
        ges = self.getMitarbeiterAnz()
        for a in self.abteilungen:
            for p in a.mitarbeiter:
                if p.geschlecht == 'mann':
                    dic['mann'] += round(1/ges, 4)
                else:
                    dic['frau'] += round(1/ges, 4)
        return dic
    
    
class abteilung():
    
    def __init__(self, name, mitarbeiter, abteilungsleiter, firma):
        self.name = name
        self.mitarbeiter = mitarbeiter
        self.anz_mitarbeiter = len(mitarbeiter) 
        self.abteilungsleiter = abteilungsleiter
        self.firma = firma

class person():
    
    def __init__(self, vname, nname, alter, geschlecht):
        self.vname = vname
        self.nname = nname
        self.alter = alter
        self.geschlecht = geschlecht

class mitarbeiter(person):
    
    def __init__(self, vname, nname, alter, geschlecht, abteilung):
        super().__init__(vname, nname, alter, geschlecht)
        self.abteilung = abteilung

class abteilungsleiter(mitarbeiter):
    
    def __init__(self, vname, nname, alter, geschlecht, abteilung):
        super().__init__(vname, nname, alter, geschlecht, abteilung)




if __name__ == '__main__':
    f1 = firma('Tollste Firma ever', [])
    m1 = mitarbeiter('Hans', 'Peter', 68, 'mann', None)
    m2 = mitarbeiter('Birgitt', 'Brigitte', 15, 'frau', None)
    m3 = mitarbeiter('Marlene', 'Brigitte', 15, 'frau', None)
    m4 = mitarbeiter('Hallo', 'Brigitte', 15, 'mann', None)
    m5 = mitarbeiter('Pedda', 'Pedda', 15, 'mann', None)
    al1 = abteilungsleiter('Peter', 'Hans', 50, 'mann', None)
    al2 = abteilungsleiter('Favi', 'Favi', 500, 'mann', None)
    a1 = abteilung('IT', [m1, al1, m2], al1, f1)
    a2 = abteilung('HR', [m3, m4, al2, m5], al2, f1)
    
    m1.abteilung = a1
    m2.abteilung = a1
    al1.abteilung = a1
    
    f1.abteilungen = [a1, a2]
    
    print(f1.getGenderRatio())