use std::cmp::max;

fn part1() -> i32 {
    let games: Vec<&str> = include_str!("../../input.txt").lines().collect();
    let mut games_id_sum = 0;
    'games_loop: for game in games {
        let game_data: Vec<&str> = game.split(":").collect();
        let game_id = game_data[0].split(" ").collect::<Vec<&str>>()[1]
            .parse::<i32>()
            .unwrap();
        let game_cubes: Vec<&str> = game_data[1].split(&[',', ';'][..]).collect();
        for cube in game_cubes {
            let cube_data: Vec<&str> = cube.trim().split(" ").collect();
            let cube_color = cube_data[1];
            let cube_number = cube_data[0].parse::<i32>().unwrap();
            if cube_color == "red" && cube_number > 12
                || cube_color == "green" && cube_number > 13
                || cube_color == "blue" && cube_number > 14
            {
                continue 'games_loop;
            }
        }
        games_id_sum += game_id
    }
    games_id_sum
}

fn part2() -> i32 {
    let games: Vec<&str> = include_str!("../../input.txt").lines().collect();
    let mut cubes_power_sum = 0;
    for game in games {
        let game_data: Vec<&str> = game.split(":").collect();
        let game_cubes: Vec<&str> = game_data[1].split(&[',', ';'][..]).collect();
        let (mut red_cubes, mut green_cubes, mut blue_cubes) = (0, 0, 0);
        for cube in game_cubes {
            let cube_data: Vec<&str> = cube.trim().split(" ").collect();
            let cube_color = cube_data[1];
            let cube_number = cube_data[0].parse::<i32>().unwrap();
            match cube_color {
                "red" => red_cubes = max(red_cubes, cube_number),
                "green" => green_cubes = max(green_cubes, cube_number),
                "blue" => blue_cubes = max(blue_cubes, cube_number),
                _ => (),
            }
        }
        cubes_power_sum += red_cubes * green_cubes * blue_cubes;
    }
    cubes_power_sum
}

fn main() {
    let part1_answer = part1();
    println!("Part 1: {}", part1_answer);

    let part2_answer = part2();
    println!("Part 2: {}", part2_answer);
}
