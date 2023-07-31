import React from "react";
import {useState} from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import '../App.css';
const baseUrl = "http://localhost:5000"
const Home = () => {
    const navigate = useNavigate();
    const [fiboNum, setFiboNum] = useState("");
    const [fiboResult, setFiboResult] = useState([]);

    const handleChange = e => {
        if (parseInt(e.target.value) > 0 || e.target.value === '')
            setFiboNum(e.target.value);
    };
    


    const handleSubmit = async(e) => {
        e.preventDefault();
        try {
            if (fiboNum !== '' && fiboNum > 0){
                const data = await axios.get(`${baseUrl}/fiboValue`, { params: { num: fiboNum } });
                let fiboArr = data?.data.data;
                setFiboResult(fiboArr);
                navigate("/results", 
                    {
                        state: {series: fiboArr}
                    }
                );  
            }
        } catch (err) {
            console.log(err.message);
        }
    };
    
    return (
        <section className='fiboForm'>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor='fibonacci-number'>Fibonacci Number(Input a number greater than 0): </label>
                    <p>The app will generate the first N fibonacci numbers (N - The number you input in the box below, <b>UPTO N=92</b>)</p>
                </div>
                <div className="fiboInput">
                    <input 
                    onChange={handleChange}
                    type="number"
                    name='fibonacci-number'
                    id='fibonnaci-number'
                    value={fiboNum}
                    ></input>
                    <button type='submit'>Submit</button>
                </div>
                
            </form>
        </section>
    );
}

export default Home;