from django.contrib import admin



#-------------------DAFTAR PENGUNJUNG--------------------
from website_app.models import  Pengunjung
from django.urls import reverse
from django.utils.html import format_html
from .forms import PengunjungForm

class PengunjungAdmin(admin.ModelAdmin):
    list_filter = ('kategori', 'asal')  # Menambahkan filter berdasarkan tanggal, kategori, dan asal
    form = PengunjungForm
    
    def tambah_pengunjung_link(self, obj):
        tambah_url = reverse('app_user:pengunjung')
        return format_html('<a href="{}">Tambah Pengunjung</a>', tambah_url)
        
admin.site.register(Pengunjung, PengunjungAdmin)



#------------------------- KELOLA BERITA-------------------------
from website_app.models import Berita

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ['gambar', 'judul', 'deskripsi']
    search_fields = ['nama', 'judul', 'deskripsi']


#-------------------------KELOLA KOLEKSI-------------------------
from .models import Koleksi

class KoleksiAdmin(admin.ModelAdmin):
    list_display = ['nama_koleksi', 'gambar', 'deskripsi']

admin.site.register(Koleksi, KoleksiAdmin)



# --------------RATING------------------
from website_app.models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ['bintang', 'pesan', 'kesan']
    
admin.site.register(Rating, RatingAdmin)


from .models import TentangMuseum

@admin.register(TentangMuseum)
class TentangMuseumAdmin(admin.ModelAdmin):
    list_display = ('sejarah',  'gambar_museum', 'visi_misi', 'gambar_struktur_organisasi','alamat_museum', 'email_museum', 'nomor_hp', 'instagram')
