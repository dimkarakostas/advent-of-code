use std::time::Instant;
use std::io;
use year_2025::{read_lines};

fn main() -> io::Result<()> {
    let input_filename = "data/input06";

    let mut now = Instant::now();

    let mut object_vector = Vec::new();
    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            let row: Vec::<String> = line.split_whitespace().map(|x| x.to_string()).collect();
            object_vector.push(row);
        }
    }

    let mut part_1 = 0;

    for problem_col in 0..object_vector[0].len() {
        let mut problem_elements: Vec<i128> = Vec::new();
        for row in 0..object_vector.len()-1 {
            problem_elements.push(object_vector[row][problem_col].parse::<i128>().unwrap());
        }
        let operator = object_vector[object_vector.len()-1][problem_col].clone();
        if operator == "+" {
            part_1 += problem_elements.iter().sum::<i128>();
        }
        else {
            part_1 += problem_elements.iter().product::<i128>();
        }
    }

    println!("Part 1: {} ({:.2?})", part_1, now.elapsed());

    now = Instant::now();

    let mut part_2 = 0;

    let mut matrix = Vec::new();
    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            let row: Vec<char> = line.chars().collect();
            matrix.push(row);
        }
    }

    let mut problem_limits: Vec<usize> = Vec::new();
    problem_limits.push(0);
    for col in 0..matrix[0].len() {
        if matrix.iter().all(|row| row[col].is_whitespace()) {
            problem_limits.push(col+1);
        }
    }
    problem_limits.push(matrix[0].len()+1);

    for problem_idx in 0..problem_limits.len()-1 {
        let start_col = problem_limits[problem_idx];
        let end_col = problem_limits[problem_idx+1]-1;

        let mut problem_elements: Vec<i128> = Vec::new();
        let mut operator: char = ' ';
        for col in start_col..end_col {
            let mut element_vector: Vec<char> = Vec::new();
            for row in 0..matrix.len() {
                if matrix[row][col] == '*' || matrix[row][col] == '+' {
                    operator = matrix[row][col];
                }
                else if matrix[row][col] != ' ' {
                    element_vector.push(matrix[row][col]);
                }
            }
            let s: String = element_vector.iter().collect();
            problem_elements.push(s.parse().unwrap());
        }
        if operator == '+' {
            part_2 += problem_elements.iter().sum::<i128>();
        }
        else {
            part_2 += problem_elements.iter().product::<i128>();
        }
    }

    println!("Part 2: {} ({:.2?})", part_2, now.elapsed());

    Ok(())
}
