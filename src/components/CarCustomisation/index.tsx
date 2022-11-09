// import { Route, useParams } from "react-router-dom";
// import { useState, useEffect } from "react";
// import "./styles.scss"
// import { CarVariants } from "../interface";

// export function CarCustomisation(){
//     const[carDetails, setCarDetails] = useState<CarVariants[] | any>();
//     const { id } = useParams<any>();

//     const getCarDetails =async () => {
//         const response = await fetch(
//         "http://localhost:8000/website/cars/variants/",
//         {
//             method: "GET"
//         }
//         );
//         const data = await response.json()
//         setCarDetails(data.find((cardetails:any) =>(cardetails.car.id)===Number(id)));
//     }

// useEffect(() =>{
//     getCarDetails();
// }, []);
//     return(
//         <div className="car-photo">
//             {/* <img src="" alt="" /> */
//         </div>
//     )
// }