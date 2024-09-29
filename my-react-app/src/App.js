import React, { useState, useEffect, useCallback } from 'react';
import './styles.css';
import pfp from './pfp.png';

function App() {
  // eslint-disable-next-line
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);
  const [searchParams, setSearchParams] = useState({
    price: '',
    calories: '',
    protein: '',
    time: [], // This will hold multiple days
  });


  const handleInputChange = (e) => {
    const { name, value, checked } = e.target;
    if (name === 'time') {
      setSearchParams(prev => ({
        ...prev,
        time: checked
          ? [...prev.time, value]
          : prev.time.filter(day => day !== value)
      }));
    } else {
      setSearchParams(prev => ({ ...prev, [name]: value }));
    }
  };




  const [results, setResults] = useState(null);

  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

  const handleNext = () => {
    if (!isAnimating) {
      setIsAnimating(true);
      setCurrentIndex((prevIndex) => (prevIndex + 3) % days.length);
      setTimeout(() => setIsAnimating(false), 300);
    }
  };

  const handlePrev = () => {
    if (!isAnimating) {
      setIsAnimating(true);
      setCurrentIndex((prevIndex) => (prevIndex - 3 + days.length) % days.length);
      setTimeout(() => setIsAnimating(false), 300);
    }
  };

  const fetchMealSuggestions = useCallback(async () => {
    const resultsByDay = {};
    try {
      await Promise.all(searchParams.time.map(async (day) => {
        const response = await fetch(
          `http://127.0.0.1:8000/api/search?day=${day}&calorie_threshold=${searchParams.calories}&protein_threshold=${searchParams.protein}&price_threshold=${searchParams.price}`
        );
        if (!response.ok) throw new Error(`Failed to fetch meals for ${day}`);
        const data = await response.json();
        resultsByDay[day] = data;  // Store data keyed by day
      }));
      setResults(resultsByDay); // Update state with results for all selected days
    } catch (error) {
      console.error('Error fetching meal suggestions:', error);
      setResults(null); // Reset results on error
    }
  }, [searchParams]);




  useEffect(() => {
    if (
      searchParams.time !== 'Select Time' &&
      searchParams.calories &&
      searchParams.protein &&
      searchParams.price
    ) {
      fetchMealSuggestions();
    }
  }, [searchParams.time, searchParams.calories, searchParams.protein, searchParams.price, fetchMealSuggestions]);

  return (
    <div>
      <h1 className="app-title">GreenBack</h1>
      <div className="App">
        <div className="sidebar">
          <div className="pfp">
            <img src={pfp} alt="Profile" className="profile-icon" />
          </div>
          <div className="buttons">
            <button className="sidebar-button">Schedule</button>
            <button className="sidebar-button">Feed</button>
            <button className="sidebar-button">For You Page</button>
          </div>
        </div>
        <div className="main-content">
          <div className="header">
            <div className="search-bars">
              <input
                type="number"
                name="price"
                placeholder="Price Threshold"
                value={searchParams.price}
                onChange={handleInputChange}
                className="search-input"
              />
              <input
                type="number"
                name="calories"
                placeholder="Calories Threshold"
                value={searchParams.calories}
                onChange={handleInputChange}
                className="search-input"
              />
              <input
                type="number"
                name="protein"
                placeholder="Protein Threshold"
                value={searchParams.protein}
                onChange={handleInputChange}
                className="search-input"
              />
              <div className="search-days">
                {days.map((day) => (
                  <label key={day}>
                    <input
                      type="checkbox"
                      name="time"
                      value={day}
                      checked={searchParams.time.includes(day)}
                      onChange={handleInputChange}
                    /> {day}
                  </label>
                ))}
              </div>




              <button onClick={fetchMealSuggestions} className="search-button">
                Search
              </button>
            </div>
          </div>
          <div className={`calendar-container ${isAnimating ? 'animating' : ''}`}>
            <button className="nav-button" onClick={handlePrev}>
              ❮
            </button>
            <div className="calendar">
              {searchParams.time.map((day) => (
                <div key={day} className="day">
                  {day}
                  <div className="day-content scrollable-content">
                    {results && results[day] && (
                      <div className="meal-item">
                        {['breakfast', 'lunch', 'dinner'].map((mealType) => (
                          results[day][mealType] && (
                            <div key={mealType}>
                              <h4>{mealType}: {results[day][mealType].items.join(', ')} (from {results[day][mealType].restaurant})</h4>
                              <p>Calories: {results[day][mealType].total_calories}</p>
                              <p>Protein: {results[day][mealType].total_protein}g</p>
                              <p>Price: ${results[day][mealType].total_price.toFixed(2)}</p>
                            </div>
                          )
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>




            <button className="nav-button" onClick={handleNext}>
              ❯
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
