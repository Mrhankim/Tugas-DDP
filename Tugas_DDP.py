#Tugas 7 DDP
# Data pegawai
ar_pegawai = [
    {"nama":"Budi", "jabatan":"Manager", "agama":"Islam", "status":"Menikah"},
    {"nama":"Siti", "jabatan":"Asisten Manager", "agama":"Islam", "status":"Menikah"},
    {"nama":"I Gede", "jabatan":"Supervisor", "agama":"Hindu", "status":"Menikah"},
    {"nama":"Joko", "jabatan":"Staff", "agama":"Islam", "status":"Belum Menikah"},
    {"nama":"Alex", "jabatan":"Staff", "agama":"Kristen Protestan", "status":"Belum Menikah"}
]

# Gaji pokok berdasarkan jabatan
gapok_dict = {
    "Manager": 15000000,
    "Asisten Manager": 10000000,
    "Supervisor": 7000000,
    "Staff": 4000000
}

# Loop untuk menghasilkan slip gaji
for pegawai in ar_pegawai:
    nama = pegawai["nama"]
    jabatan = pegawai["jabatan"]
    agama = pegawai["agama"]
    status = pegawai["status"]

    # Menghitung komponen gaji
    gapok = gapok_dict[jabatan]
    tunjangan_jabatan = 0.3 * gapok
    bpjs = 0.1 * gapok
    tunjangan_keluarga = 0.1 * gapok if status == "Menikah" else 0
    gaji_kotor = gapok + tunjangan_jabatan + tunjangan_keluarga + bpjs
    
    # Menghitung zakat profesi
    zakat_profesi = 0
    if agama == "Islam" and gaji_kotor >= 7000000:
        zakat_profesi = 0.025 * gaji_kotor

    # Menghitung gaji bersih
    gaji_bersih = gaji_kotor - zakat_profesi

    # Mencetak slip gaji
    print("="*40)
    print("Slip Gaji Pegawai")
    print("="*40)
    print(f"Nama            : {nama}")
    print(f"Jabatan         : {jabatan}")
    print(f"Agama           : {agama}")
    print(f"Status          : {status}")
    print(f"Gaji Pokok      : Rp{gapok:,.0f}")
    print(f"Tunjangan Jabatan: Rp{tunjangan_jabatan:,.0f}")
    print(f"Tunjangan Keluarga: Rp{tunjangan_keluarga:,.0f}")
    print(f"BPJS            : Rp{bpjs:,.0f}")
    print(f"Gaji Kotor      : Rp{gaji_kotor:,.0f}")
    print(f"Zakat Profesi   : Rp{zakat_profesi:,.0f}")
    print(f"Gaji Bersih     : Rp{gaji_bersih:,.0f}")
    print("="*40)
