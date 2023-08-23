from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.db import connection   
from django.db.models import Q
from django.contrib.auth import authenticate, login 
from .forms import formlogin
from django.db.models import F
from django.core.paginator import Paginator
from django.db.models import Count
import re
from website_app.models import *
from website_app.forms import *
import io
from docx import Document
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph 
from openpyxl import Workbook
import qrcode
from io import BytesIO
from django.contrib import messages









# -----------------MENU ADMIN---------------------
from datetime import datetime

@login_required
def menu_admin(request):
    if request.method == 'POST':
        tanggal_awal = request.POST.get('tanggal_awal')
        tanggal_akhir = request.POST.get('tanggal_akhir')

        if tanggal_awal and tanggal_akhir:
            pengunjung = Pengunjung.objects.filter(tanggal__range=[tanggal_awal, tanggal_akhir]).values('kategori').annotate(jumlah=Count('kategori'))
        else:
            pengunjung = Pengunjung.objects.values('kategori').annotate(jumlah=Count('kategori'))
    else:
        pengunjung = Pengunjung.objects.values('kategori').annotate(jumlah=Count('kategori'))

    total_pengunjung = Pengunjung.objects.aggregate(total_jumlah=Sum('jumlah'))
    total_koleksi = Koleksi.objects.aggregate(total_jumlah=Count('nama_koleksi'))
    total_berita = Berita.objects.count()
    total_rating = Rating.objects.count()
    
    context = {
        'pengunjung_per_kategori': pengunjung,
        'total_pengunjung': total_pengunjung['total_jumlah'] if total_pengunjung['total_jumlah'] else 0,
        'total_koleksi': total_koleksi['total_jumlah'],
        'total_berita': total_berita,
        'total_rating': total_rating
    }

    return render(request, 'menu_admin.html', context)






# ----------------DAFTAR PENGUNJUNG---------------------
from website_app.models import Pengunjung
from website_app.models import Sum
from website_app.forms import PengunjungForm


@login_required
def daftar_pengunjung(request):
    pengunjung = Pengunjung.objects.all()
    
    total_pengunjung = Pengunjung.objects.aggregate(total_jumlah=Sum('jumlah'))

    context = {
        'pengunjung': pengunjung,
        'total_pengunjung': total_pengunjung['total_jumlah'] if total_pengunjung['total_jumlah'] else 0
    }
    return render(request, 'daftar_pengunjung.html', context)

@login_required
def edit_pengunjung(request, id_daftar_pengunjung):
    pengunjung = get_object_or_404(Pengunjung, id_daftar_pengunjung=id_daftar_pengunjung)
    if request.method == 'POST':
        form = PengunjungForm(request.POST, instance=pengunjung)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pengunjung berhasil diubah.')
            return redirect('daftar_pengunjung')
    else:
        form = PengunjungForm(instance=pengunjung)
    
    context = {'form': form}
    return render(request, 'edit_pengunjung.html', context)


@login_required
def hapus_pengunjung(request, id_daftar_pengunjung):
    pengunjung = get_object_or_404(Pengunjung, id_daftar_pengunjung=id_daftar_pengunjung)
    pengunjung.delete()
    return redirect('daftar_pengunjung')



# ----------------KELOLA BERITA--------------------
@login_required
def kelola_berita(request):
    berita = Berita.objects.all()
    total_berita = Berita.objects.aggregate(total_jumlah=Count('judul'))
    
    context = {
        'berita': berita,  # Menggunakan page_obj sebagai konteks untuk template
        'total_berita': total_berita['total_jumlah']
    }
    return render(request, 'kelola_berita.html', context)


@login_required
def tambah_berita(request):
    if request.method == 'POST':
        form = BeritaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berita Berhasil Ditambahkan.')
            return redirect('kelola_berita')
    else:
        form = BeritaForm()
    
    context = {'form': form}
    return render(request, 'tambah_berita.html', context)

@login_required
def edit_berita(request, id_berita):
    berita = get_object_or_404(Berita, id_berita=id_berita)
    if request.method == 'POST':
        form = BeritaForm(request.POST, request.FILES, instance=berita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Berita berhasil diperbarui.')
            return redirect('kelola_berita')
    else:
        form = BeritaForm(instance=berita)
    
    context = {'form': form}
    return render(request, 'edit_berita.html', context)


@login_required
def hapus_berita(request, id_berita):
    berita = get_object_or_404(Berita, id_berita=id_berita)
    berita.delete()
  
    return redirect('kelola_berita')

# ----------------KELOLA KOLEKSI-------------------

@login_required
def kelola_koleksi(request):
    koleksi_list = Koleksi.objects.all()
    total_koleksi = Koleksi.objects.aggregate(total_jumlah=Count('nama_koleksi'))

    context = {
        'koleksi_list': koleksi_list,
        'total_koleksi': total_koleksi['total_jumlah']
    }
    
    return render(request, 'kelola_koleksi.html', context)

@login_required
def tambah_koleksi(request):
    if request.method == 'POST':
        form = KoleksiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Koleksi berhasil ditambahkan.')
            return redirect('kelola_koleksi')
    else:
        form = KoleksiForm()
    
    context = {'form': form}
    return render(request, 'tambah_koleksi.html', context)

@login_required
def edit_koleksi(request, id_koleksi):
    koleksi = get_object_or_404(Koleksi, id_koleksi=id_koleksi)
    if request.method == 'POST':
        form = KoleksiForm(request.POST, request.FILES, instance=koleksi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Koleksi berhasil diubah.')
            return redirect('kelola_koleksi')
    else:
        form = KoleksiForm(instance=koleksi)
    
    context = {'form': form}
    return render(request, 'edit_koleksi.html', context)


@login_required
def hapus_koleksi(request, id_koleksi):
    koleksi = get_object_or_404(Koleksi, id_koleksi=id_koleksi)
    koleksi.delete()
    return redirect('kelola_koleksi')



#-----------------------SUARA--------------------
def deskripsi(request, id_koleksi):
    koleksi = Koleksi.objects.get(id_koleksi=id_koleksi)

    context = {
        'koleksi': koleksi
    }

    return render(request, 'deskripsi.html', context)

# ============== QR CODE ======================
@login_required
def qr_code(request):
    koleksi_list = Koleksi.objects.all()
    context = {
        'koleksi_list': koleksi_list
    }
    return render(request, 'qr_code.html', context)


@login_required
def generate_qr_code(request, id):
    # Mendapatkan URL halaman detail
    detail_url = request.build_absolute_uri('/detail/' + str(id))

    # Membuat objek QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(detail_url)
    qr.make(fit=True)

    # Membuat gambar QR code
    qr_image = qr.make_image(fill="black", back_color="white")

    # Simpan gambar ke dalam byte buffer
    qr_byte_buffer = BytesIO()
    qr_image.save(qr_byte_buffer, format='PNG')
    qr_byte_buffer.seek(0)

    # Menyajikan gambar sebagai response
    response = HttpResponse(content_type="image/png")
    response.write(qr_byte_buffer.getvalue())

    return response

# ========  PRINT QR CODE ======
@login_required
def print_qrcode(request):
    qr_code_data = request.GET.get('qr_code_data', '')

    # Membuat objek QR code menggunakan library qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(qr_code_data)
    qr.make(fit=True)

    # Membuat gambar QR code dalam format PNG
    qr_image = qr.make_image(fill="black", back_color="white")

    # Simpan gambar ke dalam byte buffer
    image_buffer = BytesIO()
    qr_image.save(image_buffer, format='PNG')
    image_buffer.seek(0)

    # Menyajikan gambar sebagai respons untuk diunduh
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="qr_code.png"'
    response.write(image_buffer.getvalue())
    return response 


# -------------- LAPORAN -----------------
from django.http import HttpResponse
from reportlab.lib.styles import ParagraphStyle
from datetime import datetime

@login_required
def kelola_laporan(request):
    search_query = request.GET.get('search', '')  # Ambil nilai search_query dari URL parameter 'search'

    # Mengambil semua objek DaftarPengunjung dari database
    pengunjung = Pengunjung.objects.all()

    if search_query:
        pengunjung = pengunjung.filter(nama__icontains=search_query)  # Filter data berdasarkan nama dengan memanfaatkan search_query

    context = {
        'pengunjung': pengunjung,
        'search_query': search_query,
    }

    #  membuat string HTML sebagai laporan
    laporan_html = "<h1>Laporan Daftar Pengunjung</h1>"
    laporan_html += "<table>"
    laporan_html += "<tr><th>NO</th><th>TANGGAL</th><th>NAMA</th><th>KATEGORI</th><th>JUMLAH</th><th>ASAL</th></tr>"

    for index, peng in enumerate(pengunjung, start=1):
        laporan_html += f"<tr><td>{index}</td><td>{peng.tanggal}</td><td>{peng.nama}</td><td>{peng.kategori}</td><td>{peng.jumlah}</td><td>{peng.asal}</td></tr>"

    laporan_html += "</table>"

    context['laporan_html'] = laporan_html

    if 'cetak' in request.GET:  # Jika ada parameter 'cetak' pada URL
        return render(request, 'laporan_cetak.html', context)  # Render halaman cetak laporan
    else:
        return render(request, 'kelola_laporan.html', context)  # Render halaman laporan


    
@login_required
def cetak_laporan(request):
    search_query = request.GET.get('search', '')
    filter_tanggal_awal = request.POST.get('filter_tanggal_awal')
    filter_tanggal_akhir = request.POST.get('filter_tanggal_akhir')
    
    # Periksa apakah tanggal awal dan tanggal akhir telah dipilih
    if not filter_tanggal_awal or not filter_tanggal_akhir:
        messages.error(request, 'Pilih tanggal terlebih dahulu.')
        return render(request, 'kelola_laporan.html', {'pengunjung': Pengunjung.objects.all(), 'search_query': search_query})

    pengunjung = Pengunjung.objects.filter(tanggal__range=[filter_tanggal_awal, filter_tanggal_akhir])
    search_results = pengunjung

    if request.method == 'POST':
        format_laporan = request.POST.get('format')


        if format_laporan == 'pdf':
            # Create a BytesIO buffer for the PDF document
            buffer = io.BytesIO()

            # Create a new PDF document using ReportLab
            pdf = SimpleDocTemplate(buffer, pagesize=letter)

            # Define table headers
            table_headers = ['NO', 'TANGGAL', 'NAMA', 'KATEGORI', 'JUMLAH', 'ASAL']

            # Create table data
            table_data = [table_headers]  # Add headers as the first row
            for i, item in enumerate(search_results, start=1):
                row = [str(i), str(item.tanggal), item.nama, item.kategori, str(item.jumlah), item.asal]
                table_data.append(row)

            # Define table style
            table_style = TableStyle([
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Mengubah warna grid menjadi hitam
            ])

            # MEMBUAT JUDUL TABEL
            elements = []
            tahun_sekarang = datetime.now().year
            title = Paragraph(f"LAPORAN DAFTAR PENGUNJUNG TAHUN {tahun_sekarang}", 
                              style=ParagraphStyle(name='title', fontSize=18, alignment=1, spaceAfter=10, leading=18))
            elements.append(title)
            table = Table(table_data)
            table.setStyle(table_style)
            elements.append(table)

            # Build the PDF document
            pdf.build(elements)

            # Set the buffer's file pointer at the beginning
            buffer.seek(0)

            # Create the HTTP response as a PDF file
            response = FileResponse(buffer, as_attachment=True, filename='laporan.pdf')
            return response

        elif format_laporan == 'word':
            # Create a new Word document
            document = Document()

            # Add a table to the document
            table = document.add_table(rows=1, cols=6)
            table.style = 'Table Grid'

            # Define table headers
            table_headers = ['NO', 'TANGGAL', 'NAMA', 'KATEGORI', 'JUMLAH', 'ASAL']

            # Add table headers
            header_cells = table.rows[0].cells
            for i in range(len(table_headers)):
                header_cells[i].text = table_headers[i]

            # Add data rows to the table
            for i, item in enumerate(search_results, start=1):
                row_cells = table.add_row().cells
                row_cells[0].text = str(i)
                row_cells[1].text = str(item.tanggal)
                row_cells[2].text = item.nama
                row_cells[3].text = item.kategori
                row_cells[4].text = str(item.jumlah)
                row_cells[5].text = item.asal

            # Create a BytesIO buffer for the document
            buffer = io.BytesIO()

            # Save the document to the buffer
            document.save(buffer)

            # Set the buffer's file pointer at the beginning
            buffer.seek(0)

            # Create the HTTP response as a Word document
            response = FileResponse(buffer, as_attachment=True, filename='laporan.docx')
            return response
        
        elif format_laporan == 'excel':
            # Create a new Workbook
            workbook = Workbook()

            # Create a new sheet in the Workbook
            sheet = workbook.active

            # Set the title of the sheet
            tahun_sekarang = datetime.now().year
            sheet.title = f"Laporan {tahun_sekarang}"

            # Add table headers
            table_headers = ['NO', 'TANGGAL', 'NAMA', 'KATEGORI', 'JUMLAH', 'ASAL']
            sheet.append(table_headers)

            # Add data rows
            for i, item in enumerate(search_results, start=1):
                row = [
                    i,
                    str(item.tanggal),
                    item.nama,
                    item.kategori,
                    item.jumlah,
                    item.asal,
                ]
                sheet.append(row)

            # Create an in-memory file-like object for the workbook
            file = io.BytesIO()

            # Save the workbook to the in-memory file-like object
            workbook.save(file)

            # Rewind the file-like object to the beginning
            file.seek(0)

            # Create a FileResponse with the in-memory file-like object
            response = FileResponse(file, as_attachment=True, filename='laporan.xlsx')

            # Set the content type for the response
            response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            return response
    
    return render(request, 'kelola_laporan.html', {'pengunjung': search_results, 'search_query': search_query})

@login_required
def tampil_data_filter(request):
    if request.method == 'GET':
        filter_tanggal_awal = request.GET.get('filter_tanggal_awal')
        filter_tanggal_akhir = request.GET.get('filter_tanggal_akhir')

        # Cek apakah tanggal awal dan akhir sudah dipilih
        if not filter_tanggal_awal or not filter_tanggal_akhir:
            messages.error(request, 'Pilih tanggal terlebih dahulu.')
            return render(request, 'kelola_laporan.html', {'pengunjung': Pengunjung.objects.all()})

        pengunjung = Pengunjung.objects.filter(tanggal__range=[filter_tanggal_awal, filter_tanggal_akhir])
        context = {'pengunjung': pengunjung}
        return render(request, 'kelola_laporan.html', context)
    else:
        # Jika metode HTTP bukan GET, tampilkan laporan tanpa filter
        pengunjung = Pengunjung.objects.all()
        context = {'pengunjung': pengunjung}
        return render(request, 'kelola_laporan.html', context)
    
# =============== KELOLA RATING ======================
from django.contrib.admin.views.decorators import staff_member_required
from user_app.forms import RatingForm
from website_app.models import Rating

@staff_member_required
def kelola_rating(request):
    rating_counts = Rating.objects.values('bintang').annotate(count=Count('bintang'))
    ratings = Rating.objects.all()
    return render(request, 'kelola_rating.html', {'rating_counts': rating_counts, 'ratings': ratings})


@login_required
def hapus_rating(request, id_rating):
    rating = get_object_or_404(Rating, id_rating=id_rating)
    rating.delete()
    return redirect('kelola_rating')



# ------------------ LOGIN ---------------------

@login_required
def login_view(request):
    form = formlogin()
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('menu_admin')
    return render(request, 'login.html')




# ------------------ TENTANG MUSEUM---------------------
from .models import TentangMuseum
from .forms import TentangMuseumForm

def kelola_tentangmuseum(request):
    informasi = TentangMuseum.objects.first()
    
    if request.method == 'POST':
        informasi = TentangMuseumForm(request.POST, request.FILES, instance=informasi)
        if informasi.is_valid():
            informasi.save()
            return redirect('kelola_tentangmuseum')
    else:
        tentangmuseum = TentangMuseumForm(instance=informasi)
    
    return render(request, 'kelola_tentangmuseum.html', {'tentangmuseum': tentangmuseum, 'informasi': informasi})



def edit_tentangmuseum(request, id_tentangmuseum):
    informasi = get_object_or_404(TentangMuseum, pk=id_tentangmuseum)
    if request.method == 'POST':
        informasi = TentangMuseumForm(request.POST, request.FILES, instance=informasi)
        if informasi.is_valid():
            informasi.save()
            messages.success(request, 'Data telah berhasil diubah.')
            return redirect('kelola_tentangmuseum')
    else:
        informasi = TentangMuseumForm(instance=informasi)
    return render(request, 'edit_tentangmuseum.html', {'informasi': informasi})


# ------------------ booking---------------------

from .forms import BookingForm  # Import the BookingForm

# ...

@login_required
def kelola_booking(request):    
    bookings = Booking.objects.all()
    context = {'bookings': bookings}
    return render(request, 'kelola_booking.html', context)


def edit_booking(request, id_booking):
    booking = get_object_or_404(Booking, id_booking=id_booking)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pengunjung berhasil diubah.')
            return redirect('kelola_booking')
    else:
        form = BookingForm(instance=booking)
    
    context = {'form': form}
    return render(request, 'edit_booking.html', context)

@login_required
def hapus_booking(request, id_booking):
    booking = get_object_or_404(Booking, id_booking=id_booking)
    booking.delete()
    return redirect('kelola_booking')