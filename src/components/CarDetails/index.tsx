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

        //Variant Button Selection Method
        const button1 = document.querySelector('#plaid');
        const button2 = document.querySelector('#lrange');
        button1?.addEventListener('click',() => buttonClick(button1,button2) );
        button2?.addEventListener('click',() => buttonClick(button2,button1) );
        function buttonClick(btnadd:any, btnrmv:any){
            btnadd.classList.add('pressed');
            btnrmv.classList.remove('pressed')
        }

    return(
        <div className="car-photo">
            <Route exact path="">
                <div >
                    <h1 className="heading-detail">{(carDetails?.car?.name)}</h1>
                    <button id="ord-btn">Order</button>
                </div>
                <div className="details">

                    <p className="nm-car">{carDetails?.car.name} Specs</p>
                    <button className="btndetails" id="plaid">Plaid</button>
                    <button className="btndetails" id="lrange">Long Range</button>

                    <table>
                        <tr>
                            <th>Range</th>
                            <th>Power Train</th>
                        </tr>
                        <tr>
                            <td>{carDetails?.range}</td>
                            <td>{carDetails?.power_train}</td>
                        </tr>
                        <tr>
                            <th>Peak Power</th>
                            <th>Acceleration</th>
                        </tr>
                        <tr>
                            <td>{carDetails?.peak_power}</td>
                            <td>{carDetails?.acceleration}</td>
                        </tr>
                        <tr>
                            <th>Top Speed</th>
                            <th>Drag Coefficient</th>
                        </tr>
                        <tr>
                            <td>{carDetails?.top_speed}</td>
                            <td>{carDetails?.drag_coefficient}</td>
                        </tr>
                        <tr>
                            <th>Weight</th>
                            <th>Wheels</th>
                        </tr>
                        <tr>
                            <td>{carDetails?.weight}</td>
                            <td>{carDetails?.car?.wheels}</td>
                        </tr>
                        <tr>
                            <th>Cargo Capacity</th>
                            <th>Charging</th>
                        </tr>
                        <tr>
                            <td>{carDetails?.cargo_capacity}</td>
                            <td>{carDetails?.charging}</td>
                        </tr>
                    </table>

                {/* <p>{carDetails?.car?.}</p> */}
                    {/* <p>{carDetails?.range}</p>
                    <p>{carDetails?.peak_power}</p>
                    <p>{carDetails?.top_speed}</p>
                    <p>{carDetails?.weight}</p>
                    <p>{carDetails?.cargo_capacity}</p>
                    <p>{carDetails?.power_train}</p>
                    <p>{carDetails?.acceleration}</p>
                    <p>{carDetails?.drag_coefficient}</p>
                    <p>{carDetails?.charging}</p>
                    <p>{carDetails?.car?.wheels}</p> */}
                </div>
                <div className="front-photo" />
                
                
            </Route>
            
        </div>
    );
}