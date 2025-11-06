use std::time::Instant;
use std::io;
use regex::Regex;
use std::collections::HashMap;
use std::collections::BinaryHeap;
use year_2024::{read_lines};

fn main() -> io::Result<()> {
    let input_filename = "data/input05";

    let mut rules: Vec<(i32, i32)> = Vec::new();

    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            if line.contains("|") {
                let re = Regex::new(r"(?P<u>\d+)\|(?P<v>\d+)").unwrap();
                for caps in re.captures_iter(&line) {
                    rules.push((caps["u"].parse().unwrap(), caps["v"].parse().unwrap()))
                }
            }
        }
    }

    let now = Instant::now();
    let mut part_1_output: i32 = 0;
    let mut part_2_output: i32 = 0;
    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            if line.contains(",") {
                let mut update_vector: Vec<i32> = Vec::new();
                let re = Regex::new(r"(?P<num>\d+),?").unwrap();
                for caps in re.captures_iter(&line) {
                    update_vector.push(caps["num"].parse().unwrap());
                }

                let mut correct_update_flag: bool = true;
                for (u, v) in rules.clone().into_iter() {
                    if update_vector.contains(&u) && update_vector.contains(&v) {
                        if update_vector.iter().position(|&r| r == u).unwrap() > update_vector.iter().position(|&r| r == v).unwrap() {
                            correct_update_flag = false;
                            break;
                        }
                    }
                }

                if correct_update_flag {
                    part_1_output += update_vector[update_vector.len()/2];
                }
                else {
                    let mut indeg: HashMap<i32, i32> = HashMap::new();
                    let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();

                    for n in update_vector.clone().into_iter() {
                        indeg.insert(n, 0);
                    }
                    for (u, v) in rules.clone().into_iter() {
                        if update_vector.contains(&u) && update_vector.contains(&v) {
                            indeg.insert(v, indeg[&v]+1);
                            graph.entry(u).or_insert(Vec::new()).push(v);
                        }
                    }
                    let mut min_h = BinaryHeap::new();
                    for num in update_vector.clone().into_iter() {
                        if indeg[&num] == 0 {
                            min_h.push(num);
                        }
                    }

                    let mut out_vector: Vec<i32> = Vec::new();
                    while !min_h.is_empty() {
                        let elem = min_h.pop().unwrap();
                        out_vector.push(elem);
                        for edge_elem in graph.entry(elem).or_insert(Vec::new()).clone() {
                            indeg.insert(edge_elem, indeg[&edge_elem]-1);
                            if indeg[&edge_elem] == 0 {
                                min_h.push(edge_elem);
                            }
                        }
                    }
                    part_2_output += out_vector[out_vector.len()/2];
                }
            }
        }
    }

    println!("Part 1: {} ({:.2?})", part_1_output, now.elapsed());
    println!("Part 2: {} ({:.2?})", part_2_output, now.elapsed());

    Ok(())
}
