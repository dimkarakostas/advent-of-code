use std::time::Instant;
use year_2024::read_lines;

fn check_safety(diffs: &Vec<i32>) -> bool {
    let all_pos = diffs.iter().all(|&x| x >= 1 && x <= 3);
    let all_neg = diffs.iter().all(|&x| x >= -3 && x <= -1);
    all_pos || all_neg
}

fn compute_diffs(parts: &Vec<&str>) -> Vec<i32> {
    let mut diffs = vec![];

    for idx in 0..(parts.len()-1) {
        let first_num = parts[idx].parse::<i32>().unwrap();
        let second_num = parts[idx+1].parse::<i32>().unwrap();
        diffs.push(first_num - second_num);
    }

    diffs
}

fn main() {
    let input_filename = "data/input02";

    let now = Instant::now();
    let mut safe_reports = 0;
    let mut dampened_safe_reports = 0;
    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            let parts = line.split_whitespace().collect::<Vec<&str>>();

            let diffs = compute_diffs(&parts);
            if check_safety(&diffs) {
                safe_reports += 1;
            }
            else {
                for idx in 0..parts.len() {
                    let new_parts = parts.iter()
                                            .enumerate()
                                            .filter(|(i, _)| *i != idx)
                                            .map(|(_, &x)| x)
                                            .collect();
                    let new_diffs = compute_diffs(&new_parts);

                    if check_safety(&new_diffs) {
                        dampened_safe_reports += 1;
                        break;
                    }
                }
            }
        }
    }

    println!("Part 1: {} ({:.2?})", safe_reports, now.elapsed());
    println!("Part 2: {} ({:.2?})", safe_reports + dampened_safe_reports, now.elapsed());
}
