use std::io;
use year_2024::{read_lines, count_lines_in_file};

fn main() -> io::Result<()> {
    let input_filename = "data/input01";

    let line_count = count_lines_in_file(input_filename)?;

    let mut first_col = vec![0; line_count];
    let mut second_col = vec![0; line_count];

    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            let parts = line.split_whitespace().collect::<Vec<&str>>();
            let left_num = parts[0].parse::<i32>().unwrap();
            first_col.push(left_num);
            let right_num: i32 = parts[1].parse().unwrap();
            second_col.push(right_num);
        }
    }

    first_col.sort();
    second_col.sort();

    let mut total_diff = 0;
    for (idx, left_num) in first_col.iter().enumerate() {
        let right_num = second_col[idx];
        let position_diff = left_num - right_num;
        total_diff += position_diff.abs();
    }

    println!("Part 1: {}", total_diff);

    first_col.dedup();

    let mut similarity_score = 0;
    for left_num in first_col.iter() {
        let right_col_count = second_col.iter().filter(|&n| *n == *left_num).count() as i32;
        similarity_score += left_num * right_col_count;
    }

    println!("Part 2: {}", similarity_score);

    Ok(())
}
