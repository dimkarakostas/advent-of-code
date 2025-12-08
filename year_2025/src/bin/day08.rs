use std::time::Instant;
use std::io;
use regex::Regex;
use std::collections::HashMap;
use year_2025::{read_lines};

fn distance_3d(point_a: (i128, i128, i128), point_b: (i128, i128, i128)) -> f64 {
    let dx = (point_a.0 - point_b.0) as f64;
    let dy = (point_a.1 - point_b.1) as f64;
    let dz = (point_a.2 - point_b.2) as f64;

    (dx * dx + dy * dy + dz * dz).sqrt()
}

fn main() -> io::Result<()> {
    let input_filename = "data/input08";

    let mut positions: Vec<(i128, i128, i128)> = Vec::new();
    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            let re = Regex::new(r"(?P<x>\d+),(?P<y>\d+),(?P<z>\d+)").unwrap();
            for caps in re.captures_iter(&line) {
                positions.push(
                    (caps["x"].parse().unwrap(), caps["y"].parse().unwrap(), caps["z"].parse().unwrap())
                );
            }
        }
    }

    let now = Instant::now();

    let mut distances: HashMap<((i128, i128, i128), (i128, i128, i128)), f64> = HashMap::new();
    for i in 0..positions.len() {
        for j in i+1..positions.clone().len() {
            distances.insert((positions[i], positions[j]), distance_3d(positions[i], positions[j]));
        }
    }

    let mut sorted_items_by_distance: Vec<(((i128, i128, i128), (i128, i128, i128)), f64)> = distances.iter().map(|(k, v)| (*k, *v)).collect();
    sorted_items_by_distance.sort_by(|a, b| a.1.partial_cmp(&b.1).unwrap());

    let mut line_points: HashMap<(i128, i128, i128), usize> = HashMap::new();

    let mut test_idx = 0;
    loop {
        let ((point_a, point_b), _) = sorted_items_by_distance[test_idx];
        if let Some(&line_name) = line_points.get(&point_a) {
            if let Some(&old_line) = line_points.get(&point_b) {
                if line_name != old_line {
                    for point in line_points.clone().keys().into_iter() {
                        if line_points[&point] == old_line {
                            line_points.insert(*point, line_name);
                        }
                    }
                }
            }
            else {
                line_points.insert(point_b, line_name);
            }
        }
        else if let Some(&line_name) = line_points.get(&point_b) {
            line_points.insert(point_a, line_name);
        }
        else {
            let line_name = line_points.keys().len();
            line_points.insert(point_a, line_name);
            line_points.insert(point_b, line_name);
        }
        test_idx += 1;
        if test_idx == 1000 {
            let mut freq = HashMap::new();
            for &value in line_points.values() {
                *freq.entry(value).or_insert(0) += 1;
            }
            let mut vals: Vec<usize> = freq.values().copied().collect();
            vals.sort_unstable_by(|a, b| b.cmp(a));
            let part_1: usize = vals.iter().take(3).product();

            println!("Part 1: {} ({:.2?})", part_1, now.elapsed());
        }

        if let Some(first) = line_points.values().next() {
            if (line_points.keys().len() == positions.len()) && (line_points.values().all(|v| v == first)) {
                let part_2 = point_a.0 * point_b.0;
                println!("Part 2: {} ({:.2?})", part_2, now.elapsed());
                break;
            }
        }
    }

    Ok(())
}
