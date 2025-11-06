use std::time::Instant;
use year_2024::read_lines;
use regex::Regex;

fn main() {
    let input_filename = "data/input03";

    let now = Instant::now();
    let mut first_result = 0;
    let mut second_result = 0;
    if let Ok(lines) = read_lines(input_filename) {
        let mut enabled = true;
        for line in lines.map_while(Result::ok) {
            let re = Regex::new(r"mul\((?P<x>\d+),(?P<y>\d+)\)").unwrap();
            for caps in re.captures_iter(&line) {
                let x: i32 = caps["x"].parse().unwrap();
                let y: i32 = caps["y"].parse().unwrap();
                first_result += x * y;
            }

            let re = Regex::new(r"mul\((?P<x>\d+),(?P<y>\d+)\)|(?P<off>don't\(\))|(?P<on>do\(\))").unwrap();
            for caps in re.captures_iter(&line) {
                if caps.name("off").is_some() {
                    enabled = false;
                }
                else if caps.name("on").is_some() {
                    enabled = true;
                }
                else if enabled && caps.name("x").is_some() {
                    let x: i32 = caps["x"].parse().unwrap();
                    let y: i32 = caps["y"].parse().unwrap();
                    second_result += x * y;
                }
            }
        }
    }

    println!("Part 1: {} ({:.2?})", first_result, now.elapsed());
    println!("Part 2: {} ({:.2?})", second_result, now.elapsed());
}
