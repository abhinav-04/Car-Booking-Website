import React, { useEffect, useState } from "react";
import "./styles.scss"
import { CarModel } from "../CarModel";
import { Car } from "../interface"

// interface Car{
//     cars:{
//         id: number;
//         name: string;
//         start_range: number;
//         Time_to_60: number;
//         top_speed: string;
//         peak_power: string;
//         base_price: number
//     };
// }

export function CarList(){

    const[cars, setCars] = useState<Car[]>();
    
    const getCars = async() => {
        const response = await fetch(
            "http://localhost:8000/website/car-list/",
            {
                method: "GET"
            }
            );
            const data = await response.json();
            // console.log(data);
            setCars(data);
        }
        
        useEffect(() => {
            getCars();
        }, []);
        // useEffect(() => {
        //         fetch("http://127.0.0.1:8000/website/car-list/")
        //             .then(res => {
        //                     return res.json();
        //                 })
        //                 .then(data => {
        //                         setCars(data);
        //                     }); 
        //             }); 
                    
    return(
        <div>
            <h1 className = "heading-list">ALL MODELS</h1>
            {/* {console.log(cars && cars.cars)} */}
            {/* <h1>{cars && cars.cars.name}</h1> */}
            <div className="card-wrapper">
                {cars && cars.map((item,index)=>{
                    return <CarModel car={item} key={index}/>
                })}
            </div>
        </div>
    );
}