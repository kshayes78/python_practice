import React, { useState } from 'react';

function TurnoutCalc() {
  const [midtermTurnout1, setMidTermTurnout1] = useState(0);
  const [midtermTurnout2, setMidTermTurnout2] = useState(0);
  const [midtermTurnout3, setMidTermTurnout3] = useState(0);
  const [averageTurnout, setAverageTurnout] = useState(0);
  const [totalVoters, setTotalVoters] = useState(0);

  function handleTurnout(e) {
    setMidTermTurnout1(e.target.value);
  }

  function handleTurnout2(e) {
    setMidTermTurnout2(e.target.value);
  }
  function handleTurnout3(e) {
    setMidTermTurnout3(e.target.value);
  }

  function turnoutAverage(e) {
    e.preventDefault();
    setAverageTurnout(
      Math.ceil(
        parseInt(midtermTurnout1) +
          parseInt(midtermTurnout2) +
          parseInt(midtermTurnout3)
      ) / 3
    );
  }

  function handleTurnoutPercent() {
    midtermYrTurnout / totalVoters;
  }

  return (
    <div className='container'>
      <h2>Turnout Calculator</h2>
      <form>
        <label htmlFor='turnout'>
          Please enter Total Voter Turnout % for 2010:
        </label>
        <input
          onChange={handleTurnout}
          type='number'
          id='turnout'
          name='turnout'
          required
          minLength='1'
        ></input>
        <label for='turnout'>
          Please enter Total Voter Turnout % for 2014:{' '}
        </label>
        <input
          onChange={handleTurnout2}
          type='number'
          id='turnout'
          name='turnout'
          required
          minLength='1'
        ></input>
        <label for='turnout'>
          Please enter Total Voter Turnout % for 2018:{' '}
        </label>
        <input
          onChange={handleTurnout3}
          type='number'
          id='turnout'
          name='turnout'
          required
          minLength='1'
        ></input>
        <button onClick={turnoutAverage}>Submit</button>
        <h2>Your average turnout is {averageTurnout}%.</h2>
      </form>
    </div>
  );
}

export default TurnoutCalc;
