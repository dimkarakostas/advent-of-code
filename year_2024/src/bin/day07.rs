use std::time::Instant;
use std::io;
use regex::Regex;
use year_2024::{read_lines};

fn detect(txt: &str) -> Result<(u128, Vec<u128>), Box<dyn std::error::Error>> {
    let re = Regex::new(r"^(\d+):((\s*[0-9]+)+)\s*$")?;
    let caps = re.captures(txt).ok_or("no match")?;
    let result = caps
        .get(1)
        .unwrap()
        .as_str()
        .parse()
        .unwrap();
    let values = caps
        .get(2)
        .unwrap()
        .as_str()
        .split_ascii_whitespace()
        .filter_map(|s| s.parse().ok())
        .collect();
    Ok((result, values))
}

fn get_combos(target: u128, nums: Vec<u128>, is_part_2: bool) -> Vec<u128> {
    let mut new_nums: Vec<u128> = Vec::new();
    if nums.len() == 2 {
        if nums[0] + nums[1] <= target {
            new_nums.push(nums[0] + nums[1]);
        }
        if nums[0] * nums[1] <= target {
            new_nums.push(nums[0] * nums[1]);
        }

        if is_part_2 {
            let concat = format!("{}{}", nums[0], nums[1]).parse().unwrap();
            if concat <= target {
                new_nums.push(concat);
            }
        }
    }
    else {
        let res = get_combos(target, nums[0..nums.len()-1].to_vec(), is_part_2); 
        let last_elem = nums[nums.len()-1];
        for num in res {
            if num + last_elem <= target {
                new_nums.push(num + last_elem);
            }
            if num * last_elem <= target {
                new_nums.push(num * last_elem);
            }

            if is_part_2 {
                let concat = format!("{}{}", num, last_elem).parse().unwrap();
                if concat <= target {
                    new_nums.push(concat);
                }
            }
        }
    }

    new_nums
}

fn main() -> io::Result<()> {
    let input_filename = "data/input07";

    let now = Instant::now();
    let mut part1 = 0;
    let mut part2 = 0;
    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            if let Ok((target, nums)) = detect(&line) {
                let combos_1 = get_combos(target, nums.clone(), false);
                if combos_1.contains(&target) {
                    part1 += target;
                    part2 += target;
                }
                else {
                    let combos_2 = get_combos(target, nums.clone(), true);
                    if combos_2.contains(&target) {
                        part2 += target;
                    }
                }
            }
        }
    }
    println!("Part 1: {} ({:.2?})", part1, now.elapsed());
    println!("Part 2: {} ({:.2?})", part2, now.elapsed());

    Ok(())
}
