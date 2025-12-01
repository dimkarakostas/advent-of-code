use std::time::Instant;
use std::io;
use year_2025::{read_lines};

fn main() -> io::Result<()> {
    let input_filename = "data/input01";

    let mut rotor_position: i32 = 50;

    let now = Instant::now();
    
    let mut part_1: i32 = 0;
    let mut part_2: i32 = 0;
    if let Ok(lines) = read_lines(input_filename) {
        for line in lines.map_while(Result::ok) {
            let (direction, num) = line.split_at(1);
            let mut rotation: i32 = num.parse().unwrap();

            part_2 += rotation / 100;

            rotation %= 100;

            if direction == "L" {
                if (rotor_position != 0) && (rotor_position <= rotation) {
                    part_2 += 1;
                }
                rotor_position = (rotor_position - rotation + 100) % 100;
            }
            else if direction == "R" {
                if rotor_position + rotation > 99 {
                    part_2 += 1;
                }
                rotor_position = (rotor_position + rotation) % 100;
            }
            if rotor_position == 0 {
                part_1 += 1;
            }
        }
    }

    println!("Part 1: {} ({:.2?})", part_1, now.elapsed());
    println!("Part 2: {} ({:.2?})", part_2, now.elapsed());

    Ok(())
}
