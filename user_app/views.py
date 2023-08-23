from django.shortcuts import render, get_object_or_404
from website_app.models import * 
from django.shortcuts import redirect
from website_app.forms import *
from django.core.paginator import Paginator
from website_app.models import Berita

#---------------- WEBSITE MUSEUM ------------------
def index(request):
    informasi =TentangMuseum.objects.all()
    context = {
        'informasi': informasi
    }
    return render(request, 'index.html', context)


def tentangmuseum(request):
    informasi =TentangMuseum.objects.all()
    context = {
        'informasi': informasi
    }
    return render(request, 'tentangmuseum.html', context)

# -------------------- BERITA ---------------------------
def berita(request):
    berita_list = Berita.objects.all()[:10] 
    informasi =TentangMuseum.objects.all()
    paginator = Paginator(berita_list, 12)  # Menentukan jumlah berita per halaman
    page_number = request.GET.get('page')  # Mengambil nomor halaman dari parameter URL
    page_obj = paginator.get_page(page_number)  # Mengambil objek halaman yang sesuai dengan nomor halaman

    context = {
        'page_obj': page_obj,
        'informasi': informasi
    }
    return render(request, 'berita.html', context)


def berita_deskripsi(request, id_berita):
    berita = Berita.objects.get(id_berita=id_berita)
    informasi =TentangMuseum.objects.all()
    context = {
        'berita': berita,
        'informasi': informasi
    }
    return render(request, 'berita_deskripsi.html', context)

# -------------------- KOLEKSI---------------------------
def koleksi(request):
    koleksi_list = Koleksi.objects.all() # Mengambil 10 data pertama
    informasi =TentangMuseum.objects.all()
    paginator = Paginator(koleksi_list, 20)  # Menentukan jumlah data per halaman
    page_number = request.GET.get('page')  # Mengambil nomor halaman dari parameter URL
    page_obj = paginator.get_page(page_number)  # Mengambil objek halaman yang sesuai dengan nomor halaman

    context = {
        'page_obj': page_obj,
        'informasi': informasi
    }
    return render(request, 'koleksi.html', context)


# ---------------- DAFTAR PENGUNJUNG ---------------------
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from website_app.forms import PengunjungForm

def tambah_pengunjung(request):
    if request.method == 'POST':
        form = PengunjungForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selamat')
    else:
        form = PengunjungForm()
    return render(request, 'pengunjung.html', {'form': form})


# ---------------- RATING ---------------------
from user_app.forms import RatingForm

def tambah_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('terimakasih')
    else:
        form = RatingForm()
    return render(request, 'tambah_rating.html', {'form': form})

# ---------------- SELAMAT ---------------------
def selamat(request):
    pengunjung = {
        'nama': request.POST.get('nama') if request.method == 'POST' else None
    }
    return render(request, 'selamat.html', {'pengunjung': pengunjung})

def terimakasih(request):
    return render(request, 'terimakasih.html')


# -------------BOOKING--------------
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from website_app.forms import BookingForm
from django.contrib import messages

def tambah_booking(request):
    if request.method == 'POST':
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'datamu sudah dibooking')
            return redirect('tambah_booking')
    else:
        form = BookingForm()
    return render(request, 'tambah_booking.html', {'form': form})