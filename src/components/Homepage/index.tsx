import React from "react";
import "../Homepage/styles.scss"
import { Link } from "react-router-dom"

export function Homepage()  {
    return(
        <div className="homepage">
            {/* <img src="brand.svg" className="brand-logo" alt="brand logo"/> */}
            <h1 className="heading">Electric Cars, Solar & Energy</h1>
            <p className="range">RANGE CALCULATOR</p>
            <Link to="/cars">
                <button className="btn">ALL CARS</button>
            </Link>
        </div>
    );
}
