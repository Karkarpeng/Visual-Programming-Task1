class Mahasiswa():
	def __init__ (self, masukkan_nama, masukkan_kelas, masukkan_prodi, masukkan_fakultas, masukkan_tempat_tinggal, masukkan_asal):
		self.nama = masukkan_nama
		self.kelas = masukkan_kelas
		self.prodi = masukkan_prodi
		self.fakultas = masukkan_fakultas
		self.tempat_tinggal = masukkan_tempat_tinggal
		self.asal = masukkan_asal
objek = Mahasiswa("Aqmal Al Gifahri", "A", "Pendidikan Komputer", "FKIP", "Sentosa 2A", "Berau")

print("Data Diri :")
print("Nama :", objek.nama)
print("Kelas :",objek.kelas)
print("Prodi :", objek.prodi)
print("Fakultas :", objek.fakultas)
print("Tempat Tinggal :", objek.tempat_tinggal)
print("Asal :", objek.asal)
