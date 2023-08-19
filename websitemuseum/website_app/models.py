from django.db import models
from django.db.models import Sum
from django.db.models import Count



# ---------------- DAFTAR PENGUNJUNG---------------------
class Pengunjung(models.Model):
    KATEGORI_CHOICES = (
        ('umum', 'Umum'),
        ('siswa', 'Siswa'),
        ('mahasiswa', 'Mahasiswa'),
    )
    id_daftar_pengunjung = models.AutoField(primary_key=True)
    tanggal = models.DateField(auto_now_add=True)
    
    nama = models.CharField(max_length=255)
    kategori = models.CharField(max_length=10, choices=KATEGORI_CHOICES)
    jumlah = models.IntegerField()
    asal = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

    def total_pengunjung():
        return Pengunjung.objects.aggregate(total_jumlah=Sum('jumlah'))['total_jumlah'] or 0

# ----------------KELOLA BERITA---------------------
class Berita(models.Model):
    id_berita = models.AutoField(primary_key=True)
    tanggal = models.DateField(auto_now_add=True)
    gambar = models.ImageField(upload_to='berita/') 
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    
    def __str__(self):
        return self.judul
    
    def total_berita():
         return Berita.objects.aggregate(total_jumlah=Count('judul'))['total_jumlah'] or 0

        
# ----------------KELOLA KOLEKSI---------------------
class Koleksi(models.Model):
    id_koleksi = models.AutoField(primary_key=True)
    tanggal = models.DateField(auto_now_add=True)
    nama_koleksi = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to='koleksi/')
    deskripsi = models.TextField()
    def __str__(self):
        return self.nama_koleksi
    
    def total_koleksi():
        return Koleksi.objects.aggregate(total_jumlah=Count('nama_koleksi'))['total_jumlah'] or 0
    
# -------------------RATING-----------------
class Rating(models.Model):
    RATING_CHOICES = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )
    id_rating = models.AutoField(primary_key=True)
    pesan = models.TextField()
    kesan = models.TextField()
    bintang = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.kesan


# -----------------------Booking--------------------

from django.db import models

class Booking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    tanggal_pengajuan = models.DateField()
    waktu_pengajuan = models.TimeField()
    no_hp = models.CharField(max_length=15)
    asal_rombongan = models.CharField(max_length=100)
    institusi = models.CharField(max_length=100)
    jumlah_rombongan = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking {self.id_booking}"


        




















    # def save(self, *args, **kwargs):
    #     if not self.no:  # Hanya berlaku saat objek baru dibuat
    #         last_koleksi = Koleksi.objects.order_by('-no').first()
    #         self.no = last_koleksi.no + 1 if last_koleksi else 1
    #     super().save(*args, **kwargs)
