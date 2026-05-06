import os 
from flask import Flask, jsonify, request 
from flask_cors import CORS 
app = Flask(__name__) 
CORS(app) 
# ===================================================================== 
# DILARANG MENGUBAH ATAU MENG-HARDCODE BAGIAN INI! 
# ===================================================================== 
# Sistem akan otomatis membaca Environment Variables dari Azure ACI. 
# Jika kalian menulis nama langsung di sini, nilai otomatis dipotong. 

nama_owner = os.environ.get('NAMA_PRAKTIKAN', 'Misterius') 
nim_owner = os.environ.get('NIM_PRAKTIKAN', '00000000')

# =====================================================================
# BAGIAN INI BEBAS KALIAN MODIFIKASI SESUAI TEMA YANG KALIAN PILIH 
# =====================================================================

toko_buku_data = {
    "nama_toko": f"Bookstore Coding - {nama_owner}",
    "pemilik": nama_owner,
    "nim": nim_owner,
    "koleksi": ["Clean Code", "The Pragmatic Programmer", "Introduction to Algorithms"]
}

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify(toko_buku_data)

@app.route('/api/add-book', methods=['POST'])
def add_book():
    new_item = request.json.get('item')
    if new_item:
        toko_buku_data["koleksi"].append(new_item)
        return jsonify({"message": "Buku ditambahkan!", "koleksi": toko_buku_data["koleksi"]}), 201
    return jsonify({"error": "Data tidak valid"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)