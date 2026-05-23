//import { useState } from 'react'
//import reactLogo from './assets/react.svg'
//import viteLogo from './assets/vite.svg'
//import heroImg from './assets/hero.png'
//import { useEffect } from 'react';
import './App.css'


function App() {
  // const [count, setCount] = useState(0)
  // const[data, setData] = useState(null);

  // useEffect(() => {
  //   fetch('http://localhost:8000')
  //     .then(response => response.json())
  //     .then(data => setData(data))
  // }, []);
  ``

  return (
    <>
      <section id="center">
        <div id="hero">
          <h1>Employee Management System</h1>
        </div>
        <div id="datafield">
          <label htmlFor="employeeId">Employee ID:</label>
          <input type="text" id="employeeId" name="employeeId" />
          
          <label htmlFor="employeeName">Employee Name:</label>
          <input type="text" id="employeeName" name="employeeName" />

          <label htmlFor="employeeEmail">Employee Email:</label>
          <input type="email" id="employeeEmail" name="employeeEmail" />

          <label htmlFor="employeeDepartment">Employee Department:</label>
          <input type="text" id="employeeDepartment" name="employeeDepartment" />

          <button id="submitBtn">Submit</button>
        </div>
      </section>

      <section>

      </section>

      <section id="footer">
        <div id = "footer-content">
          <p>IAM Pvt. Ltd.</p>
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App
