use std::time::Instant;
use std::io;
use year_2025::{read_lines};

fn run(input_filename: &str, num_of_digits: usize) -> usize {
    let mut output: usize = 0;
    if let Ok(lines) = read_lines(input_filename) {
        for mut line in lines.map_while(Result::ok) {
            let mut digits: Vec<usize> = vec![];

            for digit_idx in 0..num_of_digits {
                for n in (0..10).rev() {
                    if let Some(pos) = line.chars().position(|c| c == std::char::from_digit(n, 10).unwrap()) {
                        if pos < line.chars().count()-(num_of_digits-1-digit_idx) {
                            digits.push(n.try_into().unwrap());
                            line = (&line[pos+1..]).to_string();
                            break;
                        }
                    } 
                }
            }

            for (idx, digit) in digits.into_iter().enumerate() {
                output += 10_usize.pow((num_of_digits-1-idx).try_into().unwrap()) * digit;
            }
        }
    }
    output
}

fn main() -> io::Result<()> {
    let input_filename = "data/input03";

    let mut now = Instant::now();

    let part_1 = run(&input_filename, 2);
    println!("Part 1: {} ({:.2?})", part_1, now.elapsed());

    now = Instant::now();
    let part_2 = run(&input_filename, 12);
    println!("Part 2: {} ({:.2?})", part_2, now.elapsed());

    Ok(())
}
