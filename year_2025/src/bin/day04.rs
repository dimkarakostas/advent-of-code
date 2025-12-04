use std::time::Instant;
use std::ops::Not;
use std::io;
use year_2025::{read_lines, count_lines_in_file, count_first_line_length};

fn check_if_eligible(table: &Vec<Vec<char>>, x: usize, y: usize) -> bool {
    let rows = table.len();
    let cols = table[0].len();
    let mut eligible = false;
    if table[x][y] == '@' {
        let mut adjacent_rolls = 0;
        for x_adj in 0..3 {
            for y_adj in 0..3 {
                if (x+x_adj > 0 && x+x_adj < rows+1) && (y+y_adj > 0 && y+y_adj < cols+1) && (x_adj == 1 && y_adj == 1).not() {
                    if table[x+x_adj-1][y+y_adj-1] == '@' {
                        adjacent_rolls += 1;
                    }
                }
            }
        }

        if adjacent_rolls < 4 {
            eligible = true;
        }
    }
    eligible
}

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

    let mut now = Instant::now();
    let mut roll_count = 0;
    for x in 0..rows {
        for y in 0..cols {
            if check_if_eligible(&input_table.clone(), x, y) {
                roll_count += 1;
            }
        }
    }

    println!("Part 1: {} ({:.2?})", roll_count, now.elapsed());

    now = Instant::now();
    roll_count = 0;
    loop {
        let mut roll_was_removed = false;
        for x in 0..rows {
            for y in 0..cols {
                if check_if_eligible(&input_table, x, y) {
                    roll_was_removed = true;
                    input_table[x][y] = '.';
                    roll_count += 1;
                }
            }
        }
        if !roll_was_removed {
            break;
        }
    }

    println!("Part 2: {} ({:.2?})", roll_count, now.elapsed());

    Ok(())
}
