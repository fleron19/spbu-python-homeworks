def n_queens_bitmask_complete(n):
    def solve(row, cols_mask, diag1_mask, diag2_mask, current_solution, all_solutions):
        if row == n:
            all_solutions.append(current_solution[:])
            return

        available_positions = ~(cols_mask | diag1_mask | diag2_mask) & ((1 << n) - 1)
        while available_positions:
            position = available_positions & -available_positions
            
            col = (position.bit_length() - 1)
            
            current_solution.append(col)
            
            solve(
                row + 1,
                cols_mask | position,  
                (diag1_mask | position) << 1,  
                (diag2_mask | position) >> 1,
                current_solution,
                all_solutions
            )
            
            current_solution.pop()
            
            available_positions -= position
    
    all_solutions = []
    solve(0, 0, 0, 0, [], all_solutions)
    return all_solutions


print(len((n_queens_bitmask_complete(int(input())))))
