// Mengambil data pengunjung dari daftar_pengunjung menggunakan AJAX
fetch('/url/daftar_pengunjung/')
  .then(response => response.json())
  .then(data => {
    // Proses data yang diterima dari server
    var data_pengunjung = [0, 0, 0]; // Inisialisasi data pengunjung untuk kategori siswa, mahasiswa, dan umum

    // Loop melalui data pengunjung dan menghitung jumlah pengunjung berdasarkan kategori
    for (var i = 0; i < data.length; i++) {
      var kategori = data[i].kategori;
      var jumlah = parseFloat(data[i].jumlah);

      // Menambahkan jumlah pengunjung ke kategori yang sesuai
      if (kategori === 'siswa') {
        data_pengunjung[0] += jumlah;
      } else if (kategori === 'mahasiswa') {
        data_pengunjung[1] += jumlah;
      } else if (kategori === 'umum') {
        data_pengunjung[2] += jumlah;
      }
    }

    // Konfigurasi dan menggambar chart menggunakan Chart.js
    const ctx1 = document.getElementById('chart-1').getContext('2d');
    const myChart = new Chart(ctx1, {
      type: 'bar',
      data: {
        labels: ['Siswa', 'Mahasiswa', 'Umum'],
        datasets: [{
          label: 'Jumlah Pengunjung',
          data: data_pengunjung,
          backgroundColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
          ],
        }]
      },
      options: {
        responsive: true,
      },
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });



// static/js/chart.js
// const ctx1 = document.getElementById('chart-1').getContext('2d');
// const myChart = new Chart(ctx1, {
//     type: 'bar',
//     data: {
//         labels: ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Desember'],
//         datasets: [{
//             label: 'ABSENSI PERBULAN',
//             data: [
//               {% for bulan in data_pengunjung %}
//                   {{ bulan.jumlah }}{% if not forloop.last %},{% endif %}
//               {% endfor %}
//             ],
//             backgroundColor: [
//                'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//             ],
//         }]
//     },
//     options: {
//         responsive: true,
//     },
// });




// Tangkap elemen canvas
const ctx = document.getElementById('myChart').getContext('2d');

// Buat grafik menggunakan Chart.js
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Label 1', 'Label 2', 'Label 3'],
    datasets: [{
      label: 'Data',
      data: [10, 20, 30],
      backgroundColor: 'rgba(25, 104, 214, 0.5)',
      borderColor: 'rgba(25, 104, 214, 1)',
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});






