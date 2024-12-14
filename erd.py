import pandas as pd
import networkx as nx

# Baca dataset laptop
df = pd.read_csv('laptop_prices.csv')

# Buat graph untuk ERD
G = nx.Graph()

# Definisikan entitas utama
entities = {
    'Laptop': ['Company', 'Product', 'TypeName', 'Inches', 'Screen', 
               'Touchscreen', 'IPSpanel', 'RetinaDisplay'],
    'Spesifikasi': ['Ram', 'CPU_company', 'CPU_model', 'CPU_freq', 
                    'PrimaryStorage', 'PrimaryStorageType', 
                    'SecondaryStorage', 'SecondaryStorageType', 
                    'GPU_company', 'GPU_model'],
    'Harga': ['Price_euros'],
    'Sistem Operasi': ['OS']
}

# Tambahkan node entitas
for entity, attributes in entities.items():
    G.add_node(entity, type='entity')
    for attr in attributes:
        G.add_node(attr, type='attribute')
        G.add_edge(entity, attr)

# Tambahkan relasi
G.add_edge('Laptop', 'Spesifikasi', relationship='memiliki')
G.add_edge('Laptop', 'Harga', relationship='punya')
G.add_edge('Laptop', 'Sistem Operasi', relationship='menggunakan')

# Simpan untuk gephi dengan versi GEXF yang didukung
nx.write_gexf(G, 'laptop_erd.gexf')

print("File ERD laptop_erd.gexf telah dibuat. Impor ke Gephi untuk visualisasi.")