import React, { useState, useEffect } from 'react';
import './styles.css';
import pfp from './pfp.png';

function App() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);
  const [searchParams, setSearchParams] = useState({
    price: '',
    calories: '',
    protein: '',
    time: 'Select Time',
  });
  const [results, setResults] = useState([]);

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

  const visibleDays = [
    days[currentIndex],
    days[(currentIndex + 1) % days.length],
    days[(currentIndex + 2) % days.length],
  ];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setSearchParams({ ...searchParams, [name]: value });
  };

  const fetchMealSuggestions = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/search?day=${searchParams.time}&calorie_threshold=${searchParams.calories}&protein_threshold=${searchParams.protein}&price_threshold=${searchParams.price}`
      );
      if (!response.ok) {
        throw new Error('No suitable meals found');
      }
      const data = await response.json();
      console.log('Response from backend:', data); // Log the response to the console
      setResults([data.best_combination]); // Set results to display the best combination
    } catch (error) {
      console.error('Error fetching meal suggestions:', error);
      setResults([]); // Reset results to empty array on error
    }
  };

  useEffect(() => {
    if (
      searchParams.time !== 'Select Time' &&
      searchParams.calories &&
      searchParams.protein &&
      searchParams.price
    ) {
      fetchMealSuggestions();
    }
  }, [searchParams.time, searchParams.calories, searchParams.protein, searchParams.price]);

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
              <select
                name="time"
                value={searchParams.time}
                onChange={handleInputChange}
                className="search-input"
              >
                <option value="Select Time" disabled>
                  Select Time
                </option>
                {days.map((day) => (
                  <option key={day} value={day}>
                    {day}
                  </option>
                ))}
                <option value="Plan My Week!">Plan My Week!</option>
              </select>
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
              {visibleDays.map((day) => (
                <div key={day} className="day">
                  {day}
                  <div className="day-content">
                    {results?.map((result, index) => (
                      <div key={index} className="meal-item">
                        <h4>Items: {result.items.join(', ')}</h4>
                        <p>Total Calories: {result.total_calories}</p>
                        <p>Total Protein: {result.total_protein}g</p>
                        <p>Total Price: ${result.total_price.toFixed(2)}</p>
                      </div>
                    ))}
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
