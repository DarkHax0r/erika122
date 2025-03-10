from django.forms import ModelForm
from website_app.models import Pengunjung
from django import forms 
from django.contrib.auth.models import User


# ----------------DAFTAR PENGUNJUNG ---------------------

class PengunjungForm(forms.ModelForm):
    class Meta:
        model = Pengunjung
        fields = ['nama', 'kategori', 'jumlah', 'asal']

        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jika Kelompok Maka Ketik "Grup" '}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Jumlah'}),
            'asal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instansi/Negara/Kota/Provinsi'}),
        }

# ----------------KELOLA BERITA---------------------
from website_app.models import Berita

class BeritaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gambar'].widget.attrs.update({'class': 'form-control'})
        self.fields['judul'].widget.attrs.update({'class': 'form-control'})
        self.fields['deskripsi'].widget.attrs.update({'class': 'form-control', 'rows': 3})

    class Meta:
        model = Berita
        fields = ['gambar', 'judul', 'deskripsi']
        labels = {
            'gambar': 'Gambar',
            'judul': 'Judul',
            'deskripsi': 'Deskripsi',
        }


# ---------------- KELOLA KOLEKSI---------------------
from .models import Koleksi

class KoleksiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama_koleksi'].widget.attrs.update({'class': 'form-control'})
        self.fields['gambar'].widget.attrs.update({'class': 'form-control'})
        self.fields['deskripsi'].widget.attrs.update({'class': 'form-control', 'rows': 3})

    class Meta:
        model = Koleksi
        fields = ['nama_koleksi', 'gambar', 'deskripsi']
        labels = {
            'nama_koleksi': 'Nama Koleksi',
            'gambar': 'Gambar',
            'deskripsi': 'Deskripsi',
        }     

# ----------------LOGIN---------------------
class formlogin(forms.Form):
    username = forms.CharField(
            max_length=30,
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'username',
        
                }
            )
        )
    password = forms.CharField(
            max_length=254,
            widget=forms.PasswordInput(
                attrs={
                    'placeholder': 'password',
                }
            )
        )
    
    
# -------------Kelola Booking---------------

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'  # Ini akan mencakup semua kolom dari model Booking
        # Jika Anda ingin menentukan kolom-kolom tertentu secara manual, Anda dapat menggunakan:
        # fields = ['tanggal_pengajuan', 'waktu_pengajuan', 'no_hp', 'asal_rombongan', 'institusi', 'jumlah_rombongan']

from django.shortcuts import render, redirect
from .forms import BookingForm

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Ganti 'success_page' dengan URL yang sesuai
    else:
        form = BookingForm()
    
    return render(request, 'booking_form.html', {'form': form})
