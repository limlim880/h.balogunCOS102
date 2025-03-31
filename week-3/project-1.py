students = {
    "Evelyn": ["Female", 17, 5.5, 80], "Jessica": ["Female", 16, 6.0, 85],
    "Sointo": ["Female", 17, 5.4, 70], "Edith": ["Female", 18, 5.9, 76],
    "Liza": ["Female", 16, 5.5, 66], "Madonna": ["Female", 18, 5.6, 87],
    "Waje": ["Female", 17, 6.1, 95], "Tola": ["Female", 20, 6.0, 50],
    "Aisha": ["Female", 19, 5.7, 49], "Latifa": ["Female", 17, 5.5, 66],

    "Chinedu": ["Male", 19, 5.7, 74], "Liam": ["Male", 16, 5.9, 87],
    "Wale": ["Male", 18, 5.8, 75], "Gbenga": ["Male", 17, 6.1, 66],
    "Abiola": ["Male", 20, 5.9, 78], "Kola": ["Male", 19, 5.5, 87],
    "Kunle": ["Male", 16, 6.1, 98], "George": ["Male", 18, 5.4, 54],
    "Thomas": ["Male", 17, 5.8, 60], "Wesley": ["Male", 19, 5.7, 60]
}

print(f"{'Name':<10} {'Gender':<8} {'Age':<5} {'Height':<7} {'Score':<5}")
print("="*40)

for name, details in students.items():
    gender, age, height, score = details
    print(f"{name:<10} {gender:<8} {age:<5} {height:<7} {score:<5}")
