import requests

# Ganti dengan URL yang sesuai
url = 'http://127.0.0.1:8000/produk/produk/'

# ID produk yang ingin dihapus
produk_id = 1  # Ganti dengan ID yang sesuai

# Mengirim permintaan DELETE
response = requests.delete(f'{url}{produk_id}/')

if response.status_code == 204:
    print('Produk berhasil dihapus')
else:
    print('Gagal menghapus produk')
