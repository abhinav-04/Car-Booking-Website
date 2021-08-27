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
        
        <div className="card">
            <Link to={`cars/${id}` }>
            <p>{name}</p>
            <p>{start_range}</p>
            <p>{Time_to_60}</p>
            <p>{top_speed}</p>
            <p>{peak_power}</p>
            <p>{base_price}</p>
            </Link>
        </div>
    )
}
