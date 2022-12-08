

nama = input("siapa nama mu?\n>> ")
def main():
    print("""
  _________            .__    .___                         .___ 
 /   _____/ ________ __|__| __| _/_  _  _______ _______  __| _/ 
 \_____  \ / ____/  |  \  |/ __ |\ \/ \/ /\__  \\_  __ \/ __ |  
 /        < <_|  |  |  /  / /_/ | \     /  / __ \|  | \/ /_/ |  
/_______  /\__   |____/|__\____ |  \/\_/  (____  /__|  \____ |  
        \/    |__|             \/              \/           \/  
                                                                                
    """)
    print("hallo",nama,"selamat datang di toko kami")
    print('''
    ┌────┬─────────────┬─────────┐
    │ no │   makanan   │  harga  │
    ├────┼─────────────┼─────────┤
    │  1 │ ayam bakar  │ 100.000 │
    │  2 │ opor ayam   │  80.500 │
    │  3 │ rendang     │ 300.000 │
    │  4 │ nasi padang │  30.000 │
    │  5 │ nasi kuning │  12.000 │
    └────┴─────────────┴─────────┘
    ''')
    pilihan = int(input("masukan pilihan mu\n>> "))

main()
