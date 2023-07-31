import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import '../App.css';

const Results = () => {
    const location = useLocation();
    const navigate = useNavigate();
    const data = location?.state?.series;

    const goBack = (e) => {
        e.preventDefault();
        navigate("/");
    }

    return (
        <section className='results'>
            <div>
                <button onClick={goBack}>Go Back - Try Another Value</button>
                <h4>The First {data.length} Fibonacci Numbers: </h4>
            </div>
            <div>
                {data?.map((ele, i) => [
                i > 0 && ", ",
                <span key={i}>{ele}</span>
                ])
            }
            </div>
        </section>
    );
}

export default Results;