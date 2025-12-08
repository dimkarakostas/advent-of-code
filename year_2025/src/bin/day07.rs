use std::time::Instant;
use std::io;
use std::collections::VecDeque;
use year_2025::{read_lines, count_lines_in_file, count_first_line_length};

fn main() -> io::Result<()> {
    let input_filename = "data/input07";

    let rows = count_lines_in_file(input_filename)?;
    let cols = count_first_line_length(input_filename)?;

    let mut beam_positions: VecDeque<(usize, usize)> = VecDeque::new();
    let mut splitter_positions: Vec<(usize, usize)> = Vec::new();
    if let Ok(lines) = read_lines(input_filename) {
        for (row, line) in lines.map_while(Result::ok).enumerate() {
            for (col, character) in line.chars().enumerate() {
                if character == 'S' {
                    beam_positions.push_back((row, col));
                }
                else if character == '^' {
                    splitter_positions.push((row, col));
                }
            }
        }
    }

    let start_position = beam_positions[0];

    let mut now = Instant::now();

    let mut part_1 = 0;
    while beam_positions.iter().any(|&(a, _)| a != rows-1) {
        if let Some((row, col)) = beam_positions.pop_front() {
            if row < rows-1 {
                if splitter_positions.contains(&(row+1, col)) {
                    part_1 += 1;
                    if col < cols-1 {
                        if !beam_positions.contains(&(row+1, col+1)) {
                            beam_positions.push_back((row+1, col+1));
                        }
                    }
                    if col > 0 {
                        if !beam_positions.contains(&(row+1, col-1)) {
                            beam_positions.push_back((row+1, col-1));
                        }
                    }
                }
                else {
                    if !beam_positions.contains(&(row+1, col)) {
                        beam_positions.push_back((row+1, col));
                    }
                }
            }
        }
    }

    println!("Part 1: {} ({:.2?})", part_1, now.elapsed());

    now = Instant::now();

    let mut col_beams = vec![0usize; cols];
    col_beams[start_position.1] = 1;
    for row in 0..rows {
        let mut next_row_col_beams = vec![0usize; cols];
        for col in 0..cols {
            if col_beams[col] > 0 {
                if splitter_positions.contains(&(row+1, col)) {
                    next_row_col_beams[col-1] += col_beams[col];
                    next_row_col_beams[col+1] += col_beams[col];
                }
                else {
                    next_row_col_beams[col] += col_beams[col];
                }
            }
        }
        col_beams.clone_from(&next_row_col_beams);
    }

    println!("Part 2: {} ({:.2?})", col_beams.iter().sum::<usize>(), now.elapsed());

    Ok(())
}
