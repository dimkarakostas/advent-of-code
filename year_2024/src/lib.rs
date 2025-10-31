use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;

pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn count_first_line_length(path: &str) -> Result<usize, io::Error> {
    let mut count = 0;
    if let Ok(lines) = read_lines(path) {
        for line in lines.map_while(Result::ok) {
            count = line.chars().count();
        }
    }
    Ok(count)
}

pub fn count_lines_in_file(path: &str) -> Result<usize, io::Error> {
    let input = File::open(path)?;
    let buffered = BufReader::new(input);
    let count = buffered.lines().count();
    Ok(count)
}
