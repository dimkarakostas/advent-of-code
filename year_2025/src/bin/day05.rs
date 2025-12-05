use std::time::Instant;
use std::io;
use regex::Regex;
use year_2025::{read_lines};

fn main() -> io::Result<()> {
    let input_filename = "data/input05";

    let mut ingredients: Vec<i128> = Vec::new();
    let mut ranges: Vec<(i128, i128)> = Vec::new();

    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            if line.contains("-") {
                let re = Regex::new(r"(?P<start>\d+)-(?P<end>\d+)").unwrap();
                for caps in re.captures_iter(&line) {
                    ranges.push((caps["start"].parse().unwrap(), caps["end"].parse().unwrap()))
                }
            }
            else if line.chars().count() > 0 {
                ingredients.push(line.parse().unwrap());
            }
        }
    }

    let mut now = Instant::now();

    let mut part_1 = 0;
    for ingredient in ingredients.clone().into_iter() {
        for (start, end) in ranges.clone().into_iter() {
            if ingredient >= start && ingredient <= end {
                part_1 += 1;
                break;
            }
        }
    }

    println!("Part 1: {} ({:.2?})", part_1, now.elapsed());

    now = Instant::now();

    ranges.sort_by_key(|&(a, _)| a);
    let mut i = 1;
    while i < ranges.len() {
        if (ranges[i].0 >= ranges[i-1].0) && (ranges[i].0 <= ranges[i-1].1) {
            ranges[i].0 = ranges[i-1].0;
            if ranges[i].1 < ranges[i-1].1 {
                ranges.remove(i);
            }
            else {
                ranges.remove(i-1);
            }
        }
        else {
            i += 1;
        }
    }

    let mut part_2: i128 = 0;
    for (start, end) in ranges.clone().into_iter() {
        part_2 += end - start + 1;
    }

    println!("Part 2: {} ({:.2?})", part_2, now.elapsed());

    Ok(())
}
