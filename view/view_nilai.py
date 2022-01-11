class ViewNilai():
    def __init__ (self, Nilai = []):
        self.Nilai = Nilai
    
    def list(self):
        while True:
            self.clear()
            print("\nDaftar Nama\n")
            print("==================================================")
            print("|  NIM  |  Nama  | Tugas | UTS |  UAS  |  Akhir  |")
            print("==================================================")
            for x in (self.data):
                print("|  {0:1}    |  {1:1}     |  {2:1}    |  {3:1}   |  {4:1}   |  {5:1}  |".format(x[0], x[1], x[2], x[3], x[4], x[5]))
            print("==================================================")