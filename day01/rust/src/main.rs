fn part1() -> u32 {
    include_str!("../../input.txt")
        .lines()
        .map(|line| {
            line.chars()
                .filter(|ch| ch.is_digit(10))
                .map(|digit| digit.to_digit(10).unwrap())
                .collect::<Vec<u32>>()
        })
        .map(|digits| digits[0] * 10 + digits[digits.len() - 1])
        .sum::<u32>()
}

fn part2() -> u32 {
    let number_words = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];
    let lines: Vec<String> = include_str!("../../input.txt")
        .lines()
        .map(|line| line.to_string())
        .collect();
    let mut numbers: Vec<u32> = Vec::new();

    for line in lines {
        let mut line_digits: Vec<u32> = Vec::new();
        for (index, ch) in line.chars().enumerate() {
            if ch.is_digit(10) {
                line_digits.push((ch as u8 - '0' as u8) as u32);
                continue;
            }
            for (number_word_index, number_word) in number_words.iter().enumerate() {
                if line[..index].starts_with(number_word) {
                    line_digits.push(number_word_index as u32 + 1)
                }
            }
        }
        numbers.push(line_digits[0] * 10 + line_digits[line_digits.len() - 1])
    }
    return numbers.iter().sum();
}

fn main() {
    let part1_answer = part1();
    println!("Part 1: {}", part1_answer);

    let part2_answer = part2();
    println!("Part 2: {}", part2_answer);
}
