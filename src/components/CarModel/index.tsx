import React from "react";
import { Link } from "react-router-dom";
import { Car } from "../interface"
import "../CarModel/styles.scss"

interface ICarModelProps{
    car: Car;
}
export function CarModel(props:ICarModelProps){
    const {car} = props;
    const {name, start_range, Time_to_60 ,top_speed, peak_power, base_price, id} = car;
    return( 
        
        <div className="card" id="text">
            <Link to={`cars/${id}` }>
                <img src="photos/1models.png" alt="model s"/>
                <br />
                <p id="car-name">{name} </p>
                <p id="car-range" >{start_range} mi</p>
                <br />
                <p id = "stats">{Time_to_60}s</p>
                <p id = "stats">{top_speed} Mph</p>
                <p id = "stats">{peak_power} HP</p>
                <p id = "stats">${base_price}</p>
                <br />
                <p id="stat-names">0-60 </p>
                <p id="stat-names">Top Speed</p>
                <p id="stat-names">Peak Power</p>
                <p id="stat-names">Starts</p>

            </Link>
        </div>
    )
}
