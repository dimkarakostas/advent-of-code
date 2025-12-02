use std::time::Instant;
use std::io;
use regex::Regex;
use year_2025::{read_lines};

fn split_middle(s: &str) -> Option<(String, String)> {
    let len = s.chars().count();
    if len % 2 != 0 {
        return None;
    }

    let mid = len / 2;
    let first: String = s.chars().take(mid).collect();
    let second: String = s.chars().skip(mid).collect();

    Some((first, second))
}

fn split_chunks(s: &str, n: usize) -> Option<Vec<String>> {
    let chars: Vec<char> = s.chars().collect();

    if chars.len() % n != 0 {
        return None;
    }

    let mut result = Vec::new();
    for chunk in chars.chunks(n) {
        result.push(chunk.iter().collect());
    }

    Some(result)
}

fn main() -> io::Result<()> {
    let input_filename = "data/input02";

    let mut ranges: Vec<(i128, i128)> = Vec::new();
    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            let re = Regex::new(r"(?P<start>\d+)-(?P<end>\d+)").unwrap();
            for caps in re.captures_iter(&line) {
                ranges.push((caps["start"].parse().unwrap(), caps["end"].parse().unwrap()));
            }
        }
    }

    let mut now = Instant::now();
    let mut part_1: i128 = 0;
    for (start, end) in ranges.clone().into_iter() {
        for i in start..=end {
            let s = i.to_string();
            if let Some((a, b)) = split_middle(&s) {
                if a == b {
                    part_1 += i;
                }
            }
        }
    }

    println!("Part 1: {} ({:.2?})", part_1, now.elapsed());

    now = Instant::now();
    let mut part_2: i128 = 0;
    for (start, end) in ranges.clone().into_iter() {
        for num in start..=end {
            let s = num.to_string();
            for slice_size in 1..=s.chars().count()/2 {
                if let Some(slice_vector) = split_chunks(&s, slice_size) {
                    if let Some(first) = slice_vector.first() {
                        if slice_vector.iter().all(|s| s == first) {
                            part_2 += num;
                            break
                        }
                    }
                }
            }
        }
    }

    println!("Part 2: {} ({:.2?})", part_2, now.elapsed());

    Ok(())
}
