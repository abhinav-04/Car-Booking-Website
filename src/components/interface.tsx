// import React from "react";

export interface Car{
    id: number;
    name: string;
    start_range: string;
    Time_to_60: string;
    top_speed: string;
    peak_power: string;
    base_price: number;
}

export interface CarVariants{
    "id": 1,
    name: string;
    add_on_price: number;
    range: string;
    peak_power: string;
    top_speed: string;
    weight: string;
    cargo_capacity: string;
    power_train: string;
    acceleration: string;
    drag_coefficient: string;
    charging: string;
    car: {
        id: number;
        name: string;
    }
}