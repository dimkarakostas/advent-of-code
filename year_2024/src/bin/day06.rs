use std::time::Instant;
use std::collections::HashSet;
use year_2024::read_lines;

fn get_position(input: Vec<Vec<char>>) -> Option<(usize, usize)> {
    for row_idx in 0..input.len() {
        for col_idx in 0..input[0].len() {
            let character = input[row_idx][col_idx];
            if matches!(character, '^' | '>' | '<' | 'v') {
                return Some((row_idx, col_idx));
            }
        }
    }
    None
}

fn run(input_table: Vec<Vec<char>>) -> (HashSet<(usize, usize, char)>, bool) {
    let (mut x, mut y) = get_position(input_table.clone()).unwrap_or((usize::MAX, usize::MAX));
    let mut direction = input_table[x][y];

    let mut visited: HashSet<(usize, usize, char)> = Vec::new().into_iter().collect();
    let mut looped = false;
    loop {
        let visited_tuple = (x, y, direction);
        if visited.contains(&visited_tuple) {
            looped = true;
            break;
        }
        visited.insert(visited_tuple);
        if direction == '^' {
            if x == 0 {
                break;
            }
            if input_table[x-1][y] != '#' {
                x -= 1;
                direction = '^';
            }
            else {
                direction = '>';
            }
        }
        else if direction == '>' {
            if y == input_table[0].len()-1 {
                break;
            }
            if input_table[x][y+1] != '#' {
                y += 1;
                direction = '>';
            }
            else {
                direction = 'v';
            }
        }
        else if direction == 'v' {
            if x == input_table.len()-1 {
                break;
            }
            if input_table[x+1][y] != '#' {
                x += 1;
                direction = 'v';
            }
            else {
                direction = '<';
            }
        }
        else if direction == '<' {
            if y == 0 {
                break;
            }
            if input_table[x][y-1] != '#' {
                y -= 1;
                direction = '<';
            }
            else {
                direction = '^';
            }
        }
    }

    (visited, looped)
}

fn main() {
    let input_filename = "data/input06";

    let mut input_table: Vec<Vec<char>> = Vec::new();
    if let Ok(lines) = read_lines(input_filename) {
        for (row_idx, line) in lines.map_while(Result::ok).enumerate() {
            input_table.push(Vec::new());
            for character in line.chars() {
                input_table[row_idx].push(character);
            }
        }
    }

    let (visited, _) = run(input_table.clone());

    let now = Instant::now();

    let cleaned_visited: HashSet<(usize, usize)> = visited.iter().map(|&(a, b, _) | (a, b)).collect();
    let part1 = cleaned_visited.len();
    println!("Part 1: {} ({:.2?})", part1, now.elapsed());

    let now = Instant::now();
    let mut part2 = 0;
    for (row_idx, col_idx) in cleaned_visited {
        if input_table[row_idx][col_idx] == '.' {
            let mut new_table = input_table.clone();
            new_table[row_idx][col_idx] = '#';
            let (_, looped) = run(new_table);
            if looped {
                part2 += 1;
            }
        }
    }
    println!("Part 2: {} ({:.2?})", part2, now.elapsed());
}
