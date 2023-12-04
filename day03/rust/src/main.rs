use std::collections::{HashMap, HashSet};

const OFFSETS: [i32; 3] = [-1, 0, 1];

fn part12() -> (i32, i32) {
    let mut sum = 0;
    let mut gear_rations_sum = 0;
    let mut gear_numbers: HashMap<(usize, usize), Vec<u32>> = HashMap::new();
    let engine: Vec<Vec<char>> = include_str!("../../input.txt")
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect();
    let (rows, cols) = (engine.len(), engine[0].len());
    for r in 0..rows {
        let mut n = 0;
        let mut has_part = false;
        let mut gears: HashSet<(usize, usize)> = HashSet::new();
        for c in 0..cols + 1 {
            if c < cols && engine[r][c].is_digit(10) {
                n = n * 10 + char::to_digit(engine[r][c], 10).unwrap();
                for off_r in OFFSETS.iter() {
                    for off_c in OFFSETS.iter() {
                        let (adj_r, adj_c) = (off_r + r as i32, off_c + c as i32);
                        if 0 < adj_r && adj_r < rows as i32 && 0 < adj_c && adj_c < cols as i32 {
                            if engine[adj_r as usize][adj_c as usize] == '*' {
                                gears.insert((adj_r as usize, adj_c as usize));
                            }
                            if !engine[adj_r as usize][adj_c as usize].is_digit(10)
                                && engine[adj_r as usize][adj_c as usize] != '.'
                            {
                                has_part = true;
                            }
                        }
                    }
                }
            } else if n > 0 {
                for gear in &gears {
                    gear_numbers.entry(*gear).or_insert(Vec::new()).push(n);
                }
                if has_part {
                    sum += n;
                    has_part = false;
                };
                n = 0;
                gears.drain();
            }
        }
    }
    for (_, numbers) in gear_numbers.iter() {
        if numbers.len() == 2 {
            gear_rations_sum += numbers[0] * numbers[1];
        }
    }
    (sum as i32, gear_rations_sum as i32)
}

fn main() {
    let (part1_answer, part2_answer) = part12();
    println!("Part 1: {}", part1_answer);
    println!("Part 2: {}", part2_answer);
}
