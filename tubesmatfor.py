import math

# Format: [Sosmed, Game, Belajar]
data_mahasiswa = [
    [7, 2, 1], [7, 0 ,3], [6, 1, 5], [6, 3, 3], [3, 1, 1], [8, 1, 3], [4, 0, 3],
    [6, 1, 1], [5, 0, 0], [5, 4, 3], [5, 0, 3], [5, 1, 0], [8, 1, 3],
    [3, 2, 3], [4, 2, 2], [2, 0, 3], [5, 1, 3], [2, 3, 2], [6, 1, 2], 
    [6, 0, 6], [9, 0, 3], [6, 0, 3], [5, 1, 3], [9, 1, 1]
]

# PENENTUAN CENTROID AWAL (K=4)
centroids = [
    [9, 1, 1],  # C1
    [5, 4, 3],   # C2
    [6, 0, 6],  # C3 
    [3, 1, 1]    # C4
]

def hitung_jarak(titik1, titik2):
    # Rumus Euclidean Distance
    kembali = math.sqrt(
        (titik1[0] - titik2[0])**2 + 
        (titik1[1] - titik2[1])**2 + 
        (titik1[2] - titik2[2])**2
    )
    return kembali

def k_means(data, pusat_kelompok, max_iterasi=10):
    for i in range(max_iterasi):
        print(f"\n--- ITERASI {i+1} ---")
        
        # Penampung cluster
        clusters = [[] for _ in range(len(pusat_kelompok))]
        
        # LANGKAH A: ASSIGNMENT (Menentukan Cluster Terdekat)
        for mhs in data:
            jarak_ke_semua_centroid = [hitung_jarak(mhs, c) for c in pusat_kelompok]
            cluster_terdekat = jarak_ke_semua_centroid.index(min(jarak_ke_semua_centroid))
            clusters[cluster_terdekat].append(mhs)
        
        # Tampilkan jumlah anggota tiap cluster
        for j, c in enumerate(clusters):
            print(f"Cluster {j+1}: {len(c)} mahasiswa")

        # LANGKAH B: UPDATE CENTROID (Menghitung Rata-rata/Mean)
        new_centroids = []
        for j, group in enumerate(clusters):
            if not group: 
                new_centroids.append(pusat_kelompok[j])
                continue
            
            rata_sosmed = round(sum(m[0] for m in group) / len(group), 2)
            rata_game = round(sum(m[1] for m in group) / len(group), 2)
            rata_belajar = round(sum(m[2] for m in group) / len(group), 2)
            new_centroids.append([rata_sosmed, rata_game, rata_belajar])
        
        # Cek apakah centroid berubah
        if new_centroids == pusat_kelompok: 
            print("\nKONVERGEN! Centroid sudah tidak berubah lagi.")
            break
            
        pusat_kelompok = new_centroids
        print("Centroid Baru:", pusat_kelompok)

    return clusters, pusat_kelompok

hasil_cluster, centroid_final = k_means(data_mahasiswa, centroids)

for i in range(4):
    print(f"centroid ke {i + 1}: {centroid_final[i]}")