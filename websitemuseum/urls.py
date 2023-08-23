from django.contrib import admin
from django.urls import path
from website_app.views import *
from django.contrib.auth.views import LoginView, LogoutView
from user_app.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'website_app'

urlpatterns = [
    # Bagian admin
    path('admin/', admin.site.urls),
    path('menu_admin/', menu_admin, name='menu_admin'),
    
    path('loginadmin/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Daftar Pengunjung
    path('daftar_pengunjung/', daftar_pengunjung, name='daftar_pengunjung'),
    path('tambah_pengunjung/', tambah_pengunjung, name='tambah_pengunjung'),
    path('edit_pengunjung/<int:id_daftar_pengunjung>/', edit_pengunjung, name='edit_pengunjung'),
    path('hapus_pengunjung/<int:id_daftar_pengunjung>/', hapus_pengunjung, name='hapus_pengunjung'),

    # Laporan
    path('kelola_laporan/', kelola_laporan, name='kelola_laporan'),
    path('cetak-laporan/', cetak_laporan, name='cetak_laporan'),
    path('tampil_data_filter/',tampil_data_filter, name='tampil_data_filter'),
    # path('tambah_laporan/', tambah_laporan, name='tambah_laporan'),

    # Kelola Berita
    path('kelola_berita/', kelola_berita, name='kelola_berita'),
    path('tambah_berita/', tambah_berita, name='tambah_berita'),
    path('edit_berita/<int:id_berita>/', edit_berita, name='edit_berita'),
    path('hapus_berita/<int:id_berita>/', hapus_berita, name='hapus_berita'),

    
    # Daftar Koleksi
    path('kelola_koleksi/', kelola_koleksi, name='kelola_koleksi'),
    path('tambah_koleksi/', tambah_koleksi, name='tambah_koleksi'),
    path('edit_koleksi/<int:id_koleksi>/', edit_koleksi, name='edit_koleksi'),
    path('hapus_koleksi/<int:id_koleksi>/', hapus_koleksi, name='hapus_koleksi'),
    path('qr_code/', qr_code, name='qr_code'),

    
    # Kelola Rating
    path('kelola-rating/', kelola_rating, name='kelola_rating'),
    path('tambah-rating/', tambah_rating, name='tambah_rating'),
    path('hapus_rating/<int:id_rating>/', hapus_rating, name='hapus_rating'),

    # Kelola Tentang museum
    path('kelola_tentangmuseum/', kelola_tentangmuseum, name='kelola_tentangmuseum'),
    path('edit_tentangmuseum/<int:id_tentangmuseum>/', edit_tentangmuseum, name='edit_tentangmuseum'),
    
    #QR CODE
    path('generate_qr_code/<int:id>/', generate_qr_code, name='generate_qr_code'),
    path('print_qrcode/', print_qrcode, name='print_qrcode'),

    # Kelola Tentang museum
    path('kelola_booking/', kelola_booking, name='kelola_booking'),
    path('tambah_booking/', tambah_booking, name='tambah_booking'),
    path('edit_booking/<int:id_booking>/', edit_booking, name='edit_booking'),
    path('hapus_booking/<int:id_booking>/', hapus_booking, name='hapus_booking'),
    
    # user
    path('', index, name='index'),
    path('tentangmuseum/', tentangmuseum, name='tentangmuseum'),
    path('berita/', berita, name='berita'),
    path('koleksi/', koleksi, name='koleksi'),
    path('selamat/', selamat, name='selamat'),
    path('terimakasih/', terimakasih, name='terimakasih'),
    path('berita_deskripsi/<int:id_berita>/', berita_deskripsi, name='berita_deskripsi'),
    path('deskripsi/<int:id_koleksi>/', deskripsi, name='deskripsi'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



