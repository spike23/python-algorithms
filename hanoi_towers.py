

def solve_hanoi(height, f_disk, t_disk, w_disk):
    if height >= 1:
        solve_hanoi(height - 1, f_disk, w_disk, t_disk )
        print(f"Move disk from {f_disk} to {t_disk}")
        solve_hanoi(height - 1, w_disk, t_disk, f_disk)


solve_hanoi(3, 'a', 'b', 'c')
