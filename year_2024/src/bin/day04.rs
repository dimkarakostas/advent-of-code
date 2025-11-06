use std::time::Instant;
use std::io;
use year_2024::{read_lines, count_lines_in_file, count_first_line_length};

fn main() -> io::Result<()> {
    let input_filename = "data/input04";

    let rows = count_lines_in_file(input_filename)?;
    let cols = count_first_line_length(input_filename)?;

    let mut input_table: Vec<Vec<char>> = vec![vec!['.'; cols]; rows];

    if let Ok(lines) = read_lines(input_filename) {
        for (row_idx, line) in lines.map_while(Result::ok).enumerate() {
            for (col_idx, character) in line.chars().enumerate() {
                input_table[row_idx][col_idx] = character;
            }
        }
    }

    let now = Instant::now();
    let mut xmas_count = 0;
    for x in 0..rows {
        for y in 0..cols {
            if input_table[x][y] == 'X' {
                if x < rows-3 && input_table[x+1][y] == 'M' && input_table[x+2][y] == 'A' && input_table[x+3][y] == 'S' {
                    xmas_count += 1;
                }
                if y < cols-3 && input_table[x][y+1] == 'M' && input_table[x][y+2] == 'A' && input_table[x][y+3] == 'S' {
                    xmas_count += 1;
                }
                if x > 2 && input_table[x-1][y] == 'M' && input_table[x-2][y] == 'A' && input_table[x-3][y] == 'S' {
                    xmas_count += 1;
                }
                if y > 2 && input_table[x][y-1] == 'M' && input_table[x][y-2] == 'A' && input_table[x][y-3] == 'S' {
                    xmas_count += 1;
                }
                if x < rows-3 && y < cols - 3 && input_table[x+1][y+1] == 'M' && input_table[x+2][y+2] == 'A' && input_table[x+3][y+3] == 'S' {
                    xmas_count += 1;
                }
                if x < rows-3 && y > 2 && input_table[x+1][y-1] == 'M' && input_table[x+2][y-2] == 'A' && input_table[x+3][y-3] == 'S' {
                    xmas_count += 1;
                }
                if x > 2 && y < cols-3 && input_table[x-1][y+1] == 'M' && input_table[x-2][y+2] == 'A' && input_table[x-3][y+3] == 'S' {
                    xmas_count += 1;
                }
                if x > 2 && y > 2 && input_table[x-1][y-1] == 'M' && input_table[x-2][y-2] == 'A' && input_table[x-3][y-3] == 'S' {
                    xmas_count += 1;
                }
            }
        }
    }

    println!("Part 1: {} ({:.2?})", xmas_count, now.elapsed());

    let now = Instant::now();
    let mut mas_count = 0;
    for x in 1..rows-1 {
        for y in 1..cols-1 {
            if input_table[x][y] == 'A' {
                if input_table[x-1][y-1] == 'M' && input_table[x+1][y+1] == 'S' && input_table[x-1][y+1] == 'M' && input_table[x+1][y-1] == 'S' {
                    mas_count += 1;
                }
                if input_table[x-1][y-1] == 'M' && input_table[x+1][y+1] == 'S' && input_table[x+1][y-1] == 'M' && input_table[x-1][y+1] == 'S' {
                    mas_count += 1;
                }
                if input_table[x+1][y+1] == 'M' && input_table[x-1][y-1] == 'S' && input_table[x-1][y+1] == 'M' && input_table[x+1][y-1] == 'S' {
                    mas_count += 1;
                }
                if input_table[x+1][y+1] == 'M' && input_table[x-1][y-1] == 'S' && input_table[x+1][y-1] == 'M' && input_table[x-1][y+1] == 'S' {
                    mas_count += 1;
                }
            }
        }
    }

    println!("Part 2: {} ({:.2?})", mas_count, now.elapsed());

    Ok(())
}
