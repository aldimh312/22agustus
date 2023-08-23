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
    
    

# ----------------TENTANG MUSEUM---------------------
from .models import TentangMuseum

class TentangMuseumForm(forms.ModelForm):
    class Meta:
        model = TentangMuseum
        fields = ['sejarah', 'gambar_museum', 'visi_misi', 'gambar_struktur_organisasi', 'alamat_museum', 'email_museum', 'nomor_hp', 'instagram']
        widgets = {
            'sejarah': forms.Textarea(attrs={'class': 'form-control'}),
            'gambar_museum': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'visi_misi': forms.Textarea(attrs={'class': 'form-control'}),
            'gambar_struktur_organisasi': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'alamat_museum': forms.TextInput(attrs={'class': 'form-control'}),
            'email_museum': forms.TextInput(attrs={'class': 'form-control'}),
            'nomor_hp': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
        }


from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tanggal_pengajuan', 'tanggal_kunjungan', 'no_hp', 'asal_rombongan', 'jumlah_rombongan']
        widgets = {
            'tanggal_pengajuan': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tanggal_kunjungan': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'no_hp': forms.TextInput(attrs={'class': 'form-control'}),
            'asal_rombongan': forms.TextInput(attrs={'class': 'form-control'}),
            'institusi': forms.TextInput(attrs={'class': 'form-control'}),
            'jumlah_rombongan': forms.NumberInput(attrs={'class': 'form-control'}),
          
        }