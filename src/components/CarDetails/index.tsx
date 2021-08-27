import { Route, useParams } from "react-router-dom";
import { CarVariants } from "../interface";
import { useState, useEffect } from "react";
import "../CarDetails/styles.scss"

export function CarDetails(){
    const[carDetails, setCarDetails] = useState<CarVariants[] | any>();
    const { id } = useParams<any>();

    const getCarDetails = async() => {
        const response = await fetch(
            "http://localhost:8000/website/cars/variants/",
            {
                method: "GET"
            }
            );
            const data = await response.json();
            // console.log(data);
            setCarDetails(data.find((cardetails:any)=>(cardetails.car.id)===Number(id)));
        }
        
        useEffect(() => {
            getCarDetails();
        }, []);
    return(
        <div className="car-photo">
            <Route exact path="">
                <div >
                    <h1 className="heading-detail">{(carDetails?.car?.name)}</h1>
                    <button className="btndetails">Order</button>
                </div>
                <div className="details">
                    <p>{carDetails?.name}</p>
                {/* <p>{carDetails?.car?.}</p> */}
                    <p>{carDetails?.range}</p>
                    <p>{carDetails?.peak_power}</p>
                    <p>{carDetails?.top_speed}</p>
                    <p>{carDetails?.weight}</p>
                    <p>{carDetails?.cargo_capacity}</p>
                    <p>{carDetails?.power_train}</p>
                    <p>{carDetails?.acceleration}</p>
                    <p>{carDetails?.drag_coefficient}</p>
                    <p>{carDetails?.charging}</p>
                    <p>{carDetails?.car?.wheels}</p>
                </div>
                <div className="front-photo" />
                
                
            </Route>
            
        </div>
    );
}